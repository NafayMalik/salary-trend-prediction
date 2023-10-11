import matplotlib.pyplot as plt
import pandas as pd
from db import db_data, conn, cursor_obj

df = pd.DataFrame(db_data)


df.plot(kind='line', x = 0, y = 8) #plot b/w work_year and inflation_rate
df.plot(kind='line', x = 4, y = 8) #plot b/w salary and inflation_rate
df.plot(kind='line', x = 0, y = 9) #plot b/w work_year and gdp

df.plot(kind='line', x = 0, y = 4) #plot b/w work_year and salary
df.plot(kind='line', x = 4, y = 9) #plot b/w salary and gdp

plt.show()


cor_1 = df[4].corr(df[8]) #correlation b/w salary and inflation rate

cor_2 = df[4].corr(df[9]) #correlation b/w salary and gdp

cor_3 = df[8].corr(df[9]) #correlation b/w iflation and gdp

print(cor_1)
print(cor_2)
print(cor_3)