def get_coords(i, j):
    m = (-1, 0, 1)
    coords = []
    for k in m:
        for l in m:
            if k == l == 0:
                continue
            coords.append((i+k, j+l))
    return coords


if __name__ == "__main__":
    counter = {}
    rolls = set()
    with open("day4_input.txt") as puzzle_input:
        h = 0
        for line in puzzle_input:
            l = len(line.strip("\n"))
            for j in range(l): 
                if line[j] == '@':
                    rolls.add((h,j))
                    for coord in get_coords(h, j):
                        if coord in counter.keys():
                            counter[coord] += 1
                        else:
                            counter[coord] = 1
            h += 1
    
    cnt = 0
    for key in rolls:
        if key not in counter.keys():
            cnt += 1
            continue
        if counter[key] < 4:
            cnt += 1
    print(cnt)



            