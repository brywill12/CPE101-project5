#Project5
#Name: Kitty Zhuang and Branyt Williamson
#Instructor: Einakian
#Section: 1

################################################

import sys
args = sys.argv

# This is a function to group the RGB colors in a list.

def groups_of_3(list1):

    num_slices = int(len(list1))//3
    residual = int(len(list1))%3
    new_list = [list1[3*i : ((i+1)*3)] for i in range(num_slices)]
    if residual != 0:
        new_list.append(list1[num_slices*3:])
    return new_list

# Terminate the program for incorrect argument

if len(args) != 4 or type(args[2]) != 'str' or type(args[3])!= int or type(args[4])!= int or type(args[5])!= int:
    print('Usage: python3 fade.py <image> <row> <column> <radius>')
    exit()

try:
    # This part is to re-organize the information stored in the image file into a list.
    fin = open(args[2])
    list_values = []
    for lines in fin:
        values = lines.split() #values would be a list of strings
        for i in range(len(values)):
            if values[i].isdigit() == True:
                list_values.append(int(values[i]))
            else:
                list_values.append(values[i])

    # This part assigns variable names to the corresponding information
    header = list_values[0]
    width = list_values[1]
    height = list_values[2]
    maximum = list_values[3]

    # Separate the RBG values into groups for each pixel
    rgb_values = list_values[4:]
    rgb_group = groups_of_3(rgb_values)

    #Calculate the distance each pixel has to the specified point(center of fade)

except:
    print('Unable to open'+args[1])
