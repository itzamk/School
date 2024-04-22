%{
Andrew Kozempel
CMPSC 497
Fall 2023
HW #1A Intro to MATLAB Statistics: Part 2 Parallel
%}

% ask for input and initialize Rtotal
num_res = input('Please enter the number of resistors: ');
Rtotal = 0;

% ask for resistances
for i = 1:num_res
    fprintf('%d. ', i);
    R = input('Please enter the resistance (ohms): ');
    Rtotal = Rtotal + 1/R;
end

% print result
fprintf('\nThe total resistance is %.2f ohms.\n', 1/Rtotal);