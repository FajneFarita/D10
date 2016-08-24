#!/usr/bin/env python3

"""Write a program that given a text file will create a new text file 
in which all the lines from the original file are numbered from 1 to n 
(where n is the number of lines in the file). [use small.txt]
Ex.
old file:
We are not what we should be
We are not what we need to be
But at least we are not what we used to be
  	  -- Football Coach
new file:
1 We are not what we should be
2 We are not what we need to be
3 But at least we are not what we used to be
4  -- Football Coach
"""

def read():
	with open("small.txt", 'r') as text:
		list_lines = text.readlines()
		for line in list_lines:
			line.strip("\n")
		return list_lines[:-1]


def numbered_lines(lines):
	numbered = [pair for pair in enumerate(lines, start=1)]
	return numbered

def write(numbered):
	with open("small_new.txt", 'w') as file:
		for item in numbered:
			file.write(str(item[0]) + " " + str(item[1]) + "\n")


def main():
    lines = read()
    numbered = numbered_lines(lines)
    write(numbered)


if __name__ == "__main__":
    main()
