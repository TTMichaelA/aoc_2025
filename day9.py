import time

def build_input(filename):
    coords = []
    with open(filename) as puzzle_input:
        for line in puzzle_input:
            sanitized = line.strip("\n").split(",")
            coords.append((int(sanitized[0]), int(sanitized[1])))
    return coords

def part_one(coord_input):
    max_area = 0
    for i in range(len(coord_input)):
        for j in range(i+1, len(coord_input)):
            x = abs(coord_input[i][0] - coord_input[j][0]) + 1
            y = abs(coord_input[i][1] - coord_input[j][1]) + 1
            max_area = max(max_area, x * y)
    return max_area

def build_polygon(coord_input):
    row_records = {}
    for i in range(len(coord_input)):
        if i == len(coord_input) - 1:
            xi, yi = coord_input[i]
            xj, yj = coord_input[0]
        else:    
            xi, yi = coord_input[i]
            xj, yj = coord_input[i+1]
        x1 = min(xi, xj)
        x2 = max(xi, xj)
        y1 = min(yi, yj)
        y2 = max(yi, yj)

        if x1 == x2:
            for k in range(y1, y2 + 1):
                if x1 in row_records.keys():
                    row_records[x1].add((x1, k))
                else:
                    row_records[x1] = set()
                    row_records[x1].add((x1, k))
        else:
            for k in range(x1, x2 + 1):
                if k in row_records.keys():
                    row_records[k].add((k, y1))
                else:
                    row_records[k] = set()
                    row_records[k].add((k, y1)) 

    return row_records

def fill_polygon(polygon):
    filled_poly = {}
    for row, rowset in polygon.items():
        filled_poly[row] = set()
        sort_row = sorted(list(rowset), key=lambda x:(x[0], x[1]))
        i = 0
        start = None
        curr = -1
        while i <  len(sort_row):
            if start is None:
                start = sort_row[i][1]
                curr = start
            elif curr == sort_row[i][1] - 1:
                curr = sort_row[i][1] 
            else:
                filled_poly[row].add((start, sort_row[i][1]))
                start = None
                curr = -1
            i +=1
            continue
        if start:
            filled_poly[row].add((start, sort_row[i-1][1]))

    return filled_poly
            

def check_square(c1, c2, filled_poly):
        xi, yi = c1
        xj, yj = c2
        x1 = min(xi, xj)
        x2 = max(xi, xj)
        y1 = min(yi, yj)
        y2 = max(yi, yj)

        i = x1
        
        while i < x2+1:
            j = y1
            while j < y2+1:
                within = False
                for r in filled_poly[i]:
                    if j>= r[0] and j <= r[1]:
                        within = True
                        j = r[1]
                        break
                if not within:
                    return False
                j += 1
            i += 1
        return True

def part_two(coord_input, filled_poly):
    max_area = 0
    for i in range(len(coord_input)):
        for j in range(i+1, len(coord_input)):
            x = abs(coord_input[i][0] - coord_input[j][0]) + 1
            y = abs(coord_input[i][1] - coord_input[j][1]) + 1
            if x * y > max_area:
                # print("Checking ", coord_input[i], "and ", coord_input[j])
                if check_square(coord_input[i], coord_input[j], filled_poly):
                    max_area = x * y
    return max_area

if __name__ == "__main__":
    start_time = time.perf_counter()
    pi = build_input("day9_input.txt")
    # print(pi)
    pg = build_polygon(pi)
    pgf = fill_polygon(pg)
    ma1 = part_one(pi)    
    end_time = time.perf_counter()
    cnt2= part_two(pi, pgf)
    end_time2 = time.perf_counter()
    
    # print(ma1)
    # for j in range(1,1):
    #     print(j)

    elapsed = end_time - start_time
    elapsed2 = end_time2 - start_time
    print(f"Part one answer is {ma1}, calculated in {elapsed:.6f} seconds")
    print(f"Part one answer is {cnt2}, calculated in {elapsed2:.6f} seconds")


