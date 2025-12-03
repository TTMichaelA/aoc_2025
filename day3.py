def get_banks():
    banks = {}
    with open("day3_input.txt") as puzzle_input:
        i = 0
        for line in puzzle_input:
            banks[i] = line.strip("\n")
            i += 1
    return banks

def digit_check(num_str):
    for i in range(9,0,-1):
        ind1 = num_str[:len(num_str)-1].find(str(i)) 
        if ind1 >= 0:
            for i in range(9,0,-1):
                ind2 = num_str[ind1+1:len(num_str)].find(str(i))
                if ind2 >= 0:
                    num_str2 = num_str[ind1+1:len(num_str)]
                    return int(num_str[ind1]) * 10 + int(num_str2[ind2])


def part_one(banks):
    score = 0
    for bank in banks.values():
        print(bank)
        score += digit_check(bank)
    return score
            


if __name__ == "__main__":
    banks = get_banks()
    print((banks))
    print(part_one(banks))

