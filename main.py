import numpy as np

# Create a numpy array of 10 random floats between 0 and 1
random_num = np.random.rand(10)

# Calculate and print the mean, median, and standard deviation
mean = np.mean(random_num)
median = np.median(random_num)
std_dev = np.std(random_num)

print("Random Numbers:", random_num)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
