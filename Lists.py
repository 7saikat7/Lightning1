listing = []
i = 0
j = 0
for i in range(0, 10):
    j = i * 2
    listing.append(j)
print(listing)
listing.sort()  # arranges the list in increasing order
print(listing)
listing.reverse()
print(listing)
# slicing
print(listing[0:5])

