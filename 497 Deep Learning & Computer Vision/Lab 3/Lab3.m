%{
Andrew Kozempel
CMPSC 497
Fall 2023
LAB #3: Color Tracking with Images
%}

% load images
images = {'img1.jpg', 'img2.jpg', 'img3.jpg'};

% loop through images
for i = 1:length(images)

    % read image
    RGB = imread(images{i});
    fprintf('\nImage %d: ', i);
    fprintf('\nSize: %d x %d', size(RGB, 1), size(RGB, 2));

    % split into R, G, B planes
    r = RGB(:, :, 1);
    g = RGB(:, :, 2);
    b = RGB(:, :, 3);
    
    % create a binary mask for red objects based on heuristic
    redMask = (r > 2*g) & (r > 2*b) & (r > 30);
    
    % apply morphological closing
    se = strel('disk', 35);
    redClosed = imclose(redMask, se);
    
    % remove small objects
    redObjects = bwareaopen(redClosed, 35);

    % display binary image
    figure;
    imshow(redObjects);
    title(sprintf('Binary Image %d', i));
    
    % properties of labeled regions
    properties = regionprops(bwlabel(redObjects), 'Centroid', 'BoundingBox');
    numRedObjects = numel(properties);
    
    % display original image
    figure;
    imshow(RGB);
    title(sprintf('Image %d', i));
    hold on;
    
    % loop through red objects to display centroids and bounding boxes
    for k = 1:numRedObjects
        centroid = properties(k).Centroid;
        boundingBox = properties(k).BoundingBox;
        
        % mark centroid (x,y,+)
        plot(centroid(1), centroid(2), 'b+');
        
        % draw bounding box
        rectangle('Position', boundingBox, 'EdgeColor', 'b', 'LineWidth', 2);
    end
    
    zoom on;

    % print the number of red objects
    fprintf('\nDetected %d red objects.\n', numRedObjects);
    
end