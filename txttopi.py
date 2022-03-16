import sympy as sp
try:
    from sympy.mpmath import mp
except ImportError:
    from mpmath import mp

def get_count():
    count = 0
    with open("pi.txt") as pi_file_without_digits:
        for line in pi_file_without_digits:
            for ch in list(line):
                if ch != ' ' and ch != '\n':
                    count = count + 1
    return count

def get_chars(count):
    mp.dps = count
    return str(mp.pi)

def replace_chars(chars):
    updated_file_contents = ""
    index = 0
    with open("pi.txt") as pi_file_without_digits:
        for line in pi_file_without_digits:
            for ch in list(line):
                if ch != ' ' and ch != '\n':
                    updated_file_contents = updated_file_contents + list(chars)[index]
                    index = index + 1
                elif ch == '\n':
                    updated_file_contents = updated_file_contents + '\n'
                elif ch == ' ':
                    updated_file_contents = updated_file_contents + ' '
    return updated_file_contents

def write_to_file(file_contents):
    with open("pi-with-digits.txt", "a") as pi_file_with_digits:
        pi_file_with_digits.write(file_contents)

write_to_file(replace_chars(get_chars(get_count())))