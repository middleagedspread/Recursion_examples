from copy import deepcopy

#the grid to be solved
Grid = [['5', '.', '1', '.', '.', '4', '.', '.', '2'],
        ['6', '.', '9', '5', '.', '7', '3', '8', '.'],
        ['.', '.', '7', '.', '.', '.', '4', '.', '.'],
        ['.', '.', '6', '3', '.', '2', '.', '1', '.'],
        ['2', '1', '.', '.', '.', '.', '.', '.', '6'],
        ['7', '.', '.', '9', '.', '.', '8', '2', '4'],
        ['3', '.', '.', '6', '.', '1', '2', '.', '8'],
        ['9', '6', '.', '7', '.', '.', '1', '.', '5'],
        ['.', '.', '5', '2', '.', '.', '6', '7', '.']]

elements = ['1','2','3','4','5','6','7','8','9'] #allowed numbers

def get_rows(new_Grid): # accepts a n rows x m columns matrix
                        # (list of n lists each of m items), e.g.:
                        # [['.', '.', '2', '3'], ['.', ' ...
                        # returns a list containing n dictionaries, representing rows
                        # mapping m matrix entries to matrix coordinates, e.g.:
                        # [{(0, 0): '.', (0, 1): '.', (0, 2): '2', (0, 3): '3'}, {(1, 0): ...
    rows = [] #create an empty list
    ## NEEDS EDITTING
    for r in range(len(Grid)): #for each sublist
        row = {} #create a dictionary
        for c in range(len(Grid)): # for each item in the sublist
            row[(r,c)] = new_Grid[r][c] # set the key as a tuple representing grid coordinate
                                        # and the value to the value at that point in the sublist
        rows.append(row) #append each dictionary to the rows list
    return rows

def get_cols(new_Grid):# accepts a n rows x m columns matrix
                        # (list of n lists each of m items), e.g.:
                        # [['.', '.', '2', '3'], ['.', ' ...
                        # returns a list containing n dictionaries, representing columns
                        # mapping m matrix entries to matrix coordinates, e.g.:
                        # [{(0, 0): '.', (1, 0): '.', (2, 0): '.', (3, 0): '3'}, {(0, 1): '.', ...
    
    cols = [] #create an empty list
    for c in range(len(Grid)): #for each sublist
        col = {} #create a dictionary
        for r in range(len(Grid)): # for each item in the sublist
            col[(r,c)] = new_Grid[r][c] # set the key as a tuple representing grid coordinate
                                        # and the value to the value at that point in the sublist
        cols.append(col) #append each dictionary to the rows list
    return cols

square_indx = [[(0,1,2),(0,1,2)],
               [(0,1,2),(3,4,5)],
               [(0,1,2),(6,7,8)],
               [(3,4,5),(0,1,2)],
               [(3,4,5),(3,4,5)],
               [(3,4,5),(6,7,8)],
               [(6,7,8),(0,1,2)],
               [(6,7,8),(3,4,5)],
               [(6,7,8),(6,7,8)]
              ]
# a list of lists, each list containg a pair of tuples
# each tuple representing the rows and columns of a square
# e.g. top left square represented by rows (0,1,2) and columns (0,1,2)

def get_squares(new_Grid):  # gets a list of dictionaries, each representing a square
                            # mapping the values in each cell in the squares
                            # to their corrdiantes in the matrix
    squares = []
    for sq in range(len(square_indx)):
        square = {}
        for r in square_indx[sq][0]: #get the rows
            for c in square_indx[sq][1]: #get the columns
                square[(r,c)] = new_Grid[r][c] #get the values
        squares.append(square) 
    return squares

def get_all_related_cells(new_Grid): #returns a list of dictionaries representing
                                     # squares, rows and columns
    ## NEEDS EDITTING
    rows = get_rows(new_Grid)
    cols = get_cols(new_Grid)
    squares = get_squares(new_Grid)
    all_vec = squares + rows + cols
    return all_vec

# get the next cell coordinates by iterating through row then column
def get_new_r_c(r, c):
    if c == 3: #if you have reached the end of the row
        if r==3: #if you've also reahced the end of the rows
            new_r = r
            new_c = c
        else: 
            new_r = r+1 #add one to rows, and reset columns to 0
            new_c = 0
    else:
        new_r = r 
        new_c = c+1 #add one to columns
        
    return new_r, new_c

# get all legal numbers for cell(r,c) in the passed grid
def get_legal_for_cell(cell_r, cell_c, new_Grid):

    if new_Grid[cell_r][cell_c] != '.': #check there isn't already a number there
        return [None],[None],[None]

    map = {}

    all_groups = get_all_related_cells(new_Grid) # get all the squares, rows and columns
    for group in all_groups:
        if (cell_r,cell_c) in group.keys(): # find the square, column and row that contain this cell
            map.update(group)   # add the elements (key value pairs) from the relevant square
                                # row and column to our map dictionary
    exist = []
    ## NEEDS EDITTING
    for m in map: #for items in map
        if not map[m] ==".": #if it's a number rather than a  '.'
            exist.append(map[m]) #append it to the exists list
    
    
    ## NEEDS EDITTING
    rest = list(set(elements)-set(exist)) # a list made of the set of elements not in the set exist
    return rest, exist, map

def is_complete(new_Grid):
    grid_complete = True
    for r in new_Grid:
        grid_complete = grid_complete and not ('.' in r)
    return grid_complete

def print_grid(new_Grid):
    for item in new_Grid:
        print(item)
    print()

def solve_step_in_sudoko(last_Grid, r, c):
    ## Base Case - print and exit
    if is_complete(last_Grid):
        print('Complete:')
        print_grid(last_Grid)
        return 0
    ## get a list of all legal numbers for next cell
    legal_for_cell, _, _ = get_legal_for_cell(r,c, last_Grid) # get legal next number for cell
    
    # loop through each legal item for next cell
    # if there is no legal item next, the for loop is skipped,
    # ending this iteration of the function call, returning to the previous call point.
    # if this item is the right one, the recursion calls will reach the base case
    # if it isn't, the recursion won't reach base case, and the for loop will move to the next item
    for item in legal_for_cell: # for each legal number in next cell
        new_Grid = deepcopy(last_Grid) # copy the last grid
        if last_Grid[r][c]=='.': #check it's an empty cell
            new_Grid[r][c]=item #add the legal number to the next cell
        new_r, new_c = get_new_r_c(r,c) # get the next cell address
        ## the recursion call
        solve_step_in_sudoko(new_Grid, new_r, new_c) #recursively call next step
    # if the code gets to here, then the for loop has exhausted it's list of legal moves
    # without reaching the base case, and the function returns to the place it was called
    # (either 1. the for loop in the previous iteration of the function, or 2. the original call)
    # if it reaches 2. without solving the grid, the grid has no solution

solve_step_in_sudoko(Grid, 0, 0)