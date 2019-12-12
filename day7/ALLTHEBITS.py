import computer.computer as PC
import itertools

program = ""
with open("input", "r") as f:
    program = f.read()

program = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"

def run_aux(mode, signal_in):
    """Runs the auxilerary program with mode and signal returning output"""
    this_aux = PC.int_computer(program)
    result = this_aux.run_program([mode, signal_in])
    return result

def aux_phase(phase_code):
    signal_in = 0
    for mode in phase_code:
        signal_in = run_aux(int(mode), signal_in)
    return signal_in

#part 1
thurster_signals = set()
for perm in itertools.permutations("01234"):
    thurster_signals.add(aux_phase("".join(perm)))

print(f"max thrust for part 1 {max(thurster_signals)}")

#part 2
#feedback_signals = set()
# uhh... fuck... uhhh

#aux_phase_fb()
#print(f"max thrust for part 2 {max(feedback_signals)}")