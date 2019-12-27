# Using the Flawed Frequency Transmission Algorithm

with open("input", "r") as f:
    problem_input = int(f.read())
    problem_part_two = int(str(problem_input))
    problem_offset = int(str(problem_input)[:7])

def generate_pattern(n):
    """returns list for n position"""
    return [0] * n + [1] * n + [0] * n + [-1] * n

def apply_pattern(sequence, pattern, pos):

    sequence = sequence[pos-1:]
    step = 1 + (pos-1)
    acc = 0

    for digit in sequence:
        acc += digit * pattern[step]
        step += 1
        if (step >= len(pattern)): step = 0

    #step = 1
    #accumulator = 0
    #for digit in sequence:
    #    accumulator += digit * pattern[step]
    #    step += 1
    #    if (step >= len(pattern)): step = 0
    accumulator = acc
    result = str(accumulator)[len(str(accumulator))-1]
    return int(result)


def get_next_phase(sequence):
    new_sequence = []
    for position in range(1, len(sequence)+1):
        new_sequence.append(apply_pattern(sequence, generate_pattern(position), position))
    return new_sequence

format_sequence = lambda number : list(map(int, list(str(number))))

# part 1
sequence = format_sequence(problem_input)
for phase in range(100):
    sequence = get_next_phase(sequence)
print(f"after 100 steps: {''.join(map(str,sequence))[:8]}")

# part 2: too slow... reddit recommends backward list traversal with replacing digit in place.  Little confusing but will think about
# [1,2,3,4,5]
# 5 = [0, 0, 0, 0, 1, 1, 1, 1, 1] = 5 
# 4 = [0, 0, 0, 1, 1, 1, 1] = 4 + 5 = 9
# 3 = [0, 0, 1, 1, 1] = 3 + 4 + 5 = 2
# 2 = [0, 1, 1, 0, 0] = 2 + 3 = 5
# 1 = [1, 0, -1, 0, 1] 1 + -3 + 5 = 3
#