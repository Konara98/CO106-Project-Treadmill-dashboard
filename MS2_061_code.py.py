import math  #import math module
import datetime
import time



# To run program with custom parameters
# python E18_G_XXX.py --motor 4 --radius "0.09 m" --height "170 cm" --time "600 s" --weight "100 lb"

# To run program with default parameters
# python E18_G_XXX.py

import argparse


# Define your functions here

# Don't change the the code below this point
if __name__=="__main__":

    args=argparse.ArgumentParser()
    args.add_argument("--motor", type=int, dest="motor_rate", help="EXAMPLE: 3", default=3)
    args.add_argument("--radius", type=str, dest="radius", help="EXAMPLE: 8 cm", default="8 cm")
    args.add_argument("--weight", type=str, dest="weight", help="EXAMPLE: 50 kg", default="50 kg")
    args.add_argument("--height", type=str, dest="height", help="EXAMPLE: 63 in", default="63 in")
    
    args=args.parse_args()

# Don't change the the code above this point
    
    print(args.motor_rate)
    print(args.radius)
    print(args.weight)
    print(args.height)
    
    # you call the functions by passing above arguments
    # eg: 
    # speed = find_speed(args.motor_rate, args.radius)
    # or
    # find_speed(args.motor_rate, args.radius)
print('                        --------------------Treadmill---------------------')

while True:
    weight=args.weight
    #weight=input('Enter the Weight(kg/lbs):')              #input weight of the person in kilograms/lbs
    try:
        space=weight.find(' ')
        unit=weight[space+1:]
        weight=abs(float(weight[:space]))                   #error handling            
    except ValueError:
        print('Wrong value input')              
        continue
    except TypeError:
        print('Wrong input')
        continue        
    if unit=='kg':
        weight=weight
        break
    elif unit=='lbs':
        weight=weight/2.204
        break
    else:
        print('Wrong unit input')
        continue

while True:
    height=args.height
    #height=input('Enter the Height(cm/m/in):')            #input height of the person in centemeters/meters/inches
    try:
        space=height.find(' ')
        unit=height[space+1:]
        height=float(height[:space])                       #error handling                   
    except ValueError:
        print('Wrong value input')
        continue
    except TypeError:
        print('Wrong input')
        continue        
    if unit=='cm':
        height=height
        break
    elif unit=='m':
        height=height*100
        break
    elif unit=='in':
        height=height*2.54
        break
    else:
        print('Wrong unit input')
        continue

while True:
    radius=args.radius
    #radius=input('Radius of the mototr(cm/m/in):')      #input the radius of the motor in meters
    try:
        space=radius.find(' ')
        unit=radius[space+1:]
        radius=float(radius[:space])                     #error handling                    
    except ValueError:
        print('Wrong value input')
        continue
    except TypeError:
        print('Wrong input')
        continue        
    if unit=='m':
        radius=radius
        break
    elif unit=='cm':
        radius=radius/100
        break
    elif unit=='in':
        radius=radius*0.0254
        break
    else:
        print('Wrong unit input')
        continue

while True:
    try:
        rpm=args.motor_rate
        #rpm=abs(float(input('Enter the RPM value:')))        #input the rpm value                
    except ValueError :
        print('Wrong input, Enter a value')                   #error handling
    else:
        break
    
time_1=time.monotonic()                         #initial time

speed_mph=2*math.pi*rpm*radius*60*0.000621371   # calculate speed using radius and rpm value in mph

speed_ms=speed_mph*0.44704                      #convert speed mph to m/s

speed = speed_mph*26.8224                       #convert speed, mph to m/min for calculation

#grade varies with many parameters like inlclintion,temperature and enviroment etc..
#Generally we get 0-1% grade value of treadmill
grade=0.01

total_distance=0                                #initial total distance
total_calories_burnt=0                          #initial total calories
total_no_of_steps=0                             #initial total no of steps

total_duration=0

while True:
    time_2=time.monotonic()                     #find final time after one loop
    duration=float(time_2 - time_1)/60          #duration in minutes
    time_1=time.monotonic()                     #find initial time for one loop
    
    #above 3.7mph as running 
    if speed_mph  > 3.7:
        print('\nRunning.....')
        vo2 = (0.2*speed) +(0.9*speed*grade) + 3.5
        
    #below 3.7mph as walking
    else:
        print('\nWalking.....')
        vo2 = (0.1*speed) +(1.8*speed*grade) +3.5

    #oxygen consumption in mililiters per minute
    vo2=vo2*weight

    #oxygen consumption in liters per minute
    vo2=vo2/1000

    #convert oxygen consumption to calories
    #1L of oxygen = 5 calories (This is defined value)
    vo2=vo2*5

    #calories burnt during the considerable time
    calories_burnt=vo2*duration
    total_calories_burnt=total_calories_burnt + calories_burnt        #calculate total calories burnt

    distance=speed*duration                                 #calculate the distance in meters
    total_distance=total_distance + distance                #calculate total distance in meters 

    height_inches=height*0.393701                           #convert cemtemeters to inches
    average_stride_lenght=(height_inches*0.413)/12          #calculate average srtide lenght
    average_step_lenght=average_stride_lenght/2             #calculate average step lenght
    steps_per_meter=5280/(average_step_lenght*1609.344)     #calculate steps per meter
        
    no_of_steps=steps_per_meter*distance                    #calculate no.of steps
    total_no_of_steps=total_no_of_steps + no_of_steps       #calculate total no of steps

    print('\nSpeed(m/s):',int(speed_ms),'\nDistance(m):',int(total_distance),'\nCalories burnt:',int(total_calories_burnt),'cal','\nNO.of Steps:',round(total_no_of_steps))
    #output values


