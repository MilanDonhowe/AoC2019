# graphical!
import pprint

def read_layer_data(width, height, data):
    """Take height, width and data and returns list each containing the layer data"""
    layers = []
    for layer in range(1, int((len(data)/(width*height)+1))):
        this_layer = data[(len(layers)*height*width):(layer*height*width)]
        this_layer_data = []
        for pixel in this_layer:
            this_layer_data.append(int(pixel))
        layers.append(this_layer_data)
    return layers

def count_digit(layer, digit):
    dig_total = 0
    for i in layer:
        if (i == digit):
            dig_total += 1
    return dig_total

def fewest_zero_digit_layer(layer_data):
    count_zeros = list(map (lambda lay: count_digit(lay, 0), layer_data))
    return layer_data[count_zeros.index(min(count_zeros))]

def multiply_ones_with_twos(layer):
    return count_digit(layer, 1) * count_digit(layer, 2)    

with open("input", "r") as f:
    problem_input = f.read()

# part 1
print (multiply_ones_with_twos(fewest_zero_digit_layer(read_layer_data(25, 6, problem_input))))

# part 2

def get_color(px):
    if (px == 0):
        return "black"
    elif(px == 1):
        return "white"
    else:
        return "red"

def draw_image(width, height, data):
    """Draws the image from data"""

    image_data = read_layer_data(width, height, data)
    image_list = []
    for h in range(height):
        image_list.append(list('9'*(width)))

    for layer in image_data:
        #print(layer)
        for y in range(height):
            for x in range(width):
                if (int(image_list[y][x]) >= 2):
                    image_list[y][x] = layer[(width*y)+x]



    for row in image_list:
        disp_str = ""
        for digit in row:
            if digit == 1: disp_str += str(digit)
            else: disp_str += " "
        print(disp_str)
#ZYBLH
                
draw_image(25, 6, problem_input)
input()