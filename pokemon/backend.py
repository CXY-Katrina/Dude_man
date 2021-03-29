import const


def get_pokemon_stats():
    """Reads the data contained in a pokemon data file and parses it into
    several data structures.

    Args:
        None

    Returns: a tuple of:
        -a dict where:
            -each key is a pokemon name (str)
            -each value is a tuple of the following stats:
                -pokemon name (str)
                -species_id (int)
                -height (float)
                -weight (float)
                -type_1 (str)
                -type_2 (str)
                -url_image (str)
                -generation_id (int)
                -evolves_from_species_id (str)
        -a dict where:
            -each key is a pokemon species_id (int)
            -each value is the corresponding pokemon name (str)
        -a list of all pokemon names (strs)
        -a dict where:
            -each key is a pokemon type (str). Note that type_1 and type_2
            entries are all considered types. There should be no special
            treatment for the type NA; it is considered a type as well.
            -each value is a list of all pokemon names (strs) that fall into
            the corresponding type
    """
    name_to_stats = {}
    id_to_name = {}
    names = []
    pokemon_by_type = {}

    # tuple is created using ()
    # we can't modify a tuple after initializing it
    # but we can modify a list

    # Write your code below.
    # open the file
    filename = const.DATA_FILENAME
    with open(filename) as f:
    # get rid of the header
    # for loop each line in the file
    # get all the fields
    # put them into data structures

    # Write your code above.

    return name_to_stats, id_to_name, names, pokemon_by_type


def parse_header(f):
    """Parses the header and builds a dict mapping column name to index

    Args:
        f: a freshly opened file in the format of pokemon.csv

    Returns:
        a dict where:
            -each key is one of:
                'pokemon', 'species_id', 'height', 'weight', 'type_1',
                'type_2', 'url_image', 'generation_id',
                'evolves_from_species_id'
            -each value is the index of the corresponding key in the CSV file
                starting from column 0.
                eg. If 'pokemon' is in the second column, then its index will
                be 1. If 'species_id' is the third column, then its index will
                be 2.
    """
    columns = ['pokemon', 'species_id', 'height', 'weight', 'type_1', 'type_2',
               'url_image', 'generation_id', 'evolves_from_species_id']
    result = {}

    # Write your code below.
    # get the header - read the first line of the file
    header = f.readline() # string
    # get rid of the new line character at the end - strip()
    header = header.strip()
    # convert the header into a list of strings - split()
    header = header.split(const.SEP) # by default, it will split based on whitespaces
    # get the index of each column
    for element in columns:
        # I want to know the index of it inside header list
        # index is a method of list
        # add the element and the index into the dictionary
        result[element] = header.index(element)

    # expected output
    # {'pokemon': 1, 'species_id': 2} 9 key-value pair
    return result

if __name__ == '__main__':
    # put this file in your directory along with this lab file
    filename = const.DATA_FILENAME

    # Call the functions and print the results here.
    # For example, this will print all the lines of the file other than the
    # header.
    with open(filename) as f:
        print(parse_header(f))
        print('--------------------------------')