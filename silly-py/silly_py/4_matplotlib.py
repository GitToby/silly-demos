import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/pollen_week.csv')
df = df.drop(['day', 'hours', 'hour of day', 'work hour'], axis=1)
df = df.cumsum()

# with plt.xkcd():
plt.figure()
df.plot()
plt.legend(loc='best')
plt.xlabel('Hours into week')
plt.tick_params(labelleft=False)
plt.show()
