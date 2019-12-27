import pprint, os, time, sys

class int_computer:

    def __init__(self, program):
        self.memory = list(map(lambda x: int(x), program.split(","))) + [0 for x in range(1000000)]
        self.memory[0] = 2
        self.instruction_ptr = 0
        self.relative_base = 0
        self.halting = False
        self.this_instruction = None
        self.screen = []
        self.screen_state = 0
        self.screen_x = 0
        self.screen_y = 0
        self.block_total = 0
        self.ball_pos = [0, 0]
        self.paddle_pos = [0, 0]
        self.on_sequence = 0
        self.score = 0

    def instruction_parse(self, instruction):
        """takes int (not-string) instuction returns dictionary with keys "mode" and "opcode" """
        data = {
            "mode":'00',
            "opcode":0,
            "raw":instruction # for debugging
        }

        if (len (str(instruction)) == 1):
            data["opcode"] = instruction
        elif (instruction == 99):
            data["opcode"] = instruction
        else:
            data["opcode"] = int(str(instruction)[-2:])
            data["mode"] = str(instruction)[:-2]
            if (len(data["mode"]) == 1):
                data["mode"] = "0" + data["mode"]

        return data


    def render(self, out):
        if (out == -1):
            self.on_sequence = 1
        elif (out == 0) and (self.on_sequence == 1):
            self.on_sequence = 2
        elif (self.on_sequence == 2):
            self.score = out
            self.on_sequence = 0
        else:
            self.screen_state += 1
            if (self.screen_state == 1):
                self.screen_x = out
            elif (self.screen_state == 2):
                self.screen_y = out
            else:
                self.screen_state = 0
                # map_id
                self.map_id(out)
    
    def map_id(self, out):
        
        if out == 0:
            this_tile = " "
        elif out == 1:
            this_tile = "|"
        elif out == 2:
            this_tile = "#"
            self.block_total += 1

        elif out == 3:
            this_tile = "_"
            self.paddle_pos[0] = self.screen_x
            self.paddle_pos[1] = self.screen_y
        else:
            self.ball_pos[0] = self.screen_x
            self.ball_pos[1] = self.screen_y
            this_tile = "@"
        
        while (self.screen_y >= len(self.screen)):
            self.screen.append([None])
        while ( self.screen_x >= len( self.screen[self.screen_y] ) ):
            self.screen[self.screen_y].append('')
        
        self.screen[self.screen_y][self.screen_x] = this_tile

    def setupParameters(self, total_params=2):
        # returns tuple with 1st and 2nd parameters
        mode = str(self.this_instruction["mode"])
        if (total_params == 1):
            if ('1' in self.this_instruction['mode']):
                return self.memory[self.instruction_ptr+1]
            elif ('2' in self.this_instruction['mode']):
                return self.memory[self.relative_base + self.memory[self.instruction_ptr+1]]
            else:
                return self.memory[self.memory[self.instruction_ptr+1]]

        
        ps = []
        
        if (len(mode) > 2):
            mode = mode [1:]

        index = total_params
        for setting in mode:
            if setting == '1':
                # immediate mode
                val = self.memory[self.instruction_ptr+index]
                ps.append(val)
            elif setting == '2':
                # relative mode
                val = self.memory[self.relative_base + self.memory[self.instruction_ptr+index]]
                ps.append(val)
            else:
                # position mode
                val = self.memory[self.memory[self.instruction_ptr+index]]
                ps.append(val)
            index -= 1

        return (ps[1], ps[0])


    def write(self, value):
        # writes value to third parameter taking mode into account
        if (self.this_instruction['mode'][0] == '2') and (len(self.this_instruction['mode']) == 3):
            self.memory[self.relative_base + self.memory[self.instruction_ptr+3]] = value
        else:
            self.memory[self.memory[self.instruction_ptr+3]] = value

    def auto_play(self):
        time.sleep(0.05)
        if self.ball_pos[0] > self.paddle_pos[0]:
            return 1
        elif self.ball_pos[0] < self.paddle_pos[0]:
            return -1
        return 0

    def run(self):
        """runs the program loaded into memory"""
        while not self.halting:
            offset = 0
            this_instruction = self.instruction_parse(self.memory[self.instruction_ptr])
            self.this_instruction = this_instruction

            if (this_instruction["opcode"] == 99):
                #halt instruction
                self.halting = True
            
            elif (this_instruction["opcode"] == 1):
                # add together values at positions 1 and 2 then store at index noted in position 3
                p1, p2 = self.setupParameters()
                # third position always considered positional
                self.write(p1 + p2)
                offset = 4

            elif (this_instruction["opcode"] == 2):
                # multiply together values at positions 1 and 2 store in position 3
                p1, p2 = self.setupParameters(2)
                self.write(p1 * p2)

                offset = 4
            elif (this_instruction["opcode"] == 3):
                # takes input and saves at position stated in parameter

                
                #sys.stdout.write("\r")
                #sys.stdout.flush()
                outstr = ""
                for line in self.screen:
                    for char in line:
                        outstr += char
                    outstr += "\n"
                sys.stdout.write("\r" * len(outstr))
                sys.stdout.flush()
                sys.stdout.write(outstr)
                sys.stdout.flush()
                
                #print(outstr)

                if '2' in this_instruction['mode']:
                    self.memory[self.relative_base + self.memory[self.instruction_ptr+1]] = self.auto_play()
                else:
                    self.memory[self.memory[self.instruction_ptr+1]] = self.auto_play()

                #os.system("cls")

                offset = 2

            elif (this_instruction["opcode"] == 4):
                # outputs value at position
                p1 = self.setupParameters(1)


                self.render(p1)


                #print(p1)

                offset = 2
            
            elif (this_instruction["opcode"] == 5):
                # JUMP-IF-TRUE
                p1, p2 = self.setupParameters()
                if (p1 != 0):
                    self.instruction_ptr = p2
                else:
                    offset = 3

            elif (this_instruction["opcode"] == 6):
                # JUMP-IF-FALSE
                p1, p2 = self.setupParameters()

                if (p1 == 0):
                    self.instruction_ptr = p2
                else:
                    offset = 3
            
            elif (this_instruction["opcode"] == 7):
                # LESS-THAN
                p1, p2 = self.setupParameters()

                if (p1 < p2):
                    self.write(1)
                else:
                    self.write(0)
                
                offset = 4

            elif (this_instruction["opcode"] == 8):
                # EQUALS
                p1, p2 = self.setupParameters()
                if (p1 == p2):
                    self.write(1)
                else:
                    self.write(0)                
                offset = 4
            
            elif (this_instruction["opcode"] == 9):
                # ADD TO RELATIVE BASE REGISTER

                p1 = self.setupParameters(1)
                self.relative_base += p1

                offset = 2

            else:
                print("error... unexpected opcode %d" % (this_instruction["opcode"]))
                exit()
            # increment based on number of parameters
            self.instruction_ptr += offset
        print(f"there are {self.block_total} blocks\n and the total score is {self.score}")