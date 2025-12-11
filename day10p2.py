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

def process_joltage(config_str):
    config_list = config_str.replace("{","").replace("}","").split(",")
    output_list = [int(x) for x in config_list]
    return tuple(output_list)

def build_input(filename):
    with open(filename) as input_file:
        i = 0
        machine_list = {}
        for line in input_file:
            light_config_raw = re.search("(\[.*\])", line.strip("\n")).group(1)
            button_set_raw = re.search("(\(.*\))", line.strip("\n"))
            joltage_raw = re.search("(\{.*\})", line.strip("\n")).group(1)

            machine_list[i] = {}
            machine_list[i]["l"] = process_light_config(light_config_raw)
            machine_list[i]["b"] =  process_button_set(button_set_raw.group())
            machine_list[i]["j"] = process_joltage(joltage_raw)
            i += 1
        return machine_list
    
def distance_from_joltage(putative, actual):
    for i in range(len(putative)):
        if putative[i] > actual[i]:
            return -1
        
    return sum(putative)

def check_valid(putative, actual):

        
    return 

def handle_record(buttons, joltage):
    brute_forcer = queue.PriorityQueue()
    attempted = set()
    best = sum(joltage)

    button_set = (0,) * len(buttons)
    presses = 0
    jolt = (0,) * len(joltage)
    dist = 0
    
    attempted.add(button_set)

    base = (dist, presses, button_set, jolt)
    brute_forcer.put(base)
    
    while not brute_forcer.empty():
        next_record = brute_forcer.get()
        print(next_record)
        dist = -next_record[0]
        presses = -next_record[1]
        if presses > best:
            continue
        
        button_set = list(next_record[2])
        jolt = list(next_record[3])
        for i in range(len(buttons)):
            npresses = presses + 1
            nbutton_set = button_set.copy()
            nbutton_set[i] += 1
            nbutton_set = tuple(nbutton_set)
            if nbutton_set in attempted:
                continue
            njolt = jolt.copy()
            for j in range(len(buttons[i])):
                k = buttons[i][j]
                njolt[k] += 1
            njolt = tuple(njolt)
            ndist = distance_from_joltage(njolt, joltage)
            if ndist < 0:
                attempted.add(nbutton_set)
                continue
            elif njolt == joltage:
                attempted.add(nbutton_set)
                if not best or npresses < best:
                    best = npresses
            else:
                if nbutton_set not in attempted and npresses < best:
                    attempted.add(nbutton_set)
                    next = (-ndist, -npresses, nbutton_set, njolt)
                    brute_forcer.put(next)

    return best


            

    


if __name__ == "__main__":
    pi = build_input("day10_input.py")
    for i in range(1):
        j = pi[i]["j"]
        b = pi[i]["b"]
        best = handle_record(b, j)
        print(best)
    

    