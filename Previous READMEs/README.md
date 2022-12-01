# Project for drawning Sierpinski-Hexagon

### Makers:
* Viivi @laivii
* And a bit help gotten from Ville @Vsimpro

## This is a personal project out of love for Mathematics

This project was to make a code for formimg a picture of the Sierpinski Hexagon.
It needs a lot of optimization at it's current state (8.11.22), but it forms a nice picture in a manageable time with 10_000 points drawn.

The Idea of the Sierpinski Hexagon also known as N-flake is that we take a random destination point of one of the hexagons corners and draw a point to the 2/3rds of the destination towards the end point. The picture forms always the same way eventhough the order of the points is always totally random. 

Heres a link to a video on Tik Tok that explains this a lot better than me: https://vm.tiktok.com/ZMFf8RnUb/ (it was also the reason I wanted to do this project).

## So how does it work?

First of all in this code the Hexagons corners have assigned coordinates, so they are the same all the time. We have a function where we have assigned those and from where we can call them when we need them. We have also assigned the starting point. In the real life action the starting point is the corner number one, but to make things easier for us we have assigned the starting point to be a point between corner one and six.

### So to the actual code and how it works:
1.  We get the number of the corner we are moving towards to by getting a random number from the generator and giving that to our function that stores or corner coordinates ==> function named "whichGon".
2.  Next we calculate our next point with "calculateNextOne" function which we give the coordinates of the starting point and the assigned corner as parametres. These coordinates are saved to a list.
3.  NExt we calculate all our cooordinates and forming a list of them to use with drawing the picture
4.  Lastly we draw a picture by changin the value of the picture pixels depending on if the point is in our coordinate list or not. (if it is then the color is black, if it's not the color is white.)

## Here is one picture made with this code
This picture has 10.000 points drawn.
![alt text](https://github.com/laivii/Sierpinski-Hexagon/blob/main/Pictures/sierpinski10_000_black.png?raw=true)
