input_file = open("input", "r")
frequency = 0

for line in input_file:
    frequency += int(line)

print(frequency)