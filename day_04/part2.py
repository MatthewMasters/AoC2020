import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def parse_passport(text):
    return dict([kv.split(':') for kv in text.replace('\n', ' ').split(' ')])


def check_validity(passport):
    try:
        byr = 1920 <= int(passport['byr']) <= 2002
        iyr = 2010 <= int(passport['iyr']) <= 2020
        eyr = 2020 <= int(passport['eyr']) <= 2030
        hgt = int(passport['hgt'][:-2])
        hgt_unit = passport['hgt'][-2:]
        if hgt_unit == 'cm':
            hgt = 150 <= hgt <= 193
        elif hgt_unit == 'in':
            hgt = 59 <= hgt <= 76
        else:
            hgt = False

        hcl = len(re.findall("^#[a-fA-F0-9]{6}", passport['hcl'])) == 1
        ecl = passport['ecl'].lower() in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        pid = passport['pid'].strip()
        pid = len(pid) == 9 and pid.isnumeric()

        checks = [byr, iyr, eyr, hgt, hcl, ecl, pid]
        return sum(checks) == len(checks)
    except:
        return False


def count_valid(passports):
    return sum([check_validity(passport) for passport in passports])


if __name__ == '__main__':
    passport_text = open('input.txt').read().strip().split('\n\n')
    passports = [parse_passport(text) for text in passport_text]
    count = count_valid(passports)
    print(count)