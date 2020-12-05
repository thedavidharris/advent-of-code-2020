#!/usr/bin/env python3
with open('input.txt', 'r') as f:
    input = f.read().splitlines()

# print(input)

substrings = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
numValid = 0
numInvalid=0

passports=[""]
index=0
for line in input:
    if line == "":
        passports.append("")
        index +=1
    else:
        passports[index] += line + " "

for line in passports:
    valid = True
    for string in substrings:
        if string not in line:
            valid = False
    
    if valid:
        parts = line.split(" ")
        parts = parts[:-1]
        # print(parts)

        numbers = {0,1,2,3,4,5,6,7,8,9}
        validFields = True
        for part in parts:
            [key, value] = part.split(":")
            if key == "byr":
                if int(value) < 1920 or int(value) > 2002:
                    validFields = False
            elif key == "iyr":
                if int(value) < 2010 or int(value) > 2020:
                    validFields = False
            elif key == "eyr":
                if int(value) < 2020 or int(value) > 2030:
                    validFields = False
            elif key == "hgt":
                if "cm" in value:
                    height = int(value.replace("cm", ""))
                    if height < 150 or height > 193:
                        validFields = False
                elif "in" in value:
                    height = int(value.replace("in", ""))
                    if height < 59 or height > 76:
                        validFields = False
                else:
                    validFields = False
            elif key == "hcl":
                letters = {"a", "b","c","d","e","f"}
                if "#" in value:
                    if value[0] in numbers:
                        for num in value:
                            if int(num) not in numbers:
                                validFields = False
                    elif value[0] in letters:
                         for letter in value:
                            if letter not in letters:
                                validFields = False
                else:
                    validFields = False
            elif key == "ecl":
               valid = {"amb", "blu", "brn", "gry", "grn","hzl", "oth"}
               if value not in valid:
                   validFields = False
            elif key == "pid":
                if len(value) != 9:
                    validFields = False
                else:
                    for num in value:
                        if int(num) not in numbers:
                            validFields = False
            
        if validFields:
            numValid += 1
            print(line)


print(numValid)