import matplotlib.pyplot as plt 
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-bright') 
fig, ax = plt.subplots() 
ax.scatter(x_values, y_values, c="red", s=200)

# Set chart title and label axes. 
ax.set_title("Square Numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of Value", fontsize=14) 
# Set size of tick labels. 
ax.tick_params(labelsize=14)
plt.show()