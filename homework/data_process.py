def move_cursor(f):
    '''Given an open file f, reads past its evolution header.

    Args:
        f: a freshly opened file in the format of the file alkaline_metals.txt
    '''
    f.readline()
    f.readline()
    f.readline()


def list_of_list(f):
    '''Reads the contents of alkaline_metals.txt and returns it in a list
    of lists, with each inner list containing the name, atomic number, and
    atomic weight for an element. (Hint: Use string.split.)

    Args:
        f: a freshly opened file in the format of the file alkaline_metals.txt
    '''

    # expected output:
    # [["beryllium", 4, 9.012], ["magnesium", 12, 24.305]]
    move_cursor(f)
    output = []
    for line in f:
        element = line.split()
        output.append(element)
    return output

def sorted_atomic_weights(f):
    '''Returns a list containing the three highest atomic weights(represented as
    floats), in descending order, for all metals.

    Args:
        f: a freshly opened file in the format of the file alkaline_metals.txt
    Hint:
        Use split() to create a list of each line
        Use sort() function to sort elements of a list
        Be mindful of the types of data
        Once you assign melements to a list; you need to use float() function
        to convert str type to float type. Else, elements won't get sorted
    '''
    # step 1: skip the header -> call move_cursor
    move_cursor(f)
    # step 2: put all the weights into a list
    output = []
    for line in f:
      line_list = line.split()  # ['beryllium', '4', '9.012']
      output.append(float(line_list[2]))
    # step 3: sort the list in descending order
    output.sort(reverse=True)
    # step 4: select the highest three weights -> slicing
    # step 5: return the output
    return output[0:3]

def create_dict(f):
    '''Returns a dictionary where key is the name of the metal and value
    is the atomic weight.

    Args:
        f: a freshly opened file in the format of the file alkaline_metals.txt
    Hint:
        Multiple ways to solve this.
        One way:
        Create a list first using list_of_list(f)
        Then assign first element as key and third element as value
    '''
    # step 1: skip the header
    move_cursor(f)
    # step 2: initialize an empty dictionary {}
    output = {}
    # step 3: go through each line of the file -> for loop
        # get rid of the new line character (\n)
        # split the elements based on whitespaces
        # get the name of the metal and the weight
        # put the name and weight pair into a dictionary
        for line in f:
            line_list = line.split()    # the format of line_list [name, number, weights]
            # indexing
            name = line_list[0]
            # Homework: get the third element of line_list
            # weights = 
            # To add a key-value pair into a dictionary:
            # dictionary_name[key] = value
            # in our case, key is the name, value is the weights

    # step 4: return the dictionary


if __name__ == '__main__':
    # put this file in your directory along with this lab file
    filename = './alkaline_metals.txt'

    # Call the functions and print the results here.
    # For example, this will print all the lines of the file other than the
    # header.
    with open(filename) as f:
        move_cursor(f)
        for line in f:
            print(line.strip())
        print('--------------------------------')

    # similarly, call the rest of the functions
    with open(filename) as f:
        print(list_of_list(f))
        print('--------------------------------')
    
    with open(filename) as f:
        print(sorted_atomic_weights(f))
        print('--------------------------------')