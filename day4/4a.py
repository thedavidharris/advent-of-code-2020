#!/usr/bin/env python3

# print(sum ( all(x in d for x in ["byr","iyr","eyr","hgt","hcl","ecl","pid"]) and all([1920<= int(d["byr"]) <=2002,2010<= int(d["iyr"]) <=2020,2020<= int(d["eyr"]) <=2030,d["hgt"][-2:] in ("cm","in") and ( ( d["hgt"][-2:] == "in" and 59<= int(d["hgt"][:-2]) <= 76 ) or( d["hgt"][-2:] == "cm" and 150<= int(d["hgt"][:-2]) <= 193) ),d["hcl"][0] == "#" and all (c in "0123456789abcdef" for c in d["hcl"][1:]),d["ecl"] in "amb blu brn gry grn hzl oth".split(),d["pid"].isdigit() and len(d["pid"])==9]) for d in [ dict( tuple(x.split(":")) for x in line.split() ) for line in [ line.replace("\n"," ") for line in open(day_04_path).read().split("\n\n") ] ]) )

print(sum(all(key in passportKeyValues for key in ["byr","iyr","eyr","hgt","hcl","ecl","pid"]) for passportKeyValues in [dict(x.split(":") for x in line.split()) for line in [line.replace("\n"," ") for line in open("input.txt", "r").read().split("\n\n")]]))

# expectedFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}