"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

numbers = dict()
for c in calls:
    numbers[c[0]] = int(c[-1]) + numbers.get(c[0], 0)
    numbers[c[1]] = int(c[-1]) + numbers.get(c[1], 0)

longest_num, longest_time = sorted(numbers.items(), key=lambda item: item[1], reverse=True)[0]
# worst case runtime should be O(nlog(n)) because sorting is the most time consuming operation here
print(longest_num, ' spent the longest time, ', longest_time, ' seconds, on the phone during September 2016.')
