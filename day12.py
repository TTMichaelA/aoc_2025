import time

def read_input(filename):
    regions = {}
    with open(filename) as input:
        for i, line in enumerate(input):
            if "x" not in line:
                continue
            else:
                lenwid, gifts = line.strip("\n").split(": ")
                gifts = gifts.split(" ")
                lenwid = lenwid.split("x")
                regions[i-30] = ( (tuple([int(x) for x in lenwid]),tuple([int(x) for x in gifts])))
    return regions
if __name__ == "__main__":
    possible_regions = 0
    reg = read_input("day12_input.py")
    for i, r in reg.items():
        a = r[0][0] * r[0][1]
        t = sum(r[1]) * 7
        print(f"{r[0][0]} * {r[0][1]} vs. {sum(r[1]) * 7} :: {a} vs. {t}")
        if r[0][0] * r[0][1] >= sum(r[1]) * 7:
            print("cnt += 1")
            possible_regions += 1
    
    print(possible_regions)