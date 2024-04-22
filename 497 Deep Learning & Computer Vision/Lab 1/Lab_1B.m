%{
Andrew Kozempel
CMPSC 497
Fall 2023
LAB #1B Cookie Defect Detector
%}

% Initialize running totals
total_crackers = 0;
total_good = 0;
total_bad = 0;

%images = {'cracker10.png'};
images = {'cracker1.png', 'cracker2.png', 'cracker3.png', 'cracker4.png', 'cracker5.png', 'cracker6.png', 'cracker7.png', 'cracker8.png', 'cracker9.png', 'cracker10.png'};


for i = 1:length(images)

    % Access original RGB image
    RGB = imread(images{i});
    figure, imshow(RGB);
    
    % Create grayscale image
    gray = rgb2gray(RGB);
    threshold = graythresh(gray);
    %figure, imshow(gray);
    
    % Create bw (binary image)
    bw = im2bw(gray, threshold);
    %figure, imshow(bw);
    
    % Remove all object containing fewer than 30 pixels
    bw1 = bwareaopen(bw, 30);
    %figure, imshow(bw1);
    
    % Fill a gap in the pen's cap
    se = strel('disk', 2); % Structuring element; "paintbrush"
    bw2 = imclose(bw1, se); % We will cover later in course
    %figure, imshow(bw2);
    
    % Fill any holes, so that regionprops can be used to estimate the area 
    % enclosed by each of the boundaries
    bw3 = imfill(bw2, 'holes');
    %figure, imshow(bw3);
    
    % Get pixels for boundaries of each object
    [B,L] = bwboundaries(bw3, 'noholes');
    
    % Display the label matrix and draw each boundary
    figure, imshow(label2rgb(L, @jet, [.5 .5 .5]));
    
    % Allow graphics to be added to same plot
    hold on;
    
    % length(B) is number of objects
    for k = 1:length(B)
        % B is “cell” data type (set)
        boundary = B{k};
        plot(boundary(:,2), boundary(:,1), 'w', 'LineWidth', 2);
    end
    
    % Find area(in pixels) and centroid (x, y) for each object in label matrix
    stats = regionprops(L, 'Area', 'Centroid'); 
    
    % Arbitrary value (change as needed)
    threshold = 0.75; 
    
    
    fprintf('\nCracker %d:', i);
    % Loop over the boundaries (each object has a boundary)
    for k = 1:length(B)
    
        % Obtain (X,Y) boundary coordinates corresponding to label 'k'
        boundary = B{k};
    
        % Compute a simple estimate of the object's perimeter
    
        % Find 2-col. array of (x2-x1)^2 and (y2-y1)^2
        delta_sq = diff(boundary).^2; 
    
        % Sum (row) and take sqrt to find dist.
        % Then sum all distances to find perimeter
        perimeter = sum(sqrt(sum(delta_sq,2))); 
    
        area1 = perimeter^2/(4*pi);
    
        % Obtain the area calculation corresponding to label 'k'
        area2 = stats(k).Area; % So, we calculated the area 2 different ways
    
        % Compute the roundness metric (compare 2 methods)
        metric = area2/area1; % Circular objects have metric close to 1
    
        % Display the results
        metric_string = sprintf('%2.2f', metric);
   

        % Mark objects above the threshold with a small black circle in the center of the object
        if metric > threshold
            centroid = stats(k).Centroid;
            plot(centroid(1), centroid(2), 'ko');
    
            % Increment the round object count
            total_good = total_good + 1;
            % Print test case
            fprintf(' GOOD (%0.2f)', metric);

        else

            % Increment the round object count
            total_bad = total_bad + 1;
            % Print test case
            fprintf(' BAD (%0.2f)', metric);

        end
    
        text(boundary(1,2)-35, boundary(1,1)+13, metric_string, 'Color', 'y', 'FontSize', 14, 'FontWeight', 'bold');
    end
    
    total_crackers = total_crackers + 1;
end

% Print total number of crackers
fprintf('\n\nTotal Number of crackers: %d\n', total_crackers);

%Print total number of good crackers
fprintf('Total Number of good crackers: %d\n', total_good);

%Print total number of bad crackers
fprintf('Total Number of bad crackers: %d\n', total_crackers-total_good);