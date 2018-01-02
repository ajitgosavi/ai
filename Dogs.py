import numpy as np
import matplotlib.pyplot as plot

greyhound = 500
lab = 500
greyhound_height = 28 + 4 * np.random.randn(greyhound)
lab_height = 28 + 4 * np.random.randn(lab)
plot.hist([greyhound_height, lab_height],stacked= True, color=['r','b'])
