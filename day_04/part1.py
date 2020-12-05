import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def parse_passport(text):
    return dict([kv.split(':') for kv in text.replace('\n', ' ').split(' ')])


def check_validity(passport):
    return sum([1 for field in required_fields if field in passport.keys()]) == len(required_fields)


def count_valid(passports):
    return sum([check_validity(passport) for passport in passports])


if __name__ == '__main__':
    passport_text = open('input.txt').read().strip().split('\n\n')
    passports = [parse_passport(text) for text in passport_text]
    count = count_valid(passports)
    print(count)