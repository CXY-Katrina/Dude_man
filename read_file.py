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
        # intput: "Apple 5\n" - string
        # output: ["Apple","5"] - list
        element = line.split() # by default, split based on whitespaces " ", "     ", tab, a new line
                            # skip all the whitespaces
                            # the reture value of split() is a list
        # print(line) # for the print function, by default, it will add a new line character at the end
        # How to add a new element to a list?
        output.append(element) # append is a list method
    return output

# with open("fruits.txt") as f:
#     print(list_of_list(f))

# 3. sorted_fruit_quantity(f):
# This function should return a list containing the two highest quantity, 
# in descending order, for all fruits.
# [15, 10]

# Define a function:
# 1. header of the function
# def function_name(input_name):
# 2. the description (We don't need to have it)
# 3. the body of the function
# Everything inside the body of the function should be indented

def sorted_fruit_quantity(f):
    """
    This function should return a list containing the two highest quantity, 
    in descending order, for all fruits.
    """
    # skip the header of the file
    move_cursor(f)
    # put all the quantities into a list
    # expected output: [5, 10, 3, 15]
        # read the file line by line
    output = []
    for line in f:
        line_list = line.split() # ["Apple","5"]
        output.append(int(line_list[1]))
    # sort the list in descending order
    # expected output: [15, 10, 5, 3]
    output.sort(reverse=True)
    # only select the highest two quantities in the list and return them
    # expected output: [15, 10]
    # slicing
    # Hint: ending pos is the index of the first element that I don't want to include
    # in the final result
    return output[0:2]

# '5' vs 5
# type
# '5' is a string
# 5 is a number

# print('5'>'25') # expected output: false
                # actual output: true
# '5' > '2'-> True
# 'apple'<'banana'->True
# print(5 < 25)

# print("cart"[0:3])

# what u have: [15, 10, 5, 3]
# what I want: [15, 10]

# with open("fruits.txt") as f:
#     print(sorted_fruit_quantity(f))

# 4. create_dict(f)
# This function should return a dictionary where key is the name of the fruit 
# and value is the quantity.
# {"Apple": 5, "Orange": 10, "Banana": 3, "Kiwi": 15}

def create_dict(f):
    # skip the header of the file
    move_cursor(f)

    output = {}
   
    # for loop - go through each line of the file
    for line in f:
        # "Apple 5\n" -> {"Apple": 5}
        # get rid of the new line character (\n)
        line = line.strip()
        # split "Apple 5" into two strings "Apple" "5"
        line_list = line.split() # ["Apple","5"]
        # convert "5" into an integer 5
        # the second element of line_list - line_list[1]
        quantity = int(line_list[1])
        # add this key value pair to the output
        # the name of the fruits - variable 
        # Q: how to get the first element of variable line_list?
        # A: line_list[0]
        output[line_list[0]] = quantity
    return output

with open("fruits.txt") as f:
    print(create_dict(f))

# git vs github
# control the logic vs UI of git

# d = {}
# d["Apple"] = 5
# print(d)

# strip()
# delete all the leading and trailing characters, by default, it will delete spaces
# print("      ap ple         ".strip())

# strip(string)
# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grtn") # a set of characters
# print(x)

# l = ["abc", "5"]
# print(l[1])