"""DfaInput module contains functions for:
    Reading the first five lines of input
        from a file.
    Printing the input from input_list format.
    Splitting the input into lists containing
        the states, alphabet symbols, and
        transitions.
    Verifying that each line from the input
        is in the proper format.
"""
import re



class Input():



    def read_input(self, file_name):
        """Open a file, read the first
            five lines of input, and close
            the file. Save each line of input
            individually in a list.
        Parameters:
            file_name: name of the file containing
                the formal description for the DFA.
        Returns:
            A list containing the separated input lines.
        """

        file = open(file_name, "r")
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        line4 = file.readline()
        line5 = file.readline()
        file.close()

        input_list = [line1, line2, line3, line4, line5]

        return input_list



    def print_input(self, input_list):
        """Print the input from the input list.
        Parameters:
            input_list: list containing the 5 lines of input
                read from the file.
        Returns:
            None
        """

        # For each line in the input list, print the line 
        # without extra newline spacing. Print a newline
        # at the end.
        for line in input_list:
            print(line, end = '')
        print('\n')

    

    def split_input(self, input_list):
        """Create a list containing a list of states, a 
            list of alphabet symbols, a list of transitions,
            a list with the starting state, and a list of
            accept states.
        Parameters:
            input_list: list containing the 5 lines of input
                read from the file.
        Returns:
            The new list.
        """

        # Retrieve each line from the input list.
        line1 = input_list[0]
        line2 = input_list[1]
        line3 = input_list[2]
        line4 = input_list[3]
        line5 = input_list[4]

        state = re.compile("q[0-9]") # what to consider a state

        # Get the states, alphabet symbols, and transitions
        states = re.findall(state, line1)
        alphabet = re.findall("[a-z0-9]", line2)
        transitions = re.findall("q[0-9]\sx\s[a-z0-9]\s=\sq[0-9]", line3)
        start = re.findall(state, line4)
        accept = re.findall(state, line5)

        split_list = [states, alphabet, transitions, start, accept]

        return split_list

    

    """External Citation:
        Date: 24 November 2020
        Resources: 
            https://www.w3schools.com/python/python_dictionaries.asp
            CS 357 Regex Lab
        Usage: I looked up the regex expression rules.
    """
    def in_correct_format(self, input_list):
        """Check each line of the input list
            to make sure it matches the format.
        Parameters:
            input_list: list containing the 5 lines of input
                read from the file.
        Returns:
            True if all five input lines match.
            False if one or more lines do not match.
        """

        # Retrieve each line from the input_list.
        line1 = input_list[0]
        line2 = input_list[1]
        line3 = input_list[2]
        line4 = input_list[3]
        line5 = input_list[4]

        # Specify the format that each line should match.
        test_line1 = re.compile("^{(q[0-9],\s)*(q[0-9])+}$")
        test_line2 = re.compile("^{([a-z0-9],\s)*([a-z0-9])+}$")
        test_line3 = re.compile("^((q[0-9]\sx\s[a-z0-9]\s=\sq[0-9];\s)*)((q[0-9]\sx\s[a-z0-9]\s=\sq[0-9])+)$|^$")
        test_line4 = re.compile("^q[0-9]$")
        test_line5 = re.compile("^{(q[0-9],\s)*(q[0-9])+}$|^{}$")

        # Check if the lines match the format.
        line1_correct = test_line1.match(line1)
        line2_correct = test_line2.match(line2)
        line3_correct = test_line3.match(line3)
        line4_correct = test_line4.match(line4)
        line5_correct = test_line5.match(line5)

        return True if (line1_correct and line2_correct and line3_correct
        and line4_correct and line5_correct) else False