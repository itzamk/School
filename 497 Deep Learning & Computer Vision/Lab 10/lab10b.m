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
layers(23) = fullyConnectedLayer(4); % changed to 4
layers(25) = classificationLayer

% Perform Transfer Learning (can be adjusted)
opts = trainingOptions('sgdm', 'InitialLearnRate', 0.001, ...
    'MaxEpochs', 5, 'MiniBatchSize', 16, ...
    'Plots', 'training-progress');

% Set custom read function
trainingImages.ReadFcn = @readFunctionTrain; % resize

% Train the Network (may take 5 to 15+ minutes)
% Create a new network built on Alexnet w new layers
new_Net_5 = trainNetwork(trainingImages, layers, opts);

% Test Network Performance on Test Images
testImages.ReadFcn = @readFunctionTrain; % resize
predictedLabels = classify(new_Net_5, testImages); % test
accuracy = mean(predictedLabels == testImages.Labels)

% Display the confusion chart
confusionchart(predictedLabels, testImages.Labels);

save new_Net_5.mat new_Net_5;