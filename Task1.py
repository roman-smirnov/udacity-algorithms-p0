"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
numbers = []

for t in texts:
    numbers.append(t[0])
    numbers.append(t[1])

for c in calls:
    numbers.append(c[0])
    numbers.append(c[1])

unique_numbers = set(numbers)
# the worst case runtime complexity is O(n^2) because I assume creating a set is an O(n^2) operation
print('There are ', len(unique_numbers), ' different telephone numbers in the records.')

