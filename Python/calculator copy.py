import png, time, random

#Calculates the coordinates for the next point (always 2/3rds of the distance between the two points towards the end point)
def calculate_next_point (point1,point2):
    #Calculating the coordinates x and y for the next point by using the coordinates of our starting and end point
    x = int(point1[0] + ((point2[0]-point1[0])*0.66))
    y = int(point1[1] + ((point2[1]-point1[1])*0.66))

    new_point = [x,y] #Saving them together as a list

    return new_point #Returning it so it can be used later

#This function returns the coordinates of the hexagons corners, the corner is selected by random number generator
def which_corner(corner):
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
def calculate_coordinates():
    starting_point = [85, 286]  # Set the first point
    coordinates = set()  # Initialize an empty set to store coordinates

    # Calculate x amount of points so the picture starts to form
    for _ in range(1, 15_000):
        corner_point = which_corner(random.randint(1, 6))  # Get the corner by a random number between 1 and 6
        point = calculate_next_point(starting_point, corner_point)

        starting_point = point  # Update the starting point
        coordinates.add(tuple(point))  # Save the coordinates as a tuple to the set

    return coordinates

#Draws the picture by using the coordinates that we have collected
def draw_picture(coordinates):
    #Here we assign the size of the picture
    width = 1001 
    height = 1001

    #Here we take the lsit of coordinates so we can use them
    coords = coordinates
    
    #Formatting the picture so it can be printed (starting it as empty list, here we will collect the information of the color of the pixel)
    img = []

    #This loop goes through our list of coordinates and assign the color for each individual pixel and saves that information to the "img" list
    for y in range(height):
        print(f"On line: {y}", end="\r")  # Printing progress

        row = [
            (0, 0, 0) if (x, y) in coords else (255, 255, 255)
            for x in range(width)
        ]

        img.append(row)

    #Here we form the actual picture
    with open('gradient.png', 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)

#Assigning the calculated coordinates here so they can be used
coordinates = calculate_coordinates()

#Forming the picture
draw_picture(coordinates)