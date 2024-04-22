# Andrew Kozempel
# CMPSC 455
# Fall 2023
# In class Lab/Project

#############
# PART 1
#############
print('\n=====Part 1=====\n')

# part 1a
p1a = 1 + 10**-16 + 10**-16 + 10**-16 + 10**-16 + 10**-16 + 10**-16 + 10**-16 + 10**-16 + 10**-16 + 10**-16
print(f'a: {p1a}')

# part 1b
p1b = 10**-16 + 10**-16 + 10**-16 + 10**-16 + 10**-16 + 10**-16 + 10**-16 + 10**-16 + 10**-16 + 10**-16 + 1
print(f'b: {p1b}')

# part 1c
p1c = 1 + 10*10**-16
print(f'c: {p1c}')

# part 1d
p1d = 10*10**-16 + 1
print(f'd: {p1d}\n')

#############
# PART 2
#############
print('\n=====Part 2=====\n')

def part2p(x):

    return x**3 - 3*x**2 + 3*x -1

def part2q(x):

    return ((x-3)*x+3)*x-1

p2p272 = part2p(2.72)
p2q272 = part2q(2.72)

p2p975 = part2p(0.975)
p2q975 = part2q(0.975)

print(f'P(2.72): \n\tExact: {p2p272}\n\tRounded:{round(p2p272,2)}')
print(f'Q(2.72): \n\tExact: {p2q272}\n\tRounded:{round(p2q272,2)}  ')

print(f'P(0.975): \n\tExact: {p2p975}\n\tRounded:{round(p2p975,2)}')
print(f'Q(0.975): \n\tExact: {p2q975}\n\tRounded:{round(p2q975,2)}  ')


#############
# PART 3
#############
print('\n=====Part 3=====\n')

print(f'1+10^-15-1 = {1+10**-15-1}')


#############
# PART 4
#############
print('\n=====Part 4=====\n')

def derivative(h):

    return ((1+h)-1)/h

for i in range(20):
    
    h = 10**-(i+1)

    print(f'10^-{i+1} --> {derivative(h)}')