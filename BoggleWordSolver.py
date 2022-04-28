class Tree():
    def __init__(self, letter = None, ):
        self.letter = letter
        self.children = {} # a dictionary to hold the child trees
        self.leaf = False
        
    #add a word, letter by letter to the tree structure
    def add(self, word):
        if len(word): #True unless word length is 0
            letter = word[0]
            word = word[1:]
            if letter not in self.children: #if letter not already in the children dictionary
                self.children[letter] = Tree(letter) #add a dictionary entry with key letter and value new Tree(letter)
            return self.children[letter].add(word) # add the truncated word to the child letter tree, and return that child
        else: #base case - end of word
            self.leaf = True
            return self #return this Tree
        
    # locate a letter in the tree
    def search(self, letter):
        if letter not in self.children: # therefore, from this point
                                        # no words exist with this letter
                                        # as the next letter
            return None
        else:
            return self.children[letter]

# function for the word solver
# from each grid, starting examine possible directions
# appending letters to string. track path to prevent backtrack
# for each letter appended check in the dictionary tree to see
# to see if that next letter branch exists and hence
# a valid word has been created. If not, we return out of the function.
# If we encounter a leaf, we add the word to a list of validated words.
# depth first traversal - we keep adding letters to the string until
# a valid word is found, or a path terminates, then we backtrack and add
# another available letter to the string
def findWord(board, tree, validated, row, col, path = None, currLetter = None, word = None):
            # parameters: validated is the set of valid words to date
            # row and col are the current board coordinates
            # path tracks the path on the board, to prevent backtracking
            # currLetter stores the point on the Tree we are at
            # word = the string of letters built so far
    letter = board[row][col]
    if path is None or currLetter is None or word is None: # if this is the first letter
        currLetter = tree.search(letter) # get the first level on the tree with the letter
        path = [(row, col)] # add first location to path
        word = letter #add first letter to string
    else:
        currLetter = currLetter.search(letter) #set currLetter to next step in branch (or none)
        path.append((row,col)) #add the current location to the path
        word = word + letter #append the letter to the string

    # base cases
    if currLetter is None: #then this isn't a valid word
        return

    if currLetter.leaf: #if leaf is true, this is a valid word - add it and continue
        validated.add(word)

    # recursive call
    for r in range(row-1, row+2): # range is the row above to row below
        for c in range(col-1, col+2): #range is column to left to column to right
            if (r>=0 and r<4 and c>=0 and c<4 and (r,c) not in path): # r != row and c != col and
                #check for grid bounds, current position or previously used locations
                findWord(board, tree, validated, r, c, path[:], currLetter, word[:])
                # call findWords for each available adjacent location

def main():
    # aprint("Hello")
    #initialise game board based on user input
    board = []
    for row in range(0,4):
        row_list = []
        for cell in range(0,4):
            letter = input(f"Enter letter {cell + 1} from row {row + 1}:").strip().upper()
            row_list.append(letter)
        board.append(row_list)
    
    for i in range(0,4):
        for j in range (0,4):
            print(board[i][j], end = " ")
        print()

    # load dictionary
    dict = open('dictionary-yawl.txt', "r")

    tree = Tree() #instantiate tree object
    for line in dict: #only one word per line
        word = line.rstrip().upper() 
        tree.add(word) #add words to tree object

    #set to store strings that match valid words in the dictionary
    validated = set()

    #call the findWords function from each grid
    for row in range(0,4):
        for col in range(0,4):
            findWord(board, tree, validated, row, col)

    for word in sorted(validated):
        if len(word) > 2:
            print(word)

main()