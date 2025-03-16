
import numpy 
from scipy import stats

marks = (23, 45, 98, 54, 67, 89, 34, 90, 78, 34, 23, 890)
speed = [99, 56, 78, 34, 90, 45, 45, 67, 245]

modee = stats.mode(speed).mode[0]  # Access the mode value
lemmeintroducex = numpy.mean(marks)  # Calculate the mean

print("Mean of marks:", lemmeintroducex)
print("Mode of speed:", modee)
