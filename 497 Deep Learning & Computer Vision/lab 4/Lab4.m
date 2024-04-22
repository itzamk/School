%{
Andrew Kozempel
CMPSC 497
Fall 2023
LAB #4: Color Tracking with Webcam
%}

cam = webcam;

% define figure for later
figure;

for i = 1:10000

    % get image from video
    RGB = snapshot(cam);
    fprintf('\nSize: %d x %d', size(RGB, 1), size(RGB, 2));
    
    % split into R, G, B planes
    r = RGB(:, :, 1);
    g = RGB(:, :, 2);
    b = RGB(:, :, 3);
    
    % create binary mask for red objects
    redMask = (r > 2*g) & (r > 2*b) & (r > 30);
    
    % apply closing
    se = strel('disk', 35);
    redClosed = imclose(redMask, se);
    
    % remove small objects
    redObjects = bwareaopen(redClosed, 35);
    
    % properties of labeled regions
    properties = regionprops(bwlabel(redObjects), 'Centroid', 'BoundingBox', 'Area');
    
    % if red objects were detected
    if ~isempty(properties)

        % find the largest red object
        [~, largest] = max([properties.Area]);
        centroid = properties(largest).Centroid;
        boundingBox = properties(largest).BoundingBox;

        % display original image
        imshow(RGB);
        title(sprintf('Frame %d', i));
        hold on;
        
        % mark centroid and draw bounding box
        plot(centroid(1), centroid(2), 'b+');
        rectangle('Position', boundingBox, 'EdgeColor', 'b', 'LineWidth', 2);
    
    else
        imshow(RGB);
        title(sprintf('Frame %d - No Red Object Detected', i));

    end

    drawnow; % Update the figure window
end