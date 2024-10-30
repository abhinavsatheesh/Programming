import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({"Week 1":[5000,5900,6500,3500,4000,5300,7900], "Week 2":[4000,3000,5000,5500,3000,4300,5900], "Week 3":[4000,5800,3500,2500,3000,5300,6000], "Day":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]})
df.plot(kind='barh', x='Day', color=['r','y','purple'], edgecolor='g', linestyle='--')
plt.title("Mela Sales Report")
plt.xlabel("Sales in Rs.")
plt.ylabel("Days")
plt.legend(['W1', 'W2', "W3"])
plt.show()