# Pokedex will have the following functionality:
# 1. Look up pokemon by name
# 2. Look up pokemon by number
# 3. Loop up a list of all pokemon belonging to a certain type

# Functions to complete
# input: f - a freshly opened file == the read cursor is at the beginning of the file

# 1. move_cursor(f)
# This function will be used as a helper function for your other functions. 
# This function should skip the header information and move the cursor to 
# the first line in the file that contains actual data.

# header
# def function_name(arguments/inputs):
# description
# body

def move_cursor(f): # <-header
    f.readline() # read one line of the file starting from the read cursor
    f.readline()

# with open("fruits.txt") as f:
#     # the cursor is at the beginning of the file
#     move_cursor(f)
#     # the cursor is at the beginning of the 3rd line
#     print(f.readline()) # this will read the 3rd line of the file

# 2. list_of_list(f)
# This function should read the contents of fruits.txt and return it in a list 
# of lists, with each inner list containing the name and quantity for a fruit.
# Expected Output: [["Apple", 5],["Orange", 10],["Banana", 3],["Kiwi", 15]]

def list_of_list(f):
    # skip the first two lines of the file
    move_cursor(f)
    # where is the read cursor? at the beginning of the 3rd line
    output = []
    for line in f:
        # intput: "Apple 5\n"
        # output: ["Apple","5"]
        element = line.split() # by default, split based on whitespaces " ", "     ", tab, a new line
                            # skip all the whitespaces
                            # the reture value of split() is a list
        # print(line) # for the print function, by default, it will add a new line character at the end
        # How to add a new element to a list?
        output.append(element) # append is a list method
    return output

with open("fruits.txt") as f:
    print(list_of_list(f))

# 3. sorted_fruit_quantity(f):
# This function should return a list containing the two highest quantity, 
# in descending order, for all fruits.
# [15, 10]

# 4. create_dict(f)
# This function should return a dictionary where key is the name of the fruit 
# and value is the quantity.
# {"Apple": 5, "Orange": 10, "Banana": 3, "Kiwi": 15}