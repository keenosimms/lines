Write a function in this file called nine_lines that uses the function three_lines (provided below) to print a total of nine lines.

Now add a function named clear_screen that uses a combination of the functions nine_lines, three_lines, and new_line (provided below) to print a total of twenty-five lines. The last line of your program should call the function clear_screen.

The function three_lines and new_line are defined below so that you can see nested function calls. Also, to make counting “blank” lines visually easier, the print command inside new_line will print a dot at the beginning of the line:

def new_line():

print('.')
def three_lines():

new_line()

new_line()

new_line()
Must execute your script and paste the output produced into a document that you will submit along with your Python script. It is very helpful if you print a placeholder between the printing of 9 lines and the printing of 25 lines. It will make your output easier to read for your peer assessors. A placeholder can be output such as “Printing nine lines” or “Calling clearScreen()”.
