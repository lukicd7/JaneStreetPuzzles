# square = [[9,8,10,12,11,8,10,7],
#           [7,9,11,9,10,12,14,12],
#           [4,7,5,8,8,6,13,10],
#           [4,10,7,9,6,8,7,9],
#           [2,6,4,2,5,9,8,11],
#           [0,3,1,4,2,7,10,7],
#           [1,2,0,1,2,5,7,6],
#           [0,2,4,3,5,6,2,4]]

square = [[11,10,11,14],
          [8,6,9,9],
          [10,4,3,1],
          [7,6,5,0]]

cur_pos = "a1"
total_duration = 0

def translate_pos(pos):
    return len(square) - int(pos[1]), ord(pos[0]) - 96 - 1

def print_array():
    print("Total Duration: ", total_duration)
    print("Current State of Array:")
    for row in square:
        frmt = "{:>5}"*len(row) # trying to format the row data with 5 blank spaces
        print(frmt.format(*row)) # makes it have nice layout as the numbers grow or shrink or have - sign
    print("\n")

def movement(duration, new_pos):
    total_duration += duration
    print("you moved")
    print_array()

# print(square[cur_row][cur_col])
print(translate_pos('c4'))

