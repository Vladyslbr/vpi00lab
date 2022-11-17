import numpy as np

file = np.loadtxt("input_100.txt", dtype=int)
file = file[1:]
file = np.sort(file)
filesSize = file.size

fileVector = file.reshape(-1, 1)

w = np.arange(1, filesSize + 1, 1)
e = np.insert(fileVector, 0, w, axis=1)

r = e[..., 1] # working unit
i = e[..., 0]

unique_values = np.unique(r)
unique_values, occurence = np.unique(r, return_counts=True)

nf = open('new_file.txt', 'w')

nf.write('Occurence array:\n'+str(occurence))

#=====
nf.write('\n-------')

q1 = 1/4*(filesSize + 1)
q3 = 3/4*(filesSize + 1)
q1 = int(q1)
q3 = int(q3)

q1c1 = i==q1
q1c2 = i==(q1+1)
q1v1 = np.extract(q1c1, e[..., 1])
q1v2 = np.extract(q1c2, e[..., 1])

q1r = q1v1 + 0.25*(q1v2 - q1v1)
nf.write('\nQ1 = '+str(q1r))

q3c1 = i==q3
q3c2 = i==(q3+1)
q3v1 = np.extract(q3c1, e[..., 1])
q3v2 = np.extract(q3c2, e[..., 1])

q3r = q3v1 + 0.75*(q3v2 - q3v1)
nf.write('\nQ3 = '+str(q3r))

p90 = 90/100 * (filesSize + 1)
nf.write('\np90 = '+str(p90))

#=====
nf.write('\n-------')

xMean = np.sum(unique_values) / len(unique_values)
xMean = round(xMean, 4)
nf.write('\nX mean = '+str(xMean))

S = np.sqrt((np.sum(occurence * np.square(unique_values - xMean))) / (np.sum(occurence) - 1))
S = round(S, 4)
nf.write('\nSD = '+str(S))

MD = np.sum(occurence * np.absolute(unique_values - xMean))/np.sum(occurence)
MD = round(MD, 4)
nf.write('\nMD = '+str(MD))

#=====
nf.write('\n-------')

diffA = np.array([[xMean, 1], [100, 1]])
diffB = np.array([[95], [100]])
a, b = np.linalg.solve(diffA, diffB)

nf.write('\ny = '+str(a)+'*x + '+str(b))

eq = a * r + b
eq = eq.astype(int)
nf.write('\n\nNew values by an equation:\n'+str(eq))

#=====
nf.write('\n-------')

nf.write('\nStem-and-leaf:')

from collections import OrderedDict, Counter

def stemleaf(x):
    d = OrderedDict((((str(v)[:-1], ' ')[v < 10], Counter()) for v in sorted(x)))
    for s in ((str(v), ' '+str(v))[v < 10] for v in x):
        d[s[:-1]][s[-1]] += 1
    m = max(len(s) for s in d)
    for k in d:
        nf.write('\n%s%s | %s'%(' '*(m-len(k)), k, ' '.join(sorted(d[k].elements()))))

stemleaf(r)

nf.write('\nKey:\n 1 | 1 = 11')

#=====

import matplotlib.pyplot as plt

data = [r, eq]
fig, ax = plt.subplots()
ax.boxplot(data)
#plt.show()
