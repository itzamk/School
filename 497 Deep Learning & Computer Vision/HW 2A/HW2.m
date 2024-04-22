%{
Andrew Kozempel
CMPSC 497
Fall 2023
HW2 imopen() and imclose()

amk97@psu.edu

%}

%---------
% imopen()
%---------

% load image
im = imread('connected.bmp');

% print size
fprintf('Size of connected.bmp (imopen() image): %d x %d\n', size(im,1), size(im,2));

% show image
figure;
imshow(im);
title('Original: Before imopen()');

% separate the circles using imopen()
se = strel('disk', 5);  
im_opened = imopen(im, se);

% show separate objects
figure;
imshow(im_opened);
title('New: After imopen()');

%----------
% imclose()
%----------

% load image
im2 = imread('separate.bmp');

% print size
fprintf('Size of separate.bmp (imclose() image): %d x %d\n', size(im2,1), size(im2,2));

% show image
figure;
imshow(im2);
title('Original: Before imclose()');

% separate the squares using imclose()
se2 = strel('square', 20);  
im_closed = imclose(im2, se2);

% show separate objects
figure;
imshow(im_closed);
title('New: After imclose()');