import sys
sys.path.append("..")

from aocutil import FrequencyStore


input_file = open("input", "r")

twos = 0
threes = 0

for line in input_file:
    store = FrequencyStore()
    for ch in line:
        store.insert(ch)

    two = False     # Save if the word will count for two
    three = False   # Save if the word will count for three
    freqs = store.get_frequencies()

    # Count each frequency, if there is a 2 and/or a three then that word
    # will add one for whichever one(s) it had to the total count
    for f in freqs:
        if f == 2:
            two = True
        elif f == 3:
            three = True

        # No need to keep iterating if the word already counts for both
        if two and three:
            break

    if two:
        twos += 1
    if three:
        threes += 1

print(twos*threes)
