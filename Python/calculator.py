import png, time, random

#Calculates the coordinates for the next point (always 2/3rds of the distance between the two points towards the end point)
def calculateNextOne (point1,point2):
    #Calculating the coordinates x and y for the next point by using the coordinates of our starting and end point
    x = int(point1[0] + ((point2[0]-point1[0])*0.66))
    y = int(point1[1] + ((point2[1]-point1[1])*0.66))

    new_point = [x,y] #Saving them together as a list

    return new_point #Returning it so it can be used later

#This function returns the coordinates of the hexagons corners, the corner is selected by random number generator
def whichCorner(corner):
    match corner:
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

#Calculates the coordinates and saves them to a list that the function will return for later use
def calculateCoordinates():
    startingPoint = [85, 286] #set a the first point (2/3 of 1 --> 6)
    coordinates = [] #Formatting the list where we will save our coordinates to

    #Calculates x amount of points so the picture starts to form
    for iteration in range(1, 15_000):
        cornerPoint = whichCorner(random.randint(1,6)) #Getting the corner by random number in between 1 - 6.
        point = calculateNextOne(startingPoint,cornerPoint)

        startingPoint = point #Changing the value of the "startingPoint"
        coordinates.append(point)  #Saving the coordinates to a list

    return coordinates

#Draws the picture by using the coordinates that we have collected
def drawPicture(coordinates):
    #Here we assign the size of the picture
    width = 1001 
    height = 1001

    #Here we take the lsit of coordinates so we can use them
    coords = coordinates
    
    #Formatting the picture so it can be printed (starting it as empty list, here we will collect the information of the color of the pixel)
    img = []

    #This loop goes through our list of coordinates and assign the color for each individual pixel and saves that information to the "img" list
    for y in range(height):
        row = () #Forms a tuple where we assign rows
        print(f"On line: {y}", end="\r")
        for x in range(width):
            color = (255,255,255) #Defaukt color for the pixels
            for i in coords:
                #This one checks if the coordinate is in our list
                if  y == i[1] and x == i[0]:
                    color = (0,0,0) #If the coordinate is in the list we change the color of that pixel to black
                    break
            row += color #this assigns the color
        img.append(row) #Here we append the row to the "row" tuple

    #Here we form the actual picture
    with open('gradient.png', 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)

#Assigning the calculated coordinates here so they can be used
coordinates = calculateCoordinates()

#Forming the picture
drawPicture(coordinates)