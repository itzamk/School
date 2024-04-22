%{
Andrew Kozempel
CMPSC 497
Fall 2023
LAB #9: Cookie/Cracker Defect Detection System using Deep Learning
%}

% load images (each class in separate folders within a parent folder)
allImages = imageDatastore('TrainingData', 'IncludeSubfolders', true,...
'LabelSource', 'foldernames');

% Split data into training (80%)and test (20%) sets
[trainingImages, testImages] = splitEachLabel(allImages, 0.8, 'randomize');

% Load Pre-trained Network (AlexNet)
alex = alexnet;

% Review Network Architecture
layers = alex.Layers

% Modify Pre-trained Network
layers(23) = fullyConnectedLayer(2); % changed to 2
layers(25) = classificationLayer

% Perform Transfer Learning (can be adjusted)
opts = trainingOptions('sgdm', 'InitialLearnRate', 0.001, ...
'MaxEpochs', 20, 'MiniBatchSize', 64);

% Set custom read function
trainingImages.ReadFcn = @readFunctionTrain; % resize

% Train the Network (may take 5 to 15+ minutes)
% Create a new network built on Alexnet w new layers
myNet = trainNetwork(trainingImages, layers, opts);

% Test Network Performance on Test Images
testImages.ReadFcn = @readFunctionTrain; % resize
predictedLabels = classify(myNet, testImages); % test
accuracy = mean(predictedLabels == testImages.Labels)

save myNet.mat myNet;