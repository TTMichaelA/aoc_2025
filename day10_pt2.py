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
    output_dict = {}
    for i in range(len(output_list)):
        output_dict[i] = output_list[i]
    return output_dict

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
    


if __name__ == "__main__":
    