import sys

class int_computer ():
    
    def __init__(self, program_text):
        self.program = list(map(lambda x: int(x), program_text.split(",")))
        self.instruction_ptr = 0
        self.output = 0
        self.halt = False
    # takes an instruction and returns a dictionary with its opcode and mode
    def instruction_parse(self, instruction):

        # note: mode stored as binary number.
        instruction_data = {
            "opcode":0,
            "mode":0b0
        }

        # if simple instruction
        if (len(str(instruction)) == 1):
            instruction_data["opcode"] = instruction
        else:
            # opcode two far-most right digits
            instruction_data["opcode"] = int(str(instruction)[len(str(instruction))-2:])
            #print(instruction_data["opcode"])

            if (instruction_data["opcode"] != 99):
                print(str(instruction)[:len(str(instruction))-2])
                instruction_data["mode"] = int(str(instruction)[:len(str(instruction))-2], 2)
            else:
                print(f"HALTED: {self.output}")
                self.halt = True
                # get mode from the remaining digits
        print(instruction_data["opcode"])
        return instruction_data

    def setupParameter(self, mode, value):
        if (self.instruction_parse(self.program[self.instruction_ptr])["mode"] & mode):
            return self.program[self.instruction_ptr+value]
        else:
            return self.program[self.program[self.instruction_ptr+value]]

    def run_program(self, inputs):
        ic = 0
        while (self.halt == False):
            offset = 0

            this_instruction = self.instruction_parse(self.program[self.instruction_ptr])

            if (this_instruction["opcode"] == 1):
                # add together values at positions 1 and 2 then store at index noted in position 3
                parameter_one = self.setupParameter(0b1, 1)
                parameter_two = self.setupParameter(0b10, 2)

                # third position always considered positional
                self.program[self.program[self.instruction_ptr+3]] = parameter_one + parameter_two

                offset = 4

            elif (this_instruction["opcode"] == 2):
                # multiply together values at positions 1 and 2 store in position 3
                
                parameter_one = self.setupParameter(0b1, 1)
                parameter_two = self.setupParameter(0b10, 2)

                self.program[self.program[self.instruction_ptr+3]] = parameter_one * parameter_two

                offset = 4
        
            elif (this_instruction["opcode"] == 3):
                # takes input and saves at position stated in parameter 
                #self.program[self.program[self.instruction_ptr+1]] = int(input())
                if(ic <= 1):
                    self.program[self.program[self.instruction_ptr+1]] = inputs[ic]
                    ic += 1
                else:
                    self.program[self.program[self.instruction_ptr+1]] = self.output
                offset = 2

            elif (this_instruction["opcode"] == 4):
                # outputs value at position
                parameter = self.setupParameter(0b1, 1)
                self.output = parameter
                #sbreak
                #print(parameter)

                offset = 2
            
            elif (this_instruction["opcode"] == 5):
                # JUMP-IF-TRUE
                parameter_one = self.setupParameter(0b1, 1)
                parameter_two = self.setupParameter(0b10, 2)

                if (parameter_one != 0):
                    self.instruction_ptr = parameter_two
                else:
                    offset = 3

            elif (this_instruction["opcode"] == 6):
                # JUMP-IF-FALSE
                parameter_one = self.setupParameter(0b1, 1)
                parameter_two = self.setupParameter(0b10, 2)

                if (parameter_one == 0):
                    self.instruction_ptr = parameter_two
                else:
                    offset = 3
            
            elif (this_instruction["opcode"] == 7):
                # LESS-THAN
                parameter_one = self.setupParameter(0b1, 1)
                parameter_two = self.setupParameter(0b10, 2)
                

                if (parameter_one < parameter_two):
                    self.program[self.program[self.instruction_ptr+3]] = 1
                else:
                    self.program[self.program[self.instruction_ptr+3]] = 0
                
                offset = 4

            elif (this_instruction["opcode"] == 8):
                # EQUALS
                parameter_one = self.setupParameter(0b1, 1)
                parameter_two = self.setupParameter(0b10, 2)

                if (parameter_one == parameter_two):
                    self.program[self.program[self.instruction_ptr+3]] = 1
                else:
                    self.program[self.program[self.instruction_ptr+3]] = 0
                
                offset = 4
            elif (this_instruction["opcode"] == 99): pass
            else:
                print(this_instruction["opcode"])
                exit()
            # increment based on number of parameters
            self.instruction_ptr += offset
        return self.output


# with open("input", "r") as f:
#     problem_input = f.read()
