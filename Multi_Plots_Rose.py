import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mplstereonet

fig = plt.figure(figsize = (30,30)) # Creates a Figure

# Add as many plots as neccesary (row, how many columns, column #)
ax = fig.add_subplot(2,5,1, projection = 'polar'), fig.add_subplot(2,5,2, projection = 'polar'), fig.add_subplot(2,5,3, projection = 'polar'), fig.add_subplot(2,5,4, projection = 'polar'), fig.add_subplot(2,5,5, projection = 'polar'), fig.add_subplot(1,5,1, projection = 'polar'), fig.add_subplot(1,5,2, projection = 'polar'), fig.add_subplot(1,5,3, projection = 'polar'), fig.add_subplot(1,5,4, projection = 'polar'), fig.add_subplot(1,5,5, projection = 'polar')

#Add how many 
data_files = ['Region1.csv', 'Region2.csv', 'Region3.csv', 'Region4.csv', 'Region5.csv', 'Region6.csv', 'Region7.csv', 'Region8.csv', 'Region9.csv', 'Region10.csv']

# Loop to plot all of the data
 # For loop that takes the axes from the filenames (axes from data_files data)
for ax, filename in zip(ax, data_files):
  df = pd.read_csv(filename)  # Reads the csv 
  data =  df['Orientation'].values # Takes the values from specifically the Orientation column

  # Choose the specific column
  Orientation = np.concatenate([np.expand_dims(i,axis=0) for i in [data]]) # Take the data (this is "strike")
  dip = 0 # We don't have dips, only strike direction 

  bin_edges = np.arange(-5, 366, 10) # Calculates the directions (or strikes) every 10*
  number_of_orientations, bin_edges = np.histogram(Orientation, bin_edges) # Converts the orientations into bins
  number_of_orientations[0] += number_of_orientations[-1] # Sums the first value with the last

  # This part is done in order to get the "mirrored" aspect.This sums the first half with the second half.
  half = np.sum(np.split(number_of_orientations[:-1], 2), 0)
  two_halves = np.concatenate([half, half])
  ax.bar(np.deg2rad(np.arange(0, 360, 10)), two_halves, 
       width=np.deg2rad(10), bottom=0.0, color='black', edgecolor='grey')
  
  ax.set_theta_zero_location('N') # Makes 0 be North

  ax.set_theta_direction(-1) # Makes the plot go counter clockwise


# Modify each plot individually
  if filename == "Region1.csv":
    ax.set_title('Region 1', y=1.10, fontsize=15)

  elif filename == "Region2.csv":
    ax.set_title('Region 2', y=1.10, fontsize=15)

  elif filename == "Region3.csv":
    ax.set_title('Region 3', y=1.10, fontsize=15)

  elif filename == "Region4.csv":
    ax.set_title('Region 4', y=1.10, fontsize=15)

  elif filename == "Region5.csv":
    ax.set_title('Region 5', y=1.10, fontsize=15)

  elif filename == "Region6.csv":
    ax.set_title('Region 6', y=1.10, fontsize=15)

  elif filename == "Region7.csv":
    ax.set_title('Region 7', y=1.10, fontsize=15)

  elif filename == "Region8.csv":
    ax.set_title('Region 8', y=1.10, fontsize=15)
  
  elif filename == "Region9.csv":
    ax.set_title('Region 9', y=1.10, fontsize=15)

  elif filename == "Region10.csv":
    ax.set_title('Region 10', y=1.10, fontsize=15)


  ax.set_thetagrids(np.arange(0, 360, 10), labels=np.arange(0, 360, 10)) # Modify the grid as neccesary
  ax.set_yticklabels([]) # Remove the radial labels

# Below is the plotting of the rose diagram.
plt.savefig('fig.png',bbox_inches='tight')

