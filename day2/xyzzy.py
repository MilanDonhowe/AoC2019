#int code program
#yeah I don't really get it either

def intcode(string_input):
    program_counter = 0;
    program = list(map(lambda x: int(x), string_input.split(",")))
    while True:
        if (program[program_counter] == 1):
            # add together values at positions 1 and 2 then store at index noted in position 3
            program[program[program_counter+3]] = program[program[program_counter+1]] + program[program[program_counter+2]]
        elif (program[program_counter] == 2):
            # multiply together values at positions 1 and 2 store in position 3
            program[program[program_counter+3]] = program[program[program_counter+1]] * program[program[program_counter+2]]
        elif (program[program_counter] == 99):
            #print("Program Finished!")
            break
        else:
            print("error... unexpected opcode")
            exit()
        program_counter += 4
    return program


submission_code = ""
with open("input.txt", "r") as f:
    submission_code = f.read()

#part 1
#print(intcode(submission_code))

#part 2
def brute_force(int_program):
    #ah shit I kinda fucked myself didn't i?
    int_program = list(map(lambda x: int(x), int_program.split(',')))
    counter = 0
    for pos_one in range (0, 100):
        for pos_two in range(0, 100):
            int_program[1] = pos_one
            int_program[2] = pos_two
            stringify_program = ",".join( list(map(lambda x: str(x), int_program) ) )
            results = intcode(stringify_program)
            if (results[0] == 19690720):
                print(f"The correct noun and verb are {pos_one} and {pos_two}")
                exit()
            else:
                counter += 1
                print(f"attempt #{counter} failed, trying again...")

brute_force(submission_code)




