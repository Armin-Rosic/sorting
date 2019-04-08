
#!/usr/bin/env python3

import sys 
import re 

def generator_sort(input_list):
    '''Integer sorting function that leverages generators.

    Args:
        input_list: list of int

    Return:
        sorted_list: list of int
    '''

     #Populating a list with tuples of type (int , <generator object>)
     #Each <generator object> is populated by the placeholder value None, {integer} times 
    tup_list = [(integer, (i for i in [None]*integer)) for integer in input_list]

    sorted_list = [] 
    deletions = [] #Utility list to keep track of empty generators in each loop 

     #The main sorting loop where each tuple's generator yields once per loop
     #Tuples are removed from tup_list once their generator is empty
    while (tup_list != []): #Loop until all generators are empty
        for tup in tup_list: 
            try:    
                next(tup[1]) 
            except: 
                sorted_list.append(tup[0]) 
                deletions.append(tup) 
        for i in deletions: 
            tup_list.remove(i) 
        deletions = [] 
     
    return sorted_list 


if __name__ == "__main__":
    '''
    If used on the Unix Command-Line, the sorting functionality can be accesed in two ways:

    1. As a part of a Unix pipe 
    2. As a Command-Line program accepting integers as Command-Line arguments

    Case 1:
        -The program will process incoming data from stdin.
        -The delimiter of the incoming data is specified as Command-Line argument 1
        -The desired output delimiter is specified as Command-Line argument 2
        (example 1) ... (CSV input, space-delimited output)
        $ cat dataFile | python3 gensort.py ',' ' '
        int1 int2 int3 ...

        (example 2) ... (space-delimited input, semi-colon-delimited output)
        $ cat dataFile | python3 gensort ' ' ':'
        int1:int2:int3 ...

    Case 2:
        -The program will sort integers provided as arguments
        (example)
        $python3 gensort.py 4 2 3 1 3
        1 2 3 3 4
    '''
    
    #-------------Case 1---------------- 
    if not sys.stdin.isatty(): #Checking if stdin is full
        input_delimiter = sys.argv[1]
        output_delimiter = sys.argv[2]
        input_stream = []
        output_string = ""
        for line in sys.stdin:
            #Splitting each line by the specified input data-file delimiter 
            list_of_split_lines = re.split(f"{input_delimiter}",line)

            #removing trailing newline character for last entry 
            list_of_split_lines[-1] = list_of_split_lines[-1].rstrip()

            try:
                input_stream.extend([int(i) for i in list_of_split_lines])
            except ValueError as e:
                error_message, error_cause = str(e).split(':')
                print('\n')
                print(f"Error: 'gensort.py' expected a stream of integers delimited by the specified delimiter '{input_delimiter}'" + '\n')
                print(f"Encountered: {error_cause}" + '\n')
                sys.exit(0)
            

        sorted_list = generator_sort(input_stream)
        output_string = f"{output_delimiter}".join(str(integer) for integer in sorted_list)
        sys.stdout.write(output_string + '\n')

    #-------------Case 2---------------- 
    else:
        output_string = ""
        try:
            input_stream = [int(arg) for arg in sys.argv[1:]]
        except ValueError as e:
            error_message, error_cause = str(e).split(':')
            print('\n')
            print(f"Error: 'gensort.py' expected integer Command-Line arguments" + '\n')
            print(f"Encountered: {error_cause}" + '\n')
            sys.exit(0) 
        
        sorted_list = generator_sort(input_stream)
        output_string = ' '.join(str(integer) for integer in sorted_list)
        sys.stdout.write(output_string + '\n')