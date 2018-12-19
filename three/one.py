import collections
from claim import Claim

def get_input_array(input_file):
    input = []

    for line in input_file:
        pieces = line.split()
        i = pieces[0]
        c = pieces[len(pieces) - 2]
        s = pieces[len(pieces) - 1]

        id_string = i.replace("#", "")
        id = int(id_string)

        coords = c.replace(":", "")
        xy = coords.split(",")
        x = int(xy[0])
        y = int(xy[1])

        size = s.split("x")
        width = int(size[0])
        height = int(size[1])

        input.append(Claim(id, x, y, width, height))

    return input

input_file = open("input", "r")
claims = get_input_array(input_file)

fabric = collections.defaultdict(float)

x_max = claims[0].x
y_max = claims[0].y
for claim in claims:
    if claim.x > x_max:
        x_max = claim.x
    elif claim.x+claim.width > x_max:
        x_max = claim.x+claim.width
    if claim.y > y_max:
        y_max = claim.y
    elif claim.y+claim.height > y_max:
        y_max = claim.y+claim.height

for claim in claims:
    for j in range(claim.y, claim.y+claim.height):
        for i in range(claim.x, claim.x+claim.width):
            fabric[i, j] += 1

total = 0
for j in range(y_max+1):
    for i in range(x_max+1):
        if fabric[i, j] > 1:
            total += 1
print(total)

for claim in claims:
    overlap = False
    for j in range(claim.y, claim.y+claim.height):
        for i in range(claim.x, claim.x+claim.width):
            if fabric[i, j] > 1:
                overlap = True

            if overlap == True:
                break

        if overlap == True:
            break

    if overlap == False:
        print(claim.id)
        break
