import time
def partone():
    iranges = []
    cnt = 0
    with open("day05_input.txt") as puzzle_input:
        
        for line in puzzle_input:
            input = line.strip("\n").split("-")
            if len(input) > 1:
                iranges.append((int(input[0]), int(input[1])))
            elif input[0] == '':
                continue
            else:
                for range in iranges: 
                    if int(input[0]) >= range[0] and int(input[0]) <= range[1]:
                        cnt+=1
                        break
    return cnt


def check_overlap(range1, range2):
    l1, r1 = range1
    l2, r2 = range2

    if l1 >= l2 and l1 <= r2:
        return True
    if r1 >= l2 and r1 <= r2:
        return True 
    if l1 <= l2 and r1 >= r2:
        return True
    if l1 >= l2 and r2 <= r2:
        return True
    else:
        return False

def parttwo():
    iranges = []
    cnt = 0
    with open("day5_input.txt") as puzzle_input:
        
        for line in puzzle_input:
            input = line.strip("\n").split("-")
            if len(input) > 1:
                irange = (int(input[0]), int(input[1]))
                iranges.append(irange)
            elif input[0] == '':
                break
    sranges = sorted(iranges)
    
    counter =0
    for i in range(len(sranges)):
        irange = sranges[i]
        counter = max(irange[0], counter)
        if counter <= irange[1]:
            cnt += irange[1] - counter + 1
            counter = irange[1] + 1
    return cnt
    

if __name__ == "__main__":

    # Record the start time
    start_time = time.perf_counter()
    cnt = partone()
    cnt2 = parttwo()

    # Record the end time
    end_time = time.perf_counter()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the result
    print(f"Part one answer is: {cnt}")
    print(f"Part two answer is: {cnt2}")
    print(f"Code execution time: {elapsed_time:.6f} seconds")

