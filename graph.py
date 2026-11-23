import matplotlib.pyplot as plt
from calculations import mean,read_csv
def converter(convert):
    converters=[]
    for i in convert:
        i=int(i)
        converters.append(i)
    return converters

def graph_1():
    data=read_csv('nokeep')
    #[0] [1] [2]
    year=converter(data[0])
    bus_passenger=converter(data[1])
    bus=converter(data[2])
    plt.plot(year,bus_passenger,color='blue',label='bus passengers')
    plt.plot(year,bus,color='red',label='bus')
    plt.title('Bus Passengers and Buses (2000–2012)')
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.legend()
    plt.show()

#loaded truck is 4
def graph_2():
    data=read_csv('nokeep')
    year=converter(data[0])
    loaded_truck=converter(data[4])
    average=mean(loaded_truck,[0,13])
    plt.bar(year, loaded_truck,color='red',label='loaded_truck')
    plt.axhline(y=average, color='blue')
    plt.yticks([100000,200000,300000,average,400000])
    plt.show()


