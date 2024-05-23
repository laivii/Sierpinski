/**
 * This function frms a black-and-white picture of the calculated coordinates to the canvas element
 */
function formCanvasPicture(){
    //Get canvas element
    const canvas = document.getElementById( "sierpinskiCanvas" );
    const context = canvas.getContext( "2d" );
    canvas.height = canvas.width;

    //Get coordinates
    const coordinates = calculateCoordinates();
            
    //Set fill color
    context.fillStyle = "white"
    for( let iteration = 0; iteration < coordinates.length-1; iteration++ ){
        //Get individual pixels coordinates
        let x = Math.round( coordinates[ iteration ].x );
        let y = Math.round( coordinates[ iteration ].y );

        //Change the color of the pixels
        context.beginPath();
        context.rect( x, y, 1, 1 ); //parameters (x-coordinate, y-coordinate, width, height)
        context.fill();
    }
}

/**
 * Calculate the coordinates.
 * The number of points has been set to 100,000 point by default
 * Starting point is set to 2/3 of 1 --> 6 to make things easier
 */
function calculateCoordinates(){
    let numberOfPoints = 100000;
    let startingPoint = [ 85, 268 ];
    let coordinates = [];

    for( let index = 0; index < numberOfPoints; index++ ){
        //Get corner point coordinates
        let corner = Math.floor( Math.random() * 6 ) + 1; //Get random integer between 1-6
        let cornerPoint =  whichCorner( corner );

        //Get the next point
        let point = calculateNextPoint( startingPoint, cornerPoint )

        //Set the point values to a coordinate object
        let coordObj = {
            x: point[ 0 ],
            y: point[ 1 ]
        }

        //Add point to the coordinates
        coordinates[index] = coordObj;
    }

    return coordinates;
}

/**
* Calculate and return the next point
* Next point is in 2/3 between point1 and point2
*/
function calculateNextPoint( point1, point2){
    let x = Math.round( point1[ 0 ] + (( point2[ 0 ] - point1[ 0 ] ) * 0.66 ));
    let y = Math.round( point1[ 1 ] + (( point2[ 1 ] - point1[ 1 ] ) * 0.66 ));

    let newPoint = [ x, y ];

    return newPoint
}

/*
#   Set endpoints, "corners", for the Sierpinski shape
#   This function is used to return the desired coordinates depending on the corner "chosed"
*/
function whichCorner( corner){
    switch( corner ){
        case 1:
           var coordinates = [ 250, 67 ];
           return coordinates;
        case 2:
           var coordinates = [ 750, 67 ];
           return coordinates;
        case 3:
           var coordinates = [ 1000, 500 ];
           return coordinates;
        case 4:
           var coordinates = [ 750, 933 ];
           return coordinates;
        case 5:
           var coordinates = [ 250, 933 ];
           return coordinates;
        case 6:
           var coordinates = [ 0, 500 ];
           return coordinates;
        default:
           throw new Error( "Invalid corner number" );
   }
}

formCanvasPicture();
