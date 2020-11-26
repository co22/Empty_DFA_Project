This program determines whether the language for a DFA is empty or not empty.

Input File:
An input file for the program should include five lines representing the formal description of a DFA.
The input should be a .txt file.

Input Format:
{Q} # States in the DFA
{∑} # The DFA's alphabet
{δ} # The DFA's transitions
q0 # The DFA's start state
{F} # The DFA's accepting states

Example Input:
{q0, q1}
{a, b}
q0 x a = q1; q0 x b = q0; q1 x a = q1; q1 x b = q0
q0
{q1}

Usage:
The input files can be changed in the main() function found in Main.py.
Under # Specify files to be tested, files can be appended to the list of input files.
The program can be run from Main.py.