import bisect

input_file = open("input", "r")

changes = []
previous = []
frequency = 0

#Finds the index where frequency would be inserted
#If frequency is already there, encountered duplicated frequency
def check_previous():
    i = bisect.bisect_left(previous, frequency)
    if i != len(previous) and previous[i] == frequency:
        return i

    return False

#Read in all of the freqeuncy changes
for line in input_file:
    changes.append(int(line))

index = 0
while True:
    frequency += changes[index]

    if check_previous():
        print(frequency)
        break

    #Insert new frequency, keeping array in sorted order
    bisect.insort_left(previous, frequency)
    index += 1
    if index >= len(changes):
        index = 0