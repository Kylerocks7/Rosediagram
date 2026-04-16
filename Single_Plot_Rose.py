import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mplstereonet

#Add the csv file name here
df = pd.read_csv('Region1.csv')

# Choose the specific column
data = df['Orientation'].values
Orientation = np.concatenate([np.expand_dims(i,axis=0) for i in [data]])
dip = 0 #We don't have dips, only strike direction

print (df) # Prints the csv table, look over it!


bin_edges = np.arange(-5, 366, 10) # Calculates the directions (or strikes) every 10*
number_of_orientations, bin_edges = np.histogram(Orientation, bin_edges) # Converts the orientations into bins

number_of_orientations[0] += number_of_orientations[-1] # Sums the first value with the last

# This part is done in order to get the "mirrored" aspect.This sums the first half with the second half.
half = np.sum(np.split(number_of_orientations[:-1], 2), 0)
two_halves = np.concatenate([half, half])


# Below is the plotting of the rose diagram.

fig = plt.figure(figsize=(16,7)) # Here you can modify the size.

ax = fig.add_subplot(projection='polar') #This is the overall rose diagram, "polar" is the kind of plot we want.

# Below is the aesthetic part of the code, here I can modify its look.

ax.bar(np.deg2rad(np.arange(0, 360, 10)), two_halves, 
       width=np.deg2rad(10), bottom=0.0, color='black', edgecolor='grey')
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_thetagrids(np.arange(0, 360, 10), labels=np.arange(0, 360, 10))
ax.set_title('Region 1', y=1.10, fontsize=15)
ax.set_yticklabels([])


plt.savefig('fig.png',bbox_inches='tight')

