def get_coords(roll):
    m = (-1, 0, 1)
    coords = []
    for k in m:
        for l in m:
            if k == l == 0:
                continue
            coords.append((roll[0]+k, roll[1]+l))
    return coords

def remove_rolls(rolls):
    remove_list = set()
    for roll in rolls:
        cnt = 0
        for coord in get_coords(roll):
            if coord in rolls:
                cnt +=1
        if cnt < 4:
            remove_list.add(roll)
    return remove_list


def partone():
    rolls = set()
    with open("day4_input.txt") as puzzle_input:
        h = 0
        for line in puzzle_input:
            l = len(line.strip("\n"))
            for j in range(l): 
                if line[j] == '@':
                    rolls.add((h,j))
            h += 1

def parttwo():
    rolls = set()
    with open("day4_input.txt") as puzzle_input:
        h = 0
        for line in puzzle_input:
            l = len(line.strip("\n"))
            for j in range(l): 
                if line[j] == '@':
                    rolls.add((h,j))
            h += 1
    
    rm = remove_rolls(rolls)
    cnt = len(rm)
    print("Pt 1: ", cnt)
    prev = len(rolls)
    next = 0
    rolls -= rm
    
    while prev != next:
        rm = remove_rolls(rolls)
        cnt += len(rm)
        rolls -= rm
        prev = next
        next = len(rolls)
    print("Pt 2: ", cnt)

if __name__ == "__main__":
    partone()
    parttwo()
            