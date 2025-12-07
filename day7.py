import time

def build_input():
    grid = {}
    i=0
    origin = 0
    with open("day7_input.txt") as puzzle_input:
        for line in puzzle_input:
            if i == 0:
                for k in range(len(line)):
                    if line[k] == 'S':
                        origin =k 
            grid[i] = set()
            for k in range(len(line)):
                if line[k] == '^':
                    grid[i].add(k)
            i += 1
            
    return grid, origin

def partone(grid, origin):
    split = 0
    curr = set()
    curr.add(origin)
    for i in range(len(grid)-1):
        next = set()
        for k in curr:
            if k in grid[i]:
                split+= 1
                next.add(k-1)
                next.add(k+1)
            else:
                next.add(k)
        curr = next
    return split
    
def parttwo(grid, origin):
    split = 0
    curr = {}
    curr[origin] = 1
    for i in range(len(grid)-1):
        next = {}
        for k in curr.keys():
            if k in grid[i]:
                if k-1 in next.keys():
                    next[k-1] += curr[k]
                else:
                    next[k-1] = curr[k]
                if k+1 in next.keys():
                    next[k+1] += curr[k]
                else:
                    next[k+1] = curr[k]
            else:
                if k in next.keys():
                    next[k] += curr[k]
                else:
                    next[k] = curr[k]
        curr = next
    for value in next.values():
        split += value
    return split

if __name__ == "__main__":
    start_time = time.perf_counter()
    
    grid, origin = build_input()

    p1 = partone(grid, origin)
    p2 = parttwo(grid, origin)
    
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    
    print(f"Part one answer is: {p1}")
    print(f"Part one answer is: {p2}")
    print(f"Calculation time: {elapsed:.6f} seconds")
