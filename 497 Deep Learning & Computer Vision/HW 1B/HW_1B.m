%{
Andrew Kozempel
CMPSC 497
Fall 2023
HW #1A Intro to MATLAB Statistics: Part 1
%}

% PART 1 - peppers.png

% 1 - read/display
im = imread('peppers.png');
imshow(im);

% 2 - dimensions
fprintf(['peppers.png Dimensions:\n\tRows: %d\n\tColumns %d' ...
    '\n\tPlanes: %d\n'], size(im));

% 3 - pixel regions
imtool(im);

% 4 - red plane
red = im(:, :, 1);
figure;
imshow(red);
title('Red Plane');

% 5 - blue plane
blue = im(:, :, 2);
figure;
imshow(blue);
title('Blue Plane');

% 6 - green plane
green = im(:, :, 3);
figure;
imshow(green);
title('Green Plane');

% 7 - grayscale
gray = rgb2gray(im);
[gray_rows, gray_cols] = size(gray);
figure;
imshow(gray);
title('Grayscale');

% 7 - questions
fprintf('\nGrayscale Pixel Range:\n\t%d to %d\n', min(min(gray)), max(max(gray)));
fprintf('Grayscale Dimensions:\n\t%d Rows x %d Columns\n', size(gray));

% 8 - min, max, mean pixel vals
minimum = min(min(gray));
maximum = max(max(gray));
average = mean(mean(gray));
fprintf(['Grayscale Image Stats:\n\tMinimum: %d\n\tMaximum: %2f' ...
    '\n\tMean: %d'], minimum, maximum, average);

% 9 - Histogram
figure;
imhist(gray);
title('Grayscale Histogram');
xlabel('Pixel Intensity');
ylabel('Frequency');

% 10 - top half
figure;
gray_top_half = gray(1:gray_rows/2, :);
imshow(gray_top_half);
title('Top Half of Grayscale');

% 11 - right half
figure;
gray_right_half = gray(:, gray_cols/2+1:gray_cols);
imshow(gray_right_half);
title('Right Half of Grayscale');

% 12 - binary
gray_bin = imbinarize(gray);
figure;
imshow(gray_bin);
title('Binary Grayscale');
fprintf('\n\nBinary Grayscale Pixel Range:\n\t%d to %d\n', ...
    min(min(gray_bin)), max(max(gray_bin)));

% 13 - reduce OG im by .50
im_reduced = imresize(im, 0.5);
figure;
imshow(im_reduced);
title('Reduced Original Image (50% Reduced)');

% 14 - resize 200x200
im_resized = imresize(im, [200,200]);
figure;
imshow(im_resized);
title('Resized Original Image (200x200)');

% print original, reduced, resized dimensions to compare
fprintf(['\nOriginal Image Dimensions:\n\t%d Rows x %d Columns ' ...
    'x %d Planes\n'], size(im));
fprintf(['Reduced Image Dimensions:\n\t%d Rows x %d Columns ' ...
    'x %d Planes\n'], size(im_reduced));
fprintf(['Resized Image Dimensions:\n\t%d Rows x %d Columns ' ...
    'x %d Planes\n'], size(im_resized));

% PART 2 - my_image.png

% 1 - read/display
im2 = imread('my_image.png');
imshow(im2);

% 2 - dimensions
fprintf(['my_image.png Dimensions:\n\tRows: %d\n\tColumns %d' ...
    '\n\tPlanes: %d\n'], size(im2));

% 3 - pixel regions
imtool(im2);

% 4 - red plane
red2 = im2(:, :, 1);
figure;
imshow(red2);
title('Red Plane 2');

% 5 - blue plane
blue2 = im2(:, :, 2);
figure;
imshow(blue2);
title('Blue Plane 2');

% 6 - green plane
green2 = im2(:, :, 3);
figure;
imshow(green2);
title('Green Plane 2');

% 7 - grayscale
gray2 = rgb2gray(im2);
[gray_rows2, gray_cols2] = size(gray2);
figure;
imshow(gray2);
title('Grayscale 2');

% 7 - questions
fprintf('\nGrayscale 2 Pixel Range:\n\t%d to %d\n', min(min(gray2)), max(max(gray2)));
fprintf('Grayscale 2 Dimensions:\n\t%d Rows x %d Columns\n', size(gray2));

% 8 - min, max, mean pixel vals
minimum2 = min(min(gray2));
maximum2 = max(max(gray2));
average2 = mean(mean(gray2));
fprintf(['Grayscale 2 Image Stats:\n\tMinimum: %d\n\tMaximum: %2f' ...
    '\n\tMean: %d'], minimum2, maximum2, average2);

% 9 - Histogram
figure;
imhist(gray2);
title('Grayscale 2 Histogram');
xlabel('Pixel Intensity');
ylabel('Frequency');

% 10 - top half
figure;
gray_top_half2 = gray2(1:gray_rows2/2, :);
imshow(gray_top_half2);
title('Top Half of Grayscale 2');

% 11 - right half
figure;
gray_right_half2 = gray2(:, gray_cols2/2+1:gray_cols2);
imshow(gray_right_half2);
title('Right Half of Grayscale 2');

% 12 - binary
gray_bin2 = imbinarize(gray2);
figure;
imshow(gray_bin2);
title('Binary Grayscale 2');
fprintf('\n\nBinary Grayscale 2 Pixel Range:\n\t%d to %d\n', ...
    min(min(gray_bin2)), max(max(gray_bin2)));

% 13 - reduce OG im by .50
im_reduced2 = imresize(im2, 0.5);
figure;
imshow(im_reduced2);
title('Reduced Original Image 2 (50% Reduced)');

% 14 - resize 200x200
im_resized2 = imresize(im2, [200,200]);
figure;
imshow(im_resized2);
title('Resized Original Image 2 (200x200)');

% print original, reduced, resized dimensions to compare
fprintf(['\nOriginal Image 2 Dimensions:\n\t%d Rows x %d Columns ' ...
    'x %d Planes\n'], size(im2));
fprintf(['Reduced Image 2 Dimensions:\n\t%d Rows x %d Columns ' ...
    'x %d Planes\n'], size(im_reduced2));
fprintf(['Resized Image 2 Dimensions:\n\t%d Rows x %d Columns ' ...
    'x %d Planes\n'], size(im_resized2));