# part 1
def valid_pass(num):
    last_digit = str(num)[0]
    double = False
    valid = True
    for char in str(num)[1:]:
        if (int(char) < int(last_digit)):
            valid = False
            break
        elif (int(char) == int(last_digit)):
            double = True
        last_digit = char
    if (double): return valid
    else: return False


lower_bound = 171309
upper_bound = 643603
total_valid_passwords = 0
for num in range(lower_bound, upper_bound):
    if (valid_pass(num)): total_valid_passwords += 1

print(f"range {lower_bound} to {upper_bound} has {total_valid_passwords} valid passwords")

# part 2

def occurances(char, string):
    seen = 0
    for c in string:
        if c == char:
            seen += 1
    return seen

def strict_valid_pass(num):

    # check for doubling repeating digit
    double = False
    unique_digits = set(str(num))
    for digit in unique_digits:
        if (occurances(digit, str(num)) == 2):
            double = True
    if (double == False): return False

    # make sure digits are in ascending order
    last_digit = str(num)[0]
    valid = True
    for char in str(num)[1:]:
        if (int(char) < int(last_digit)):
            valid = False
            break
        last_digit = char
    return valid

total_valid_passwords = 0
for num in range(lower_bound, upper_bound):
    if (strict_valid_pass(num)): total_valid_passwords += 1

print(f"range {lower_bound} to {upper_bound} has {total_valid_passwords} strict valid passwords")