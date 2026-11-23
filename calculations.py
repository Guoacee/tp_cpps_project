import csv
from validator import number_valid

def percentage_change(initial,new):
    return ((new-initial)/initial)*100

def list_finder(keep_column):
    selected=transport_selection()
    data=read_csv(keep_column)
    for row in data:
        if selected in row:
            target = row  # try to find where is the lsit belonging to bus/personal vehecle or truck based on user input
            return data,target,selected

def read_csv(result):
    with open('code/5_6_brdrxingusc_dataset.csv','r') as file:
        reader = csv.reader(file)
        data = list(reader)
        if result == 'nokeep':
            for i in range(5):   #removes the first column of type bus passenger bus personal vehicles loaded truck)
                data[i].pop(0)
            return data
        elif result == 'keep':
            return data

def mean(target,list_range):
    total=0
    range=0
    start=list_range[0]
    stop=list_range[1]
    for i in target[start:stop]:
        i=int(i)
        total+=i
        range+=1
    mean = total/range
    return mean

def transport_selection():
    while True:
        checker=False
        select={1:'Buses',2:'Personal Vehicles',3:'Loaded Trucks'}
        selection=input('Select border-crossing transport (1 for bus, 2 for personal vehicles, 3 for loaded trucks): ')
        checker=number_valid(selection)
        if checker == True and 0< int(selection) <=3:
            selection=int(selection)
            return select[selection]
        else:
            print('invalid please re-enter.')