#########################
# Puzzle "Knight Moves 5"
# https://www.janestreet.com/puzzles/current-puzzle/
#########################

square = [[9.,8.,10.,12.,11.,8.,10.,17.],
          [7.,9.,11.,9.,10.,12.,14.,12.],
          [4.,7.,5.,8.,8.,6.,13.,10.],
          [4.,10.,7.,9.,6.,8.,7.,9.],
          [2.,6.,4.,2.,5.,9.,8.,11.],
          [0.,3.,1.,4.,2.,7.,10.,7.],
          [1.,2.,0.,1.,2.,5.,7.,6.],
          [0.,2.,4.,3.,5.,6.,2.,4.]]

from copy import deepcopy

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
    s = [[str(e) for e in row] for row in my_array]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)

    x,y = translate_pos(cur_pos)
    temp_array = deepcopy(my_array) # lists are mutable, need to deepcopy
    temp_array[x][y] = '\033[91m' + str(temp_array[x][y]) + '\033[0m'

    s = [[str(e) for e in row] for row in temp_array]
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))

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
movement(0, "a4")
movement(0, "a5")
movement(0, "c4")
movement(0, "e4")
movement(0, "f2")
movement(0, "f3")
movement(0, "g5")
movement(0, "h5")

movement(6, "h6")
movement(0, "g8")
movement(0, "e8")
movement(0, "c7")

movement(15, "d7")

movement(12, "b6")
movement(0, "d7")

movement(76, "c5")
movement(0, "b3")
movement(0, "b1")
movement(0, "c1")
movement(0, "e1")
movement(0, "e2")

movement(5, "d4")
movement(0, "c4")
movement(0, "a5")
movement(0, "c5")
movement(0, "c6")

movement(3, "e6")
movement(0, "e4")
movement(0, "d4")
movement(0, "d6")

movement(60, "b7")
movement(0, "c5")
movement(0, "e6")
movement(0, "f4")
movement(0, "d5")
movement(0, "d4")
movement(0, "c4")
movement(0, "a5")
movement(0, "c6")
movement(0, "c7")
movement(0, "d7")
movement(0, "e7")
movement(0, "f7")
movement(0, "g7")

movement(1, "h7")
movement(0, "h8")

print_array(num_visits)

# other ideas
# 1: get a different number to 17, then all the 17's to ~15's, then all the ~15's to ~13's, etc.
# until we have almost ALL ~5's and then we just hop kiddie corners around to get to H8 which is ~5