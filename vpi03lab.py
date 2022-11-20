import numpy as np
from io import StringIO
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

file0 = open('input_10_03lab.txt').read().replace(',',' ')
file = np.loadtxt(StringIO(file0), dtype=int, skiprows=1)

file01 = file[..., 1]
file01Vector = file01.reshape(-1, 1)
file02 = file[..., 2]
file02Vector = file02.reshape(-1, 1)
file00 = file[..., 0]

timeColumn = file01Vector*60 + file02Vector
spentSum = file00.reshape(-1, 1)

nf = open('new_file_3.txt', 'w')

#=====

regr = linear_model.LinearRegression()
regr.fit(timeColumn, spentSum)
predSpentSum = regr.predict(timeColumn)

avTimeColumn = np.sum(timeColumn)/len(timeColumn)
avSpentSum = np.sum(spentSum)/len(spentSum)

centerOfMass = np.column_stack((round(avTimeColumn, 2), round(avSpentSum, 2)))
nf.write(f'Center of mass = {centerOfMass}')

#=====

cov = 1/len(timeColumn) * np.absolute(np.sum(timeColumn*spentSum - avTimeColumn*avSpentSum))
var = 1/len(timeColumn) * np.sum(np.square(timeColumn) - np.square(avTimeColumn))
nf.write(f'\n\nCov = {cov}')

m = cov/var
k = avSpentSum - m*avTimeColumn

nf.write(f'\n\nRegression line equation:\ny = {k} + {m}*x')
nf.write('\nM = '+str(m)+'\nK = '+str(k))

#=====

sx = np.sqrt(1/len(timeColumn) * np.sum(np.square(timeColumn - avTimeColumn)))
sy = np.sqrt(1/len(spentSum) * np.sum(np.square(spentSum - avSpentSum)))

r = 1/(len(timeColumn) - 1) * np.sum(((timeColumn - avTimeColumn)/sx)*((spentSum - avSpentSum)/sy))
nf.write(f'\n\nCorrelation = {r}')

#=====

xRL = np.linspace(1, (np.max(timeColumn)+50), 200)
y = k+m*xRL

#=====

plt.plot(xRL, y, label='regression line', linewidth=2, color='pink')
plt.scatter(timeColumn, spentSum, label='scatter plot', color='blue')
plt.plot(timeColumn, predSpentSum, color='orange', linewidth=3, label='trend line')
plt.plot(avTimeColumn, avSpentSum, markersize=20, color='red', marker='+', label='center of mass')
plt.xlabel('Time, seconds')
plt.ylabel('Spending amount')
plt.legend(loc='upper left')
#plt.show()

print()