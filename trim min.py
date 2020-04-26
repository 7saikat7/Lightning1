from statistics import mean
import statistics
import matplotlib.pyplot as plt

estimates = [12, 34, 50, 78, 5, 56, 89, 23, 90, 100, 44, 79, 34, 67, 76, 11, 101, 1000]
estimates.sort()  # by default sorts in assending order
tv = int(0.1 * len(estimates))
estimates = estimates[tv:]  # removing smallest 10% values
print(estimates)
estimates = estimates[:len(estimates) - tv]  # removing largest 10% values
print(mean(estimates))
# above program of trim mean was done in traditional way
y = []
for i in range(len(estimates)):
    y.append(5)
print(y)
plt.plot(estimates, y, 'go')
plt.plot(60, 5, 'r^')
plt.plot([statistics.median(estimates)], [5],'bs')
plt.show()
