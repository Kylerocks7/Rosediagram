import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mplstereonet


data_files = ['Region1.csv', 'Region2.csv']

style = [
    {'color': 'tab:blue', 'alpha': 0.5, 'label': 'Region 1'},
    {'color': 'tab:red', 'alpha': 0.5, 'label': 'Region2'} 
]

Orientations = []
for filename in data_files:
    df = pd.read_csv(filename)
    Orientations.append(df['Orientation'].values)

dip = 0

bin_edges = np.arange(-5, 366, 10) # Calculates the directions (or strikes) every 10*


fig = plt.figure(figsize=(20,9))
ax = fig.add_subplot(projection='polar')

for Orientation, style in zip(Orientations, style):
    number_of_orientations, _ = np.histogram(Orientation, bin_edges) # Converts the orientations into bins
    number_of_orientations = number_of_orientations / number_of_orientations.sum() # Normalize by total count
    number_of_orientations[0] += number_of_orientations[-1] # Sums the first value with the last


    # This part is done in order to get the "mirrored". This sums the first half with the second half.
    half = np.sum(np.split(number_of_orientations[:-1], 2), 0)
    two_halves = np.concatenate([half, half])
   
    # Plot the normalized data
    theta = np.arange(0, 360, 360/len(two_halves))
    ax.bar(np.radians(theta), two_halves, width=np.radians(360/len(two_halves)), **style, edgecolor='black', linewidth=2)

ax.legend(['Region 1', 'Region 2'], loc='upper right', fontsize=9)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_thetagrids(np.arange(0, 360, 10), labels=np.arange(0, 360, 10))
ax.set_title('Rose Diagram', y=1.10, fontsize=15)
ax.set_yticklabels([])

plt.savefig('fig.png', bbox_inches='tight')
plt.show()
