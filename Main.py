#!/usr/bin/python
"""Main module runs the program
    which prints the input, checks
    that the DFA is in proper format,
    and prints whether the DFA is
    empty or not empty.
"""
from graph import Graph



class Main():



    def main(self):
        """Run the process_dfa function
            on files that are specified here.
        Parameters:
            None
        Returns:
            None
        """

        # Create a list to store the file names.
        file_list = []

        # Specify files to be tested.
        file_list.append("test1.txt")
        file_list.append("test2.txt")
        file_list.append("test3.txt")
        file_list.append("test4.txt")
        file_list.append("test5.txt")
        file_list.append("test6.txt")
        file_list.append("test7.txt")
        file_list.append("test8.txt")
        file_list.append("test9.txt")

        # Run process_dfa on each file
        for file in file_list:
            Main.process_dfa(Main, file)



    def process_dfa(self, file_name):
        """Check that the DFA formal description
            is correctly formatted, convert it to a
            graph, and determine if the DFA is
            empty or not empty.
        Parameters:
            file_name: name of the file containing
                the formal description for the DFA.
        Returns:
            True if the DFA is empty.
            False if the DFA is not empty.
        """

        g = Graph()

        # Print the file name at the top of each test.
        print("File: " + file_name)

        # Only proceed if the input file is correctly formatted.
        # Otherwise, print a separator and return False.
        if (g.correct_file(file_name)):
            input_list = g.process_input(file_name)
            dfa_graph = g.create_graph(input_list)
            dfa_empty = g.determine_empty_dfa(input_list, dfa_graph)

            if (dfa_empty):
                print("The DFA is empty.")
                print("------------------------------")
                return True
            else:
                print("The DFA is not empty.")
                print("------------------------------")
                return False
        else:
            print("------------------------------")
            return False



if __name__ == "__main__":
        Main.main(Main)
        input('Press ENTER to exit.')