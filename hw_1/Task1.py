import random

# Create a list of 100 random numbers from 0 to 1000
lst = [random.randint(0, 1000) for _ in range(100)]

# Sort the list from min to max (without using sort())
n = len(lst)
for i in range(n - 1):
    for j in range(n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Calculate average for even and odd numbers
average_even = 0
average_odd = 0
even_counter = 0
odd_counter = 0

for i, item in enumerate(lst):
    if i % 2 == 0:
        average_odd += lst[i]
        odd_counter += 1
    else:
        average_even += lst[i]
        even_counter += 1

average_even /= even_counter
average_odd /= odd_counter

# Print both average results in console
print('Average odd =', average_odd)
print('Average even =', average_even)
