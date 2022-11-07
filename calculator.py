#import math
import random

def calculateNextOne (point1,point2):
    x = point1[0] + ((point2[0]-point1[0])*0.66)
    y = point1[1] + ((point2[1]-point1[1])*0.66)

    new_point = [x,y]

    return new_point

def whichGon(number):
    match number:
        case 1:
            coordinates = [2.5,0]
            return coordinates
        case 2:
            coordinates = [7.5,0]
            return coordinates
        case 3:
            coordinates = [10,4.33]
            return coordinates
        case 4:
            coordinates = [7.5,8.66]
            return coordinates
        case 5:
            coordinates = [2.5,8.66]
            return coordinates
        case 6:
            coordinates = [0,4.33]
            return coordinates

aloitusPiste = [0.85, 2.86]

for iteration in range(1, 10):
    reunaPiste = whichGon(random.randint(1,6))
    print("Alussa: ",aloitusPiste,reunaPiste)

    piste = calculateNextOne(aloitusPiste,reunaPiste)

    aloitusPiste = piste
    print("Uusipiste: ",aloitusPiste)