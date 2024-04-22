%{
Andrew Kozempel
CMPSC 497
Fall 2023
LAB #10: Deep Learning: Image Classification Study
%}

camera = webcam; % Connect to the camera
load new_Net_5.mat; % Load the neural net (5 epochs)

%nnet = alexnet;  %(Original)

while true
    picture = camera.snapshot; % Take a picture
    picture = imresize(picture,[227,227]); % Resize
    label = classify(new_Net_5, picture); % Classify the picture (5 epochs)

    %label = classify(nnet, picture);  %(Original)
    
    image(picture); % Show the picture
    title(char(label)); % Show the label
    drawnow;
end