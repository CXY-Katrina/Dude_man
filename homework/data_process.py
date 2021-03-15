def move_cursor(f):
    '''Given an open file f, reads past its three-line header.

    Args:
        f: a freshly opened file in the format of the file alkaline_metals.txt
    '''
    pass  


def list_of_list(f):
    '''Reads the contents of alkaline_metals.txt and returns it in a list
    of lists, with each inner list containing the name, atomic number, and
    atomic weight for an element. (Hint: Use string.split.)

    Args:
        f: a freshly opened file in the format of the file alkaline_metals.txt
    '''
    pass
    

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
    pass  

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
    pass


if __name__ == '__main__':
    # put this file in your directory along with this lab file
    filename = 'alkaline_metals.txt'

    # Call the functions and print the results here.
    # For example, this will print all the lines of the file other than the
    # header.
    with open(filename) as f:
        move_cursor(f)
        for line in f:
            print(line.strip())
        print('--------------------------------')
        
    # similarly, call the rest of the functions