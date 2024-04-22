function I = readFunctionTrain(filename)

% Resize the images to the size required by the Alexnet network.
I = imread(filename);
I = imresize(I, [227 227]);