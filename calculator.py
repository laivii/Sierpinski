import png, time, random

#Calculates the coordinates for the next point (always 2/3ds of the distance between the two points)
def calculateNextOne (point1,point2):
    x = int(point1[0] + ((point2[0]-point1[0])*0.66))
    y = int(point1[1] + ((point2[1]-point1[1])*0.66))

    new_point = [x,y]

    return new_point

#This function returns the coordinates of the hexagons corner that is selected (later) by random number generator
def whichGon(number):
    match number:
        case 1:
            coordinates = [250,0]
            return coordinates
        case 2:
            coordinates = [750,0]
            return coordinates
        case 3:
            coordinates = [1000,433]
            return coordinates
        case 4:
            coordinates = [750,866]
            return coordinates
        case 5:
            coordinates = [250,866]
            return coordinates
        case 6:
            coordinates = [0,433]
            return coordinates

#Draws the picture
def drawPicture(coordinates):
    width = 1001
    height = 1001
    coords = coordinates
    
    img = []

    for y in range(height):
        row = ()
        print(f"On line: {y}", end="\r")
        for x in range(width):
            color = (255,255,255)
            for i in coords:
                if  y == i[1] and x == i[0]:
                    color = (0,0,0)
                    break
            row += color
        img.append(row)

    with open('gradient.png', 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)

def calculateCoordinates():
    aloitusPiste = [85, 286] #set a the first point (2/3 of 1 --> 6)
    coordinates = []

    #Calculates x amount of points so the picture starts to form
    for iteration in range(1, 50_000):
        reunaPiste = whichGon(random.randint(1,6))
        piste = calculateNextOne(aloitusPiste,reunaPiste)

        aloitusPiste = piste
        coordinates.append(piste)  

    return coordinates

coordinates = calculateCoordinates()

drawPicture(coordinates)