import re
from collections import defaultdict
with open('data/my_input/5.in') as f:
    lines = f.read().split("\n\n")

def part1(vlines):
    all_seeds= list(map(int,re.findall(r"\d+",vlines[0])))
    seed_to_soil_data=vlines[1]
    soil_to_fertilizer_data=vlines[2]
    fertilizer_to_water_data=vlines[3]
    water_to_light_data=vlines[4]
    light_to_temperature_data=vlines[5]
    temperature_to_humidity_data=vlines[6]
    humidity_to_location_data=vlines[7]
    seed_to_soil_map=dict()
    soil_to_fertilizer_map=dict()
    fertilizer_to_water_map=dict()
    water_to_light_map=dict()
    light_to_temperature_map=dict()
    temperature_to_humidity_map=dict()
    humidity_to_location_map=dict()
    for data in seed_to_soil_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        seed_to_soil_map[range(source,source+numrange)]=range(destination,destination+numrange)
    for data in soil_to_fertilizer_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        soil_to_fertilizer_map[range(source,source+numrange)]=range(destination,destination+numrange)
    for data in fertilizer_to_water_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        fertilizer_to_water_map[range(source,source+numrange)]=range(destination,destination+numrange)
    for data in water_to_light_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        water_to_light_map[range(source,source+numrange)]=range(destination,destination+numrange)
    for data in light_to_temperature_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        light_to_temperature_map[range(source,source+numrange)]=range(destination,destination+numrange)
    for data in temperature_to_humidity_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        temperature_to_humidity_map[range(source,source+numrange)]=range(destination,destination+numrange)
    for data in humidity_to_location_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        humidity_to_location_map[range(source,source+numrange)]=range(destination,destination+numrange)

    all_sequences=list()
    for seed in all_seeds:
        sequence=[seed]
        for source in seed_to_soil_map.keys():
            if seed in source:
                seed=seed_to_soil_map[source][0]+seed-source[0]           
                break
        sequence.append(seed)
        for source in soil_to_fertilizer_map.keys():
            if seed in source:
                seed=soil_to_fertilizer_map[source][0]+seed-source[0]
                break
        sequence.append(seed)
        for source in fertilizer_to_water_map.keys():
            if seed in source:
                seed=fertilizer_to_water_map[source][0]+seed-source[0]
                break
        sequence.append(seed)
        for source in water_to_light_map.keys():
            if seed in source:
                seed=water_to_light_map[source][0]+seed-source[0]
                break
        sequence.append(seed)
        for source in light_to_temperature_map.keys():
            if seed in source:
                seed=light_to_temperature_map[source][0]+seed-source[0]
                break
        sequence.append(seed)
        for source in temperature_to_humidity_map.keys():
            if seed in source:
                seed=temperature_to_humidity_map[source][0]+seed-source[0]
                break
        sequence.append(seed)
        for source in humidity_to_location_map.keys():
            if seed in source:
                seed=humidity_to_location_map[source][0]+seed-source[0]
                break
        sequence.append(seed)
        all_sequences.append(sequence)
    return min(map(lambda x : x[-1],all_sequences))


def part2(vlines):
    all_seeds= list(map(int,re.findall(r"\d+",vlines[0])))
    all_ranges=list()
    for i in range(len(all_seeds)//2):
        all_ranges.append(range(all_seeds[2*i],all_seeds[2*i]+all_seeds[2*i+1]))
    seed_to_soil_data=vlines[1]
    soil_to_fertilizer_data=vlines[2]
    fertilizer_to_water_data=vlines[3]
    water_to_light_data=vlines[4]
    light_to_temperature_data=vlines[5]
    temperature_to_humidity_data=vlines[6]
    humidity_to_location_data=vlines[7]
    seed_to_soil_map=dict()
    soil_to_fertilizer_map=dict()
    fertilizer_to_water_map=dict()
    water_to_light_map=dict()
    light_to_temperature_map=dict()
    temperature_to_humidity_map=dict()
    humidity_to_location_map=dict()
    for data in seed_to_soil_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        seed_to_soil_map[range(source,source+numrange)]=range(destination,destination+numrange)
    for data in soil_to_fertilizer_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        soil_to_fertilizer_map[range(source,source+numrange)]=range(destination,destination+numrange)
    for data in fertilizer_to_water_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        fertilizer_to_water_map[range(source,source+numrange)]=range(destination,destination+numrange)
    for data in water_to_light_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        water_to_light_map[range(source,source+numrange)]=range(destination,destination+numrange)
    for data in light_to_temperature_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        light_to_temperature_map[range(source,source+numrange)]=range(destination,destination+numrange)
    for data in temperature_to_humidity_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        temperature_to_humidity_map[range(source,source+numrange)]=range(destination,destination+numrange)
    for data in humidity_to_location_data.split("\n")[1:]:
        destination,source,numrange = list(map(int,re.findall(r"\d+",data)))
        humidity_to_location_map[range(source,source+numrange)]=range(destination,destination+numrange)

    min_value=10e10
    for all_seeds in all_ranges:
        for seed in all_seeds:
            for source in seed_to_soil_map.keys():
                if seed in source:
                    seed=seed_to_soil_map[source][0]+seed-source[0]           
                    break
            for source in soil_to_fertilizer_map.keys():
                if seed in source:
                    seed=soil_to_fertilizer_map[source][0]+seed-source[0]
                    break
            for source in fertilizer_to_water_map.keys():
                if seed in source:
                    seed=fertilizer_to_water_map[source][0]+seed-source[0]
                    break
            for source in water_to_light_map.keys():
                if seed in source:
                    seed=water_to_light_map[source][0]+seed-source[0]
                    break
            for source in light_to_temperature_map.keys():
                if seed in source:
                    seed=light_to_temperature_map[source][0]+seed-source[0]
                    break
            for source in temperature_to_humidity_map.keys():
                if seed in source:
                    seed=temperature_to_humidity_map[source][0]+seed-source[0]
                    break
            for source in humidity_to_location_map.keys():
                if seed in source:
                    seed=humidity_to_location_map[source][0]+seed-source[0]
                    break
            if seed < min_value:
                min_value=seed
    return min_value

print(part1(lines))
print(part2(lines))