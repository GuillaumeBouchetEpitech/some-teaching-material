
# to run in a terminal -> 'pip install numpy'
import numpy

# to run in a terminal -> 'pip install scikit-learn'
import scipy

# to run in a terminal -> 'pip install matplotlib'
import matplotlib.pyplot as plt



print("") # spacing in the console


#
# mean, median, mode, standard deviation, percentile
#

all_cars_speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]


print(f"(mean) average car speed -> {numpy.mean(all_cars_speed)}")
print(f"(median) middle car speed -> {numpy.median(all_cars_speed)}")
print(f"(mode) most common car speed -> {scipy.stats.mode(all_cars_speed)}")
print(f"(std) car speed distance from the middle value -> {numpy.std(all_cars_speed)}")
print(f"(percentile) max car speed of 80% of the drivers -> {numpy.percentile(all_cars_speed, 80)}kmh")


plt.hist(all_cars_speed, 5) # <- histogram
plt.xlabel('Cars Speed')
plt.ylabel('Total Cars')
plt.title('Cars Speed Histogram')
plt.show(block=True) # <- force the window to open and stay open




print("") # spacing in the console

