NORTH, SOUTH, WEST, EAST = 1, 2, 3, 4 

class int_computer:

    def __init__(self, program):
        self.memory = list(map(lambda x: int(x), program.split(","))) + [0 for x in range(1000000)]
        self.instruction_ptr = 0
        self.relative_base = 0
        self.halting = False
        self.this_instruction = None

        # robot specific properties
        self.input = None
        self.output = None

        self.open = set()
        self.wall = set()
        self.x = 0
        self.y = 0
        self.directions = {
            NORTH: (0, 1),
            SOUTH: (0, -1),
            EAST: (1, 0),
            WEST: (-1, 0)
        }

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

                self.decide_next_move(self.output)
                user_in = self.input

                if '2' in this_instruction['mode']:
                    self.memory[self.relative_base + self.memory[self.instruction_ptr+1]] = user_in
                else:
                    self.memory[self.memory[self.instruction_ptr+1]] = user_in

                offset = 2

            elif (this_instruction["opcode"] == 4):
                # outputs value at position
                p1 = self.setupParameters(1)                
                print(p1)
                self.output = p1
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

    def apply_direction(self, direct_tuple):
        self.x += direct_tuple[0]
        self.y += direct_tuple[1]
        return (self.x, self.y)

    def test_direction(self, direct_tuple):
        rx = self.x
        ry = self.y
        rx += direct_tuple[0]
        ry += direct_tuple[1]
        return (rx, ry)

    def decide_next_move(self, response=None):
        if response == None:
           self.input = NORTH
        elif response == 1:
            # move was successful
            open_place = self.apply_direction(self.directions[self.input])
            self.open.add(open_place)
            print(f"successfully moved to {open_place}")

            for key, vector in self.directions.items():
                if not (self.test_direction(vector) in self.open or self.test_direction(vector) in self.wall):
                    self.input = key
                    break


        elif response == 2:
            # oxygen system found!
            # TODO: calculate shortest distance
            print(f"Oxygen tank found!")
            print(self.open)
            exit()
        
        elif response == 0:
            # okay go to first not visited position
            wall_place = self.test_direction(self.directions[self.input])
            self.wall.add(wall_place)
            print(f"wall hit at {wall_place}")
            for key, vector in self.directions.items():
                if not (self.test_direction(vector) in self.wall):
                    self.input = key
                    break
            # okay well in this case backtrack!
            self.input = self.reverse_direction(self.input)

    def reverse_direction(self, dir):
        if dir == NORTH: return SOUTH
        elif dir == SOUTH: return NORTH
        elif dir == WEST: return EAST
        else: return WEST