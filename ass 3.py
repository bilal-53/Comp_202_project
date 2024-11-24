#Unchanging values
MAX_CHAR = 10000







def is_not_valid(string):
    """
    Checks if a string has any characters that are not letters or spaces.
    
    Parameters:
        string (str): The string we want to check.
        
    Returns:
        bool: False if all are letters or spaces.\
        True if there are other characters 
    
    Examples:
    
        >>> is_not_valid('Hello World')
        False
        
        >>> is_not_valid('asfg123 asdf')
        True
        
        >>> is_not_valid('wkwleoeee')
        False
    """
    #Go through each character in the input string
    for i in string:
        #Check if the character is not a lowercase letter,\
        #uppercase letter, or space
        if not ('a' <= i <= 'z' or 'A' <= i <= 'Z' or i == ' '):
            return True
        
    return False

def is_not_square(string):
    """
    Check if the length of the input string is not a perfect square.
    
    Parameters:
    string (str): The string we want to check
        
    Returns:
        bool: True if the length of the input string is not a perfect square, 
              False if it is a perfect square.
    
    Examples:
    
        >>> is_not_square('abcd')
        False
        
        >>> is_not_square('abcde') 
        True
        
        >>> is_not_square('abc')
        True
    """
    
    #Go through each character in the input string
    for i in range (1, len(string)+1):
        
        # Check if the square of i equals the length of the input string
        if len(string) == i * i:
            
            return False
        
    return True

    
        
def string2list(string):
    '''
    Convert a valid string into a 2D square list
    
    Parameters:
        string (str): Input string we want to convert

    Returns:
        output_list: 2D list of characters if the string is valid\
        empty list otherwise

    Examples:
    
        >>> string2list('Hello Bye')
        [['H', 'e', 'l'], ['l', 'o', ' '], ['B', 'y', 'e']]

        >>> string2list('Comp 202')
        []

        >>> string2list('C')
        [['C']]
    '''
    
    output_list = []
    invalid_string = is_not_valid(string)
    not_perfect_square = is_not_square(string)
    
    
    #Check if the string respects the constraints
    if invalid_string or not_perfect_square or\
       len(string) > MAX_CHAR:
        return output_list
    
    else:
        #Finds the size of the nested lists
        for i in range (1, len(string) + 1):
            if len(string) == i * i:
                size = i
        #Converts string into list        
        list_1 = list(string)
    
        # Build the 2D list
        for k in range (0, len(string), size):
            output_list.append(list_1[k:k + size])

    return output_list

def add_space(input_text):
    
    """
    Adds a space before any uppercase letter that is found between two\
    lowercase letters

    Parameters:
        input_text (str): The input text to modify.

    Returns:
        output_text (str) : Modified string with spaces added

    Examples:
    
        >>> add_space('HelloEveryone')
        'Hello Everyone'
        
        >>> add_space('HelloHOWareYou')
        'HelloHOWare You'
        
        >>> add_space('abcDefGhi')
        'abc Def Ghi'
    """
    
    output_text = ""
    
    #Traverses the string
    for i in range(len(input_text)):
        
        #Check if the current character(not the first or last one)\
        #is uppercase and is surrounded by lowercase letters
        
        if (i > 0 and 'a' <= input_text[i - 1] <= 'z' and\
            'A' <= input_text[i] <= 'Z' and\
            i < len(input_text) - 1 and 'a' <= input_text[i + 1] <= 'z'):
            output_text += ' '
            
        # Add the current character to output   
        output_text += input_text[i]  

    return output_text

def list2string(list_2D):
    """
    Converts a 2D list into a string, adding spaces when necessary
    
    Parameters:
    list_2D (list of lists): 2D list we want to convert to a string
        
    Returns:
    conv_str (str) : The converted string
    
    Examples:
    
        >>> list2string([['H', 'e', 'l'], ['l', 'o', ' '], ['B', 'y', 'e']])
        'Hello Bye'
        
        >>> list2string([['A', 'p'], ['p', 'l', 'e']])
        'Apple'
        
        >>> list2string([['H', 'e'], ['l', 'l', 'o']])
        'Hello'
    """
    string = ''
    
    #Traverses the 2D list
    for i in range (len(list_2D)):
        
        #Go through each character in the current sublist
        for j in range (len(list_2D[i])):
            string += list_2D[i][j]
            
    #Adds the necessary space characters        
    conv_str = add_space(string)
    
    return conv_str

def horizontal_flip(square_list_2D):
    """
    Flips a 2D square list horizontally
    
    Parameters:
        square_list_2D (list of lists): 2D square list we want to flip\
        horizontally.
        
    Returns:
        None: Modifies the input list directly.
    
    Examples:
    
        >>> input_list = [['B', 'I', 'H'], ['y', 'o', 'e'], ['e', ' ', 'l']]
        >>> horizontal_flip(input_list)
        >>> input_list
        [['H', 'I', 'B'], ['e', 'o', 'y'], ['l', ' ', 'e']]
        
        >>> input_list = [['C', 'O', 'M'], ['P', ' ', '2'], ['0', '2', ' ']]
        >>> horizontal_flip(input_list)
        >>> input_list
        [['M', 'O', 'C'], ['2', ' ', 'P'], [' ', '2', '0']]
        
        >>> input_list = [['C', 'O'], ['M', 'P']]
        >>> horizontal_flip(input_list)
        >>> input_list
        [['O', 'C'], ['P', 'M']]

    """
    # Traverses the 2D square list
    for i in range(len(square_list_2D)):
        
        # Go through each element up to the middle of the sublist
        for j in range(len(square_list_2D[i]) // 2):
            
            # Swap elements to flip the sublist horizontally
            square_list_2D[i][j], square_list_2D[i][-j - 1] =\
                              square_list_2D[i][-j - 1], square_list_2D[i][j]
            
            
def transpose(square_list_2D):
    """
    Transposes a 2D square list
    
    Parameters:
        square_list_2D (list of lists): A 2D square list to transpose.
        
    Returns:
        None: Modifies the input list directly.
    
    Examples:
    
        >>> input_list = [['H', 'I', 'B'], ['e', 'o', 'y'], ['l', ' ', 'e']]
        >>> transpose(input_list)
        >>> input_list
        [['H', 'e', 'l'], ['I', 'o', ' '], ['B', 'y', 'e']]
        
        >>> input_list = [['C', 'O', 'M'], ['P', ' ', '2'], ['0', '2', ' ']]
        >>> transpose(input_list)
        >>> input_list
        [['C', 'P', '0'], ['O', ' ', '2'], ['M', '2', ' ']]
        
        >>> input_list = [['C', 'O'], ['M', 'P']]
        >>> transpose(input_list)
        >>> input_list
        [['C', 'M'], ['O', 'P']]
    """
    # Traverses the 2D square list
    for i in range(len(square_list_2D)):
        
        for j in range(i, len(square_list_2D)):
            # Swap elements at [i][j] and [j][i] to transpose the list
            square_list_2D[i][j], square_list_2D[j][i] =\
                                  square_list_2D[j][i], square_list_2D[i][j]

def flip_list(square_list_2D):
    """
    Transforms a 2D square list by flipping it horizontally, 
    then transposing it.
    
    Parameters:
        square_list_2D (list of lists): A 2D square list to transform.
        
    Returns:
        None: Modifies the input list directly.
    
    Examples:
    
        >>> input_list = [['B', 'I', 'H'], ['y', 'o', 'e'], ['e', ' ', 'l']]
        >>> flip_list(input_list)
        >>> input_list
        [['H', 'e', 'l'], ['I', 'o', ' '], ['B', 'y', 'e']]
        
        >>> input_list = [['C', 'O', 'M'], ['P', ' ', '2'], ['0', '2', ' ']]
        >>> flip_list(input_list)
        >>> input_list
        [['M', '2', ' '], ['O', ' ', '2'], ['C', 'P', '0']]
        
        >>> input_list = [['C', 'O'], ['M', 'P']]
        >>> flip_list(input_list)
        >>> input_list
        [['O', 'P'], ['C', 'M']]
    """
    # First, flip the list horizontally
    horizontal_flip(square_list_2D)
    
    # Then, transpose the flipped list
    transpose(square_list_2D)
    
    
def decipher_code(input_string):
    """
    Deciphers a coded message by processing each sentence.
    
    Parameters:
        input_string (str): The string to decipher into a meaningful text
        
    Returns:
        output_string (str): The fully deciphered text
    
    Examples:
    
        >>>  secret = 'ttuoYrAtwoinLAundibKgSson.roelf ad YfImPAoitmr ucI\
        eoGAisrgoraO'
        >>> decipher_code(secret)
        'You Know About List And String It Is Official\
        You Are A Good Programmer'
        
        >>> decipher_code('LOL!')
        ''
        
        >>> decipher_code('BOUH!')
        ''
    """
    output_string = ""
    
    #Split the string into sentences
    sentences = input_string.split('.')  
    
    #The function processes each sentence at a time
    for sentence in sentences:
        
        # Only process valid sentences (invalid ones are ignored)
        if not is_not_valid(sentence):
            my_list = string2list(sentence) 
            flip_list(my_list)
            
            #Convert back the meaningful text into a string and\
            #add it to the output
            output_string += list2string(my_list)  

    return output_string