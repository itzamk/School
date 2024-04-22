%{
Andrew Kozempel
CMPSC 497
Fall 2023
LAB #2: Line Detection using Computer Vision
%}

%
% PART 1
%

fprintf('\nPart 1\n');

% load images
images = {'center.bmp', 'left.bmp', 'right.bmp'};

% loop through images
for i = 1:length(images)

    % load original image
    RGB = imread(images{i});
    figure, imshow(RGB);

    % convert to grayscale
    gray = rgb2gray(RGB);

    % get rid of "salt and pepper"
    filtered = medfilt2(gray, [15 15]);

    % create binary image
    bw = ~im2bw(filtered, 100/255);
    figure, imshow(bw);

    % set regions: left (40%), center (20%), right (40%)
    [rows, cols] = size(bw);
    left_region = bw(:, 1:floor(2*cols/5));
    center_region = bw(:, floor(2*cols/5)+1:floor(3*cols/5));
    right_region = bw(:, floor(3*cols/5)+1:end);
    
    % calculate sum of regions
    left_sum = sum(left_region(:));
    center_sum = sum(center_region(:));
    right_sum = sum(right_region(:));

    % print totals
    fprintf('\nLeft Sum: %d, Center Sum: %d, Right Sum: %d\n', left_sum, center_sum, right_sum);

    % determine which region the line is in and give command
    if center_sum > left_sum && center_sum > right_sum
        direction = 'Go Straight';
    elseif left_sum > center_sum && left_sum > right_sum
        direction = 'Turn Left';
    else
        direction = 'Turn Right';
    end

    % print direction
    fprintf('%s: %s\n', images{i}, direction);
end


%
% PART 2
%

fprintf('\nPart 2\n');

new_images = {'farleft.jpg', 'slightleft.jpg', 'center.jpg', 'slightright.jpg', 'farright.jpg', };

% loop through images
for i = 1:length(new_images)

    % load original image
    RGB = imread(new_images{i});
    figure, imshow(RGB);

    % convert to grayscale
    gray = rgb2gray(RGB);

    % get rid of "salt and pepper"
    filtered = medfilt2(gray, [15 15]);

    % create binary image ( less than 90 = 0(black))
    bw = ~im2bw(filtered, 90/255);
    figure, imshow(bw);

    % set regions: 20% each
    [rows, cols] = size(bw);
    farleft_region = bw(:, 1:floor(cols/5));
    slightleft_region = bw(:, floor(cols/5)+1:floor(2*cols/5));
    center_region = bw(:, floor(2*cols/5)+1:floor(3*cols/5));
    slightright_region = bw(:, floor(3*cols/5)+1:floor(4*cols/5));
    farright_region = bw(:, floor(4*cols/5)+1:end);
    
    % calculate sum of regions
    farleft_sum = sum(farleft_region(:));
    slightleft_sum = sum(slightleft_region(:));
    center_sum = sum(center_region(:));
    slightright_sum = sum(slightright_region(:));
    farright_sum = sum(farright_region(:));

    % print totals
    fprintf(['\nFar Left Sum: %d, Slight Left Sum: %d, Center Sum: %d, ' ...
        'Slight Right Sum: %d, Far Right Sum: %d\n'], farleft_sum, ...
        slightleft_sum, center_sum, slightright_sum, farright_sum);

    % find which is greatest
    sums = [farleft_sum, slightleft_sum, center_sum, slightright_sum, farright_sum];
    max_sum = max(sums);

    % give direction
    if max_sum ==  farleft_sum
        direction = 'Turn Hard Left';
    elseif max_sum == slightleft_sum
        direction = 'Turn Slight Left';
    elseif max_sum == center_sum
        direction = 'Go Straight';
    elseif max_sum == slightright_sum
        direction = 'Turn Slight Right';
    elseif max_sum == farright_sum
        direction = 'Turn Hard Right';
    end

    % print direction
    fprintf('%s: %s\n', new_images{i}, direction);
end