import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({"Week 1":[5000,5900,6500,3500,4000,5300,7900], "Week 2":[4000,3000,5000,5500,3000,4300,5900], "Week 3":[4000,5800,3500,2500,3000,5300,6000], "Day":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]})
df.plot(x='Day', marker='*', markersize=10,linestyle='--', linewidth=3, color=['r','b','brown'])
plt.title("Mela Sales Report")
plt.xlabel("Days")
plt.ylabel("Sales in Rs.")
plt.legend()
plt.show()