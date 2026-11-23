
from calculations import percentage_change,list_finder,read_csv,mean,transport_selection
from graph import graph_1, graph_2



def option_1():
        data=read_csv('nokeep')
        for index,year in enumerate(data[0]):
            print(f'The year {year} have {data[4][index]} trucks')

#['Personal Vehicles', '980130', '1012592', '1039135', '999836', '1001278', '973706', '973957', '1022895', '948008', '1040154', '1029593', '1054081', '1138536'] example for option_3
#['Type', '2000',     '2001', '2002',     '2003', '   2004', '    2005', '2006', '    2007', '2008', '    2009', '    2010', '2011',      '2012']
# 2001 -2006 index is 2-8


def option_2():
    #finding the mean number
    data,target,selected=list_finder('keep')
    total=0
    max_number=0
    means=mean(target,[2,8])
    #finding max number
    for k in target[2:8]:
        k=int(k)
        if k > max_number:
            max_number = k
    year_index = target.index(str(max_number))
    year=data[0][year_index]
    print(f'The mean number for {selected} is {means:.2f} and the max number is {max_number} from the year {year}')    

'''
['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012']
['11728','10374', '10415', '11290', '8345', '8465', '8317', '8124', '8418', '8565', '8980', '9544', '9935']
'''



def option_3():
    data,target,selected=list_finder('keep')
    comparison = dict(zip(data[0],target))
    del comparison['Type']
    initial=comparison['2000']
    initial=int(initial)
    previous_key = '2000'
    del comparison['2000']

    for keys,i in comparison.items():
        i=int(i)
        percentage=percentage_change(initial,i)
        print(f'There is a {percentage:.2f} percent change from year {previous_key} to {keys}')
        initial = i
        previous_key = keys

def option_4_1(decision):
    return graph_1()

def option_4_2(decision):
    return graph_2()