def compare(words, value):
    for w in words:
        diff = 0
        correct = ""

        for i in range(0, len(w)):
            if w[i] != value[i]:
                diff += 1
            else:
                correct += w[i]

        if diff == 1:
            return correct

    return ""

input_file = open("input", "r")
ids = []

for line in input_file:
    ids.append(line)

for id in ids:
    answer = compare(ids, id)
    if answer != "":
        print(answer)
        break
