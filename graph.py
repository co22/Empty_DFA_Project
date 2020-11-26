"""Graph module contains functions for:
    Verifying a file is in the correct format.
    Creating a list of the states, alphabets,
        and transitions from the input.
    Creating a graph of a DFA.
    Checking if a path exists between two states.
    Determining if a DFA is empty.
"""
import DfaInput
import re



class Graph():



    def correct_file(self, file_name):
        """Verify that the input is in the form
            of a DFA formal description.
        Parameters:
            file_name: name of the file containing
                the formal description for the DFA.
        Returns:
            True if the input is correctly formatted.
            False if the input is incorrectly formatted.
        """

        # Read input from the file and print the input.
        dfa_input = DfaInput.Input()
        input_list = dfa_input.read_input(file_name)
        print("Input: \n")
        dfa_input.print_input(input_list)

        # Check the input format.
        if (dfa_input.in_correct_format(input_list)):
            print("Input is in the correct format.")
            return True
        else:
            print("Input is not in the correct format.")
            return False



    def process_input(self, file_name):
        """Retrieve the states, alphabet, transitions,
            start state, and accept states for the DFA
            and store each category into a list.
        Parameters:
            file_name: name of the file containing
                the formal description for the DFA.
        Returns:
            The newly created list containing a list
            of states, a list of alphabets, a list of
            transitions, a list for the start state, and
            a list of accept states.
        """

        dfa_input = DfaInput.Input()
        input_list = dfa_input.read_input(file_name)
        return dfa_input.split_input(input_list)



    """External Citation:
        Date: 24 November 2020
        Resource: https://www.tutorialspoint.com/
                python_data_structure/python_graphs.htm#:~:
                text=A%20graph%20can%20be%20easily,
                the%20values%20in%20the%20dictionary
        Usage: I learned how to represent graphs in
            Python using dictionaries.
    """
    def create_graph(self, input_list):
        """Create a graph representation of the DFA
            using a dictionary. Set each key to one
            of the DFA's states and create a list of 
            values for each key that contains the states
            that key transitions into.
        Parameters:
            input_list: the list containing lists of all
                of the DFA's states, alphabet, transitions,
                start state, and set of accept states.
        Returns:
            Graph representation of the DFA.
        """

        # Create an empty dictionary for the graph,
        # read the list of states and transitions
        # and store them in variables.
        dfa_graph = {}
        list_of_states = input_list[0]
        list_of_transitions = input_list[2]

        # Create an empty list for each key.
        for state in list_of_states:
            dfa_graph[state] = []

        # For each transition, set the key
        # of the dictionary to the state that
        # the transition is coming from and
        # add the state that the transition is
        # going into to a list.
        for j in list_of_transitions:
            temp_list = re.findall("q[0-9]", j)
            temp_state = temp_list[0]
            temp_edge = temp_list[1]
            dfa_graph[temp_state].append(temp_edge)
        
        return dfa_graph



    """External Citation:
        Date: 24 November 2020
        Resource: https://www.geeksforgeeks.org/find-if-there-is-
            a-path-between-two-vertices-in-a-given-graph/
        Usage: I modified code for a BFS from this post.
    """
    def path_exists(self, dfa_graph, start, end):
        """Determine if there is a path from one state to another.
        Parameters:
            dfa_graph: graph representation of the DFA. The
                representation is stored in a dictionary where
                there is one key for each state and the values
                for each key represent states with transitions
                from the key.
            start: the DFA's starting state.
            end: the state to check if a path exists from the
            start state.
        Returns:
            True if a path exists from start to end.
            False if no path exists start to end.
        """

        # Create a queue and a dictionary
        # to keep track of states as they
        # are processed and mark them.
        # Unmark all states. Add the start state
        # to the queue and mark it.
        queue = []
        marked = {}

        for state in dfa_graph:
            marked[state] = False
        queue.append(start)
        marked[start] = True

        # While the queue is not empty, pop the
        # current state. If it matches the end
        # state, then a path exists. Otherwise,
        # find all of the state with transitions
        # into them from the current state, add
        # them to the queue, and mark them.
        while queue:
            current = queue.pop(0)
            if current == end:
                return True
            for edge in dfa_graph[current]:
                if marked[edge] == False:
                    queue.append(edge)
                    marked[edge] = True

        return False



    def determine_empty_dfa(self, input_list, dfa_graph):
        """Determine if a DFA is empty or not.
        Parameters:
            input_list: the list containing lists of all
                of the DFA's states, alphabet, transitions,
                start state, and set of accept states.
            dfa_graph: graph representation of the DFA.
        Returns:
            True if the DFA is empty.
            False if the DFA is not empty.
        """

        # Retrieve the start state and the set of accept
        # states from the input_list.
        start_list = input_list[3]
        start_state = start_list[0]
        list_of_accept_states = input_list[4]

        # If there are no accept states then the DFA is empty.
        if list_of_accept_states == []:
            return True

        # For each accept state, check if any state with a
        # valid path matches the accept state. If an accept
        # state with a valid path exists, then the DFA
        # is not empty.
        for accept_state in list_of_accept_states:
            for list_of_edges in dfa_graph.values():
                for edge in list_of_edges:
                    if (accept_state == edge and
                    self.path_exists(dfa_graph, start_state, accept_state)):
                        return False

        return True