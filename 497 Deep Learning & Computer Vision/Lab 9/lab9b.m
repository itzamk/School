%{
Andrew Kozempel
CMPSC 497
Fall 2023
LAB #9b: Cookie/Cracker Defect Detection System using Deep Learning
%}


camera = webcam; % Connect to the camera
load myNet.mat; % Load the neural net

% nnet = alexnet;  (Original)

while true
    picture = camera.snapshot; % Take a picture
    picture = imresize(picture,[227,227]); % Resize
    label = classify(myNet, picture); % Classify the picture

    % label = classify(nnet, picture);  (Original)
    
    image(picture); % Show the picture
    title(char(label)); % Show the label
    drawnow;
end