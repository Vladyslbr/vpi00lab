import numpy as np
from numpy import *
import pandas as pd


# Text file data converted to integer data type
File_data = np.loadtxt("input_100.txt", dtype=int)
File_data = File_data[1:]
File_data = np.sort(File_data)  # sorting values
lenght = len(File_data)

unique_values = np.unique(File_data)

# creating indices and occurrence_count array
unique_values, indices_list = np.unique(File_data, return_index=True)  # create index
unique_values, occurrence_count = np.unique(File_data, return_counts=True)  # count frequency

# cumulative frequency array
cumulative_frequency = np.cumsum(occurrence_count)

# sum of frequency and cumulative frequency
occurrence_count_sum = np.sum(occurrence_count)
cumulative_frequency_sum = np.sum(cumulative_frequency)

nf = open('new_file.txt', 'w')

# recording a table to a file
pd.set_option('display.max_rows', 1000)
df1 = pd.DataFrame({'value':unique_values, 'freq':occurrence_count, 'cumFreq':cumulative_frequency})
nf.write(str(df1))
nf.write('\n\n\nTotal of frequency = '+str(occurrence_count_sum))
nf.write('\nTotal of cumulative frequency = '+str(cumulative_frequency_sum))

# the value of most frequent value(s)
max_value = occurrence_count.max()
min_value = occurrence_count.min()

val_equalsto_max_value = np.nonzero(occurrence_count == max_value)
most_freq_value = unique_values[val_equalsto_max_value]
nf.write('\n\nMost frequent movie(s) = '+str(most_freq_value)+' counts: '+str(max_value))

# finding Me
if (lenght % 2) == 1:
    nf.write('\n\nMe(odd) = '+str(File_data[int(lenght/2)]))
else:
    nf.write('\n\nMe(even) = '+str(np.median(File_data)))
    #((File_data[int(lenght/2)]+File_data[int(lenght/2+1)])/2)
    #np.median(File_data)

# finding Mo
if (max_value == min_value): # Mo if no values occurrence
    nf.write('\nMo = no value')
else:
    nf.write('\nMo = '+str(max_value))

# finding the Range
nf.write('\n\nRange = '+str(max_value - min_value))

cumulative_frequency, cum_indices = np.unique(cumulative_frequency, return_index=True)

# finding Quartiles' values
q1 = 1/4 * (lenght + 1)
nf.write('\n\nQ1 = '+str(q1))
q1 = int(q1)

#index = indices_list[q1]
#q1_value = np.nonzero(occurrence_count == q1)
q11 = cum_indices[q1]
q12 = cumulative_frequency[q11 - 1]
q13 = cumulative_frequency[q11]
q14 = q12 + 1/4 * (q13 - q12)
nf.write('\nQ1 value = '+str(q14))

q2 = 1/2 * (lenght + 1)
nf.write('\nQ2 = '+str(q2))
q2 = int(q2)
q21 = cum_indices[q2]
q22 = cumulative_frequency[q21 - 1]
q23 = cumulative_frequency[q21]
q24 = q22 + 1/4 * (q23 - q22)
nf.write('\nQ2 value = '+str(q24))

q3 = 3/4 * (lenght + 1)
nf.write('\nQ3 = '+str(q3))
q3 = int(q3)
q31 = cum_indices[q3]
q32 = cumulative_frequency[q31 - 1]
q33 = cumulative_frequency[q31]
q34 = q32 + 1/4 * (q33 - q32)
nf.write('\nQ3 value = '+str(q34))

# finding the inter-quartile range
iqr = q34 - q14
nf.write('\n\nIQR = '+str(iqr))

# finding the mean absolute deviation
x_mean = np.sum(cumulative_frequency) / len(cumulative_frequency)
mad = np.sum(np.absolute(cumulative_frequency - x_mean))/lenght
mad = round(mad, 4)
nf.write('\n\nMAD = '+str(mad))

# finding the mean square error
mse = 1/len(cumulative_frequency) * np.sum(np.square(cumulative_frequency - x_mean))
mse = round(mse, 4)
nf.write('\n\nMSE = '+str(mse))


