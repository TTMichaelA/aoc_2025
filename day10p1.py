import time
import re
import queue

def process_light_config(config_str):
    config_str = config_str[1:len(config_str)-1].replace(".","0").replace("#","1")
    return [int(x) for x in config_str]

def process_button_set(config_str):
    config_list = config_str.replace("(","").replace(")","").split(" ")
    output_list = []
    for c in config_list:
        output_list.append([int(x) for x in c if x != ','])
    return output_list

def build_input(filename):
    with open(filename) as input_file:
        i = 0
        machine_list = {}
        for line in input_file:
            light_config_raw = re.search("(\[.*\])", line.strip("\n")).group(1)
            button_set_raw = re.search("(\(.*\))", line.strip("\n"))
            misc = re.search("(\{.*\})", line.strip("\n")).group(1)
            # print(misc)
            machine_list[i] = {}
            machine_list[i]["l"] = process_light_config(light_config_raw)
            machine_list[i]["b"] =  process_button_set(button_set_raw.group())
            machine_list[i]["m"] = misc
            i += 1
        return machine_list

def evaluate_combination(machine_list, rownum, presses):
    light_combo = machine_list[rownum]["l"]
    buttons = machine_list[rownum]["b"]
    tgt = {}
    for t in range(len(light_combo)):
        tgt[t] = 0
    for i in range(len(presses)):
        if presses[i] > 0:
            for j in buttons[i]: 
                tgt[j] += 1
    for i in tgt.keys():
        tgt[i] = tgt[i] % 2

    result = [0 for x in light_combo]
    for i, r in tgt.items():
        result[i] = r
    return result == light_combo

def generate_combinations(machine_list, rownum):
    presses_list = queue.PriorityQueue()
    n_buttons = len(machine_list[rownum]["b"])
    i = 1
    curr_set = set()
    curr_set.add((1,))
    curr_set.add((0,))
    while i < n_buttons:
        prev_set = curr_set
        curr_set = set()
        for j in prev_set:
            curr_set.add((1,) + j)
            curr_set.add((0,) + j)
        i += 1
    for item in curr_set:
        wt = sum(item)
        presses_list.put((wt, item))
    return presses_list 

def part_one(puzzle_input):
    sum = 0
    for k in puzzle_input.keys():
        guesses = generate_combinations(puzzle_input, k)
        done = False
        while not done:
            
            guess = guesses.get()
            wt = guess[0]
            candidate = guess[1]
            
            done = evaluate_combination(puzzle_input, k, candidate)
            if done:
                sum += wt
    
    return sum


if __name__ == "__main__":

    start_time = time.perf_counter()
    pi = build_input("day10_input.py")
    
    cnt1 = part_one(pi)
    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(f"Day 10 pt. 1 done in {elapsed:.6f} seconds with value {cnt1}")
