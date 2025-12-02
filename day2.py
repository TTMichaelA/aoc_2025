import day2_input

def validity_check(num):
    nstr = str(num)
    if len(nstr) % 2 == 0:
        if nstr[:len(nstr) // 2] == nstr[len(nstr) // 2:]:
            return False
    return True

def validity_check2(num):
    nstr = str(num)
    candidates = set()
    for i in range(1, len(nstr) // 2 + 1):
        if len(nstr) % i == 0:
            candidates.add(i)
    for candidate in candidates:
        # print(candidate)
        num_seqs = set()
        j = 0
        k = candidate
        # print(j, k)
        # print(len(nstr))
        while k <= len(nstr):
            num_seqs.add(nstr[j:k])
            # print(num_seqs)
            j += candidate
            k += candidate
            # print(j, k)
            if len(num_seqs) > 1:
                continue
        if len(num_seqs) == 1:
            return False

    return True



def process_input(input):
    input_list = input.split(",")
    score = 0
    for numrange in input_list:
        min, max = numrange.split("-")
        for num in range(int(min), int(max)+1):
            if not validity_check(num):
                score += num
    return score

def process_input2(input):
    input_list = input.split(",")
    score = 0
    for numrange in input_list:
        min, max = numrange.split("-")
        for num in range(int(min), int(max)+1):
            if not validity_check2(num):
                score += num
                # print("adding ", num)
    return score

if __name__ == "__main__":
    puzzle_input = day2_input.puzzle_input
    print(puzzle_input)
    print(process_input(puzzle_input))
    print(process_input2(puzzle_input))
