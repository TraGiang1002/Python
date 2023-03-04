import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.plot()
plt.show()
print(plt.style.available)
plt.style.use('dark_background')
x = [1, 2, 3, 4]
y = [10, 8, 6, 9]
plt.plot(x, y, color="red")
plt.show()

#Pyplot API
x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x), color="blue", linestyle="dashed", label="sin(x)")
plt.plot(x, np.cos(x), color="red", label="cos(x)")
plt.title("Sin(x) and Cos(x)")
plt.xlabel("Bien X")
plt.ylabel("F(x)")
# plt.xlim([0, 4])
# plt.ylim([-0.7, 0.6])
# plt.axis([0, 4, -0.7, 0.6])
# plt.axis("tight")
plt.axis("equal")
plt.legend()
plt.show()

#OO API
x = [1, 2, 3, 4]
y = [11, 22, 33, 44]
fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(x, y)
ax.set(title="A simple plot", xlabel="x-axis", ylabel="y-axis")
plt.show()

x = np.linspace(0, 10, 1000)
x[:5]
fig, ax = plt.subplots()
ax.plot(x, x**3)
plt.show()

plt.scatter(x, np.exp(x));
plt.show()

rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000*rng.rand(100)
fig, ax = plt.subplots()
img1 = ax.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.8)
fig.colorbar(img1)
plt.show()

soft_drink_prices = {"Coke": 10, "Pessi": 12, "Sprite": 8}
fig, ax = plt.subplots()
ax.bar(soft_drink_prices.keys(), soft_drink_prices.values())
ax.set(title="Bach Hoa Xanh's Soft Drink Prices", ylabel="Price ($)")
plt.show()
fig, ax = plt.subplots()
ax.barh(list(soft_drink_prices.keys()), list(soft_drink_prices.values()))
ax.set(title="Bach Hoa Xanh's Soft Drink Prices", xlabel="Price ($)")
plt.show()

np.random.seed(42)
student_height = np.random.normal(170, 10, 250)
plt.hist(student_height, bins=30)
plt.show()

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))
ax1.plot(x, x/2)
ax1.plot(x, x*2)
ax2.scatter(np.random.random(10), np.random.random(10))
ax3.bar(soft_drink_prices.keys(), soft_drink_prices.values())
ax4.hist(student_height, bins=30)
plt.show()

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))
ax[0,0].plot(x, x/2)
ax[0,0].plot(x, x*2)
ax[0,1].scatter(np.random.random(10), np.random.random(10))
ax[1,0].bar(soft_drink_prices.keys(), soft_drink_prices.values())
ax[1,1].hist(student_height, bins=30)
plt.show()

df = pd.read_csv('california_cities.csv')
df.head()
lat, lon = df['latd'], df['longd']
population, area = df['population_total'], df['area_total_km2']
plt.figure(figsize=(8,6))
plt.scatter(lon, lat, c=np.log10(population), linewidths=0, s=area, alpha=0.8)
plt.axis('equal')
plt.xlabel('longlatitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)
area_range = [50, 100, 300, 500]
for area in area_range:
    plt.scatter([], [], s=area, alpha=0.8, label=str(area) + 'km$^2$')
plt.legend(scatterpoints=1, labelspacing=1)
plt.show()