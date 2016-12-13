import math
vars = [38946,
43420,
49191,
50430,
50557,
52580,
53595,
54135,
60181,
62076]

sum = 0
for var in vars:
    sum += var

mean = sum / len(vars)
SS = 0
for var in vars:
    dev = (var - mean) ** 2
    SS += dev 
sq_avg = math.sqrt(SS/len(vars))


print "Sum: ", sum
print "Mean: ", mean
print "SS: ", SS 
print "sq_avg: ", sq_avg
