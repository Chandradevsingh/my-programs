# import matplotlib

# print(matplotlib.__version__)

import matplotlib.pyplot as plt

import numpy as np

#Example
#Draw a line in a diagram from position (0,0) to position (6,250):

# xpoints = np.array([0, 6])

# ypoints = np.array([0, 250])

# xpoints = np.array([1, 8])

# ypoints = np.array([3, 10])

#Example
#Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

# xpoints = np.array([1, 2, 6, 8])

# ypoints = np.array([3, 8, 1, 10])

#plt.plot(xpoints, ypoints, 'o--r', ms = 20, mec = 'c')

# plt.plot(xpoints, ypoints, 'o--r', ms = 20, mfc = 'c')

# plt.plot(xpoints, ypoints, 'o--r', ms = 20, mec = 'c', mfc = 'c')

# plt.plot(xpoints, ypoints, 'o--r', ms = 20, mec = '#4CAF50', mfc = '#4CAF50', linestyle= 'dotted', color = 'r', linewidth = '20.5')

#Example

# x1 = np.array([3, 5, 7, 2])
# x2 = np.array([3, 2, 5, 6])
# y1 = np.array([2, 6, 7, 1])
# y2 = np.array([5, 2, 5, 8])

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
# font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

# plt.plot(y1)
# plt.plot(y2)
# plt.plot(x, y)

# plt.title("Sports Watch Data", fontdict = font1, loc = 'left')

# plt.title("Sports Watch Data", fontdict = font1)

# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)

# plt.grid(axis = 'y', color = 'green', linestyle = 'dashdot', linewidth = '10.5')

# plt.show()

#plot 1:

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 1)

# plt.plot(x, y)

# plt.title("SALES")

# #plot 2:

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30 , 40])

# plt.subplot(2, 3, 2)

# plt.plot(x, y)

# plt.title("INCOME")

# plt.suptitle("MY SHOP")

# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# colors = np.array(["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan", "magenta"])

# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])


# plt.scatter(x, y, c = colors, s = sizes, alpha = 0.5, cmap='viridis')

# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

# plt.scatter(x, y, color = '#88c999')

# plt.colorbar()

# plt.show()

# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))
# sizes = 10 * np.random.randint(100, size=(100))

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

# plt.colorbar()

# plt.show()

# x = np.array(['A', 'B', 'C', 'D'])

# y = np.array([3, 8, 1, 10])

# # plt.bar(x, y, color = 'red', width = 0.1)

# plt.barh(x, y, color = 'red', height = 0.1)

# x = np.random.normal(170, 10, 250)

y = np.array([35, 25, 25, 15])

# plt.hist(x)

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

myexplode = [0.2, 0, 0, 0]

mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, startangle = 90, explode = myexplode, shadow = True, colors = mycolors)

plt.legend(title = "Four Fruits :")

plt.show()

