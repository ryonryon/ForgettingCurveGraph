import numpy as np
import math
from matplotlib import pyplot

k = 1.84
K = 1 / k
c = 1.25
g = 15

def forgetting_curve(t):
    return (math.log10(t))**c * 100 * K / (K * (math.log10(t))**c + 1)

curve_data = [forgetting_curve(i) for i in range(1, 10**5, g)]
x = [i for i in range(1, 10**5, g)]

pyplot.title('Forgetting Curve')
pyplot.xlabel('minute (m)')
pyplot.ylabel('Forgetting Rate(%)')

pyplot.xscale("log")
pyplot.plot(x, curve_data, "r-")
pyplot.show()
