import matplotlib.pyplot as plt
x1 = [2, 4, 5, 7]
y2 = [0.002, 4, 7, 3]
plt.plot(x1, y2, marker='o', markerfacecolor='yellow', label= "Line 1")
x3 = [2, 4, 6, 8]
y4 = [1, 2, 7, 8]
plt.plot(x3, y4,marker='o', markerfacecolor='green', label= "Line 2")

plt.ylim(1,8)
plt.xlim(1,8)
plt.xlabel('X Axis')
plt.ylabel('Y axis')
plt.legend()
plt.title('Example Two line Graph')
plt.show()