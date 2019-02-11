def new_line(): #defined one line, new_line
    print('.')

def three_lines():#defined three_lines
    new_line()    #nested function calls
    new_line()
    new_line()

def nine_lines(): #defined nine_lines 
    three_lines() #nested function calls
    three_lines()
    three_lines()

def clear_screen(): #defined clear_screen will print 25 lines
    nine_lines()    #nested function calls 
    nine_lines()
    three_lines()
    three_lines()
    new_line()

print("Program Will Now Print 25 Lines") 
    
clear_screen() #“Calling clearScreen()”.

#completed by Keeno Simms
#Saturday February 10th, 2019 8:27pm

    
