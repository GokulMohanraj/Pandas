import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('team_details.csv')

df.plot()

plt.show()

# using scatter plot 

df.plot(kind = 'scatter', x = 'Team Name', y ='Points')

plt.show()

# using Histogram "kind = 'hist"

df.plot(kind = 'hist')

plt.show()
