import matplotlib.pyplot as plt

input_values = range(1,11)
squares = [x*x for x in range(1,11)]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Задати назву для графіка та кожної з осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Задати розмір шрифту для підписів на розмітці.
ax.tick_params(axis='both', labelsize=14)

plt.show()