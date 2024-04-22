%{
Andrew Kozempel
CMPSC 497
Fall 2023
HW #1A Intro to MATLAB Statistics: Part 1
%}

% list of voltages
voltages = [21.2, 19.5, 20.1, 18.3, 17.7, 15.0, 21.9, 24.7, 23.1, 20.2, 16.3, 22.8, 18.4, 23.5, 21.1];

% calculate min, max, average, SD, median, number of values above max
minimum = min(voltages);
maximum = max(voltages);
average = mean(voltages);
s_d = std(voltages);
med = median(voltages);
above_avg = find(voltages > average);
length_above_avg = length(above_avg);


% print results
fprintf('1. The minimum voltage is %.2f volts \n', minimum);
fprintf('2. The maximum voltage is %.2f volts \n', maximum);
fprintf('3. The average voltage is %.2f volts \n', average);
fprintf('4. The standard deviation is %.2f volts \n', s_d);
fprintf('6. The median voltage is %.2f volts \n', med);
fprintf('7. The number of values above the average is %.2f volts \n', length_above_avg);
fprintf('8. The values above the average: ')
for i = 1:length_above_avg
    fprintf('%.2f, ',voltages(above_avg(i)));
end


% plot of raw data
figure;
plot(voltages, 'o-');
title('Voltage Measurements');
xlabel('Measurement');
ylabel('Voltage');

% histogram
figure;
histogram(voltages);
title('Voltage Distribution');
xlabel('Voltage');
ylabel('Frequency');

fprintf('\n\n9. Plot open in new window');
fprintf('\n10. Histogram open in a new window');

% sorted data
sorted = sort(voltages);
fprintf('\n\n11. Sorted Data:\n');

for i = 1:length(sorted);
    fprintf('%.2f \n', sorted(i));
end