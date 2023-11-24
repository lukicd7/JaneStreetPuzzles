#########################
# Puzzle "Knight Moves 5"
# https://www.janestreet.com/puzzles/current-puzzle/
#########################

square = [[9,8,10,12,11,8,10,17],
          [7,9,11,9,10,12,14,12],
          [4,7,5,8,8,6,13,10],
          [4,10,7,9,6,8,7,9],
          [2,6,4,2,5,9,8,11],
          [0,3,1,4,2,7,10,7],
          [1,2,0,1,2,5,7,6],
          [0,2,4,3,5,6,2,4]]

import numpy as np
import sys

# square = [[11,10,11,14],
#           [8,6,9,9],
#           [10,4,3,1],
#           [7,6,5,0]]

num_visits = [ [ 0 for i in range(len(square)) ] for j in range(len(square)) ]
num_visits[len(num_visits) - 1][0] = 1

cur_pos = "a1"
total_duration = 0

def translate_pos(pos):
    return len(square) - int(pos[1]), ord(pos[0]) - 96 - 1

def translate_diametric_pos(pos):
    x, y = translate_pos(pos)
    return len(square) - x - 1, len(square) - y - 1


def print_array(my_array):
    # print("Total Duration: ", total_duration)
    # print("Current State of Array:")
    for row in my_array:
        frmt = "{:>7}"*len(row) # trying to format the row data with 5 blank spaces
        print(frmt.format(*(np.round(row,2)))) # makes it have nice layout as the numbers grow or shrink or have - sign
    print("\n")

def movement(duration, new_pos):

    print('-----------------\n-----------------')

    global total_duration
    global cur_pos

    total_duration += duration

    # get positions in array
    x,y = translate_pos(cur_pos)
    xo, yo = translate_diametric_pos(cur_pos)
    old_height_old_pos = square[x][y]

    # need to get the number (n) of similar values and their positions so that we can apply the formula where they decrease by 1 every n minutes
    # diamatric position is ignored for calculating n, and should neither rise nor sink if equal to curr pos
    if (duration != 0):
        xs = [x]
        ys = [y]
        for a in range(len(square)):
            for b in range(len(square)):
                if (a,b) == (x,y) or (a,b) == (xo, yo):
                    continue
                elif (square[x][y] == square[a][b]):
                    xs.append(a)
                    ys.append(b)
        
        # calculate the new values as old_value - duration / n (i.e. sinks at rate 1 unit per n minutes where n = number of lattice points of altitude A)
        n = len(xs)
        value = square[x][y]
        new_value = value - duration / n

        # adjust the similar positions to the new value
        for i in range(n):
            square[xs[i]][ys[i]] = new_value

        # diamatric position is ignored for calculating n, and should neither rise nor sink if equal to curr pos
        # need to raise the diametrically opposite corner by the duration / n amount
        if (square[xo][yo] != value):
            square[xo][yo] += duration / n

    print_array(square)
    print('Moving from ', cur_pos, ' to ', new_pos)
    cur_pos = new_pos
    z = square[x][y]

    # iterate number of visits grid to ensure we are <= 3
    xnew, ynew = translate_pos(new_pos)
    global num_visits
    num_visits[xnew][ynew] += 1

    print('Average board value: ',sum(sum(square,[]))/64)

    # define positions as:
    # x: horizontal (negative is left), ynew - y
    # y: vertical (negative is down), xnew - x
    # z: height / altitude, znew - z
    # x, y, z must be like a knight, one MUST be 0, another MUST be -/+ 1, another MUST be -/+ 2
    znew = square[xnew][ynew]
    xcheck = abs(xnew - x)
    ycheck = abs(ynew - y)
    zcheck = abs(znew - z)
    print('X: ', xcheck, ', Y: ', ycheck, ', Z: ', zcheck)
    if not ((0 in [xcheck, ycheck, zcheck]) and 1 in [xcheck, ycheck, zcheck] and 2 in [xcheck, ycheck, zcheck]):
        print("CANNOT TRAVEL THIS HEIHT DIFFERENCE")
        sys.exit()

    print('Duration Added: ', duration, ' Total Duration: ', total_duration)

    # print possible moves
    # illustrate each of the knight moves (1,2) in (x,y) or (y,x) and the required time to move to the move
    # print('Possible moves: (3, a2), (5, a6)...)

#########################
# Start program here
#########################

# strategy:
# set up the final path ASAP because the average value of the board is constantly decreasing
# get a bunch of points to the same value to abuse the mechanic of sinking as duration / n

print_array(square)

movement(0, "c2")
movement(0, "a2")
movement(9, "a3")
movement(0, "a2")
movement(0, "a1")
movement(0, "b1")
movement(0, "c1")
movement(0, "e1")
movement(4, "f1")
movement(0, "f2")
movement(0, "e2")
movement(0, "d4")
movement(0, "e4")
movement(0, "e5")
movement(0, "f5")
movement(18, "g5")
movement(0, "h5")
movement(6, "h6")
movement(0, "g8")
movement(0, "e8")
movement(9, "c7")

# start a loop to gain duration

movement(0, "d5")
movement(0, "e5")
movement(0, "g5")
movement(56, "f3")
movement(0, "e3")
movement(0, "e4")
movement(0, "e5")
movement(0, "d5")
movement(0, "c7")
movement(0, "e8")
movement(0, "e7")

# finish loop to gain duration
# may want to enter via d7 instead of e8 though, so the first line below may need to be removed

movement(0, "f7")
movement(0, "g7")
movement(1, "h7")
movement(0, "h8")


print_array(num_visits)
