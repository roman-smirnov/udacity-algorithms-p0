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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

callers = [c[0] for c in calls]
callees = [c[1] for c in calls]
texters = [t[0] for t in texts]
textees = [t[1] for t in texts]

suspect_marketers = set()
for n in callers:
    if n not in texters and n not in textees and n not in callees:
        suspect_marketers.add(n)

# worst case runtime is O(n^4) because I check if each element callers against all the other lists
print('These numbers could be telemarketers: ')
print(*sorted(suspect_marketers), sep='\n')
