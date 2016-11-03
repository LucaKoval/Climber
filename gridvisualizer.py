"""
import matplotlib as mpl
import matplotlib.pyplot as pyplot
import numpy as np
from random import randint

x1, x2, x3, x4, x5, y1, y2, y3, y4, y5 = randint(0,500), randint(0,500), randint(0,500), randint(0,500), randint(0,500), randint(0,500), randint(0,500), randint(0,500), randint(0,500), randint(0,500)

# make values from -5 to 5, for this example
zvals = np.random.rand(500,500)*10-5

# make a color map of fixed colors
cmap = mpl.colors.ListedColormap(['black','green','white'])
bounds=[-6,-2,2,6]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

fig = pyplot.figure(2)

cmap2 = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',
                                           ['black','green','white'],
                                           256)

img2 = pyplot.imshow(zvals,interpolation='nearest',
                    cmap = cmap2,
                    origin='lower')

pyplot.colorbar(img2,cmap=cmap2)

pyplot.show()"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint

xMax, yMax = 100, 100

x = np.arange(xMax)
y = np.arange(yMax)
z = np.zeros([xMax,yMax])

for _ in range (10):
	z[randint(0,100), randint(0,100)] = 20

plt.pcolormesh(x,y,z)
plt.colorbar()

plt.show()











