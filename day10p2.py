import time
import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


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
    
def min_presses_for_machine(buttons, joltage):
    jol_len = len(joltage)
    button_len = len(buttons)

    A = np.zeros((jol_len, button_len))
    for j, button in enumerate(buttons):
        for i in button:
            A[i, j] = 1
    b = np.array(joltage)
    c = np.ones(button_len)

    constraint = LinearConstraint(A, lb=b, ub=b)
    bounds = Bounds(lb=np.zeros(button_len), ub=np.full(button_len, np.inf))
    res = milp(c=c,constraints=[constraint],bounds=bounds, integrality=np.ones(button_len))

    presses = int(round(res.fun))


    return presses


if __name__ == "__main__":
    start_time = time.perf_counter()
    pi = build_input("day10_input.py")
    sum = 0
    for i in range(len(pi)):
        j = pi[i]["j"]
        b = pi[i]["b"]
        best = min_presses_for_machine(b, j)
        print(best)
        sum += best
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(f"Max presses is {sum}, calculated in {elapsed:.6f} seconds.")
    

    