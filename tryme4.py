def new_line(): 
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()

def nine_lines(): #defined nine lines using function three lines 
    three_lines() #nested function
    three_lines()
    three_lines()

def clear_screen(): #defined clear_lines using functions nine_lines, three_lines
    nine_lines()    #nested function 
    nine_lines()
    three_lines()
    three_lines()
    new_line()

print ("Line 1")
print ("now printing 25 black lines")
    
clear_screen()

#lesson completed by Keeno Simms
# Saturday February 9th, 2019 7:07pm

    
