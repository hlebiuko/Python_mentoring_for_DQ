import random

# Create a list of 100 random numbers from 0 to 1000
my_list = [random.randint(0, 1000) for _ in range(100)]

# Sort the list from min to max (without using sort())
my_sorted_list = []
for x in range(len(my_list)):
    min_value = my_list[0]
    for y in range(len(my_list) - 1):
        if my_list[y + 1] < min_value:
            min_value = my_list[y + 1]
    my_sorted_list.append(min_value)
    my_list.remove(min_value)

# Calculate average for even and odd numbers
average_even = 0
average_odd = 0
even_counter = 0
odd_counter = 0

for x in range(len(my_sorted_list)):
    if x % 2 == 0:
        average_odd += my_sorted_list[x]
        odd_counter += 1
    else:
        average_even += my_sorted_list[x]
        even_counter += 1

average_even /= even_counter
average_odd /= odd_counter

# Print both average results in console
print('Average odd =', average_odd)
print('Average even =', average_even)
