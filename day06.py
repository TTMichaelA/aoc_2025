import time
def partone():
    operations = []
    with open("day06_input.txt") as puzzle_input:
        for line in puzzle_input:
            line_operations = []
            i = 0
            buffer = ''
            while i < len(line):
                
                if line[i] in (' ','\n'):
                    if len(buffer) >= 1:
                        line_operations.append(buffer)
                    buffer = ''
                else:
                    buffer += line[i]
                i+=1
            operations.append(line_operations)
    sum = 0

    for i in range(len(operations[0])):
        if operations[4][i] == '*':
            sum += (int(operations[0][i]) * 
                    int(operations[1][i]) *
                    int(operations[2][i]) *
                    int(operations[3][i]))
        else:

            sum += (int(operations[0][i]) + 
                    int(operations[1][i]) +
                    int(operations[2][i]) +
                    int(operations[3][i]))
    
    # print(operations)
    return sum
    
def parttwo():
    grid = []
    with open("day6_input.txt") as puzzle_input:
        for line in puzzle_input:
            grid.append(line.strip('\n'))
    k = 0
    groups = {}
    sum = 0
    ops = []
    for i in range(len(grid[0])):
        if grid[4][i] != ' ':
            ops.append(grid[4][i])
        
        val = grid[0][i] + grid[1][i] + grid[2][i] + grid[3][i]
        if val == '    ':
            k += 1
        else:
            if k not in groups.keys():
                groups[k] = [int(val)]
            else:
                groups[k].append(int(val))
    
    for g in range(len(ops)):
        partial = 1
        if ops[g] == '*':
            for operand in groups[g]:
                partial *= operand
        else:
            partial = 0
            for operand in groups[g]:
                partial += operand
        sum+= partial
            
    return sum

if __name__ == "__main__":
    start_time = time.perf_counter()
    cnt = partone()
    end_time = time.perf_counter()
    elapsed_time1 = end_time - start_time
    
    start_time = time.perf_counter()
    cnt2 = parttwo()
    end_time = time.perf_counter()
    elapsed_time2 = end_time - start_time

    print(f"Part one answer is: {cnt}")
    print(f"Calculation time: {elapsed_time1:.6f} seconds")
    print(f"Part two answer is: {cnt2}")
    print(f"Calculation time: {elapsed_time2:.6f} seconds")
    print(f"Total time: {(elapsed_time1 + elapsed_time2):.6f} seconds")
