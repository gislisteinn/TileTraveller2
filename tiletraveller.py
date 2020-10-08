  
# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'


def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")

def total_coins(coin_total):
    coin_amount = 0
    pull_lever = input("Pull a lever (y/n): ")
    pull_lever = pull_lever.lower()
    if pull_lever == "y":
        coin_total += 1
        print("You received 1 coin, your total is now {}.".format(coin_total))
        coin_amount = coin_total
        return coin_amount
    else:
        coin_amount = coin_total
        return coin_amount
    

        
def find_directions(col, row, coin_total, pulled_lever):
    ''' Returns valid directions as a string given the supplied location '''
    
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
        if not pulled_lever:
            coin_total = total_coins(coin_total)
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
        if not pulled_lever:
            coin_total = total_coins(coin_total)
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
        if not pulled_lever:
            coin_total = total_coins(coin_total)
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
        if not pulled_lever:
            coin_total = total_coins(coin_total)
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions, coin_total

def play_one_move(col, row, valid_directions, pulled_lever):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    
    if not direction in valid_directions:
        pulled_lever = True
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        pulled_lever = False
    return victory, col, row, pulled_lever

# The main program starts here
victory = False
row = 1
col = 1
coin_total = 0
pulled_lever = False


while not victory:
    valid_directions, coin_total = find_directions(col, row, coin_total, pulled_lever)
    print_directions(valid_directions)
    victory, col, row, pulled_lever = play_one_move(col, row, valid_directions, pulled_lever)
print("Victory! Total coins {}.".format(coin_total))