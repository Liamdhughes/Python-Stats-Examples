import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV data
data = pd.read_csv('KNEE_X_TRAIL.csv', header=None).to_numpy()

# Trim the data to include only the first 101 columns
data = data[:, :101]

# Extract the relevant portions of the data
conditionA = data[0:7, :]
conditionB = data[7:14, :]
conditionC = data[14:21, :]
conditionD = data[21:28, :]

# Calculate the average across participants for each condition
avgConditionA = np.mean(conditionA, axis=0)
avgConditionB = np.mean(conditionB, axis=0)
avgConditionC = np.mean(conditionC, axis=0)
avgConditionD = np.mean(conditionD, axis=0)

# Create the time series for 101 data points
timeSeries = np.arange(1, 102)

# Create the line plot with shades of gray and dashed lines for MPK conditions
plt.plot(timeSeries, avgConditionA, color=[0.2, 0.2, 0.2], linewidth=1.5, label='Mech + Hyd')
plt.plot(timeSeries, avgConditionB, color=[0.4, 0.4, 0.4], linewidth=1.5, label='Mech + Rig')
plt.plot(timeSeries, avgConditionC, '--', color=[0.6, 0.6, 0.6], linewidth=1.5, label='MPK + Hyd')
plt.plot(timeSeries, avgConditionD, '--', color=[0.8, 0.8, 0.8], linewidth=1.5, label='MPK + Rig')

# Set the plot title and axis labels
plt.title('Mean Trail Knee Flexion')
plt.xlabel('% of step cycle')
plt.ylabel('Distance')

# Add a legend
plt.legend()

# Display the plot
plt.show()
