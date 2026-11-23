'''
User requirment:    1) show loaded truck for all year from 2000- 12012
                    2)Ask user to choose a transport category, and display the mean, maximum and the year of maximum 
                    3) ask user to choose one transport category and calculate how much number increase or decrease from one year to the next throughout the years
                    4) Generate two graph
                        1)A line graph showing bus passenger and bus on the graph
                        2)A bar graph with 13 graph ine for each year and a line showing the mean number of loaded trucks
'''
from validator import number_valid
from options import option_1,option_2,option_3,option_4_1,option_4_2
import sys

print('                 Menu                ')
print('             Border crossing vehicles                ')
print('======================================================')
print('1.Display Loaded Trucks for all years')
print('2.Calculate Mean and Maximum (2001-2006)')
print('3.Calculate Year to Year percentage change')
print('4.Generate graph')

option= {1:option_1,2:option_2,3:option_3}

while True:
    checker=False
    choice=input('Please select your option(1,2,3,4,press q to quit): ')
    if choice.lower()  == 'q':
        print('Goodbye :) ')
        sys.exit()
    checker=number_valid(choice)
    if checker and 0 < int(choice) <= 4:
        if int(choice) != 4:
            choice=int(choice)
            option[choice]()
        else:   
                checking = False
                while checking == False:
                    task_4={'1':option_4_1,'2':option_4_2}
                    print("1. Bus Passengers and Buses")
                    print("2. Loaded Trucks")
                    decisions = input("Choose a graph (1 or 2): ")
                    if decisions in task_4:
                        task_4[decisions](decisions)
                        checking = True
                    else:
                        print('Not valid, please re-enter')
    else:
         print('Number out of range, please retry')