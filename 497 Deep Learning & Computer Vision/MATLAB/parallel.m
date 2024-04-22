%{
Andrew Kozempel
CMPSC 497
Fall 2023
HW #1A Intro to MATLAB Statistics: Part 2 Parallel
%}

% ask for input and initialize Rtotal
num_res = input('Please enter the number of resistors: ');
Rtotal = 0;

for i = 1:num_res
    fprintf('%d. ', i);
    R = input('Please enter the resistance: ');
    Rtotal = Rtotal + 1/R;
end

fprintf('\nThe total resistance is %.2f\n', 1/Rtotal)
