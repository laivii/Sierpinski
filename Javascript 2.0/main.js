$(document).ready(function(){
    $("#shape").change(function(){
        formPicture();
    });

    //This function draws the picture to our canvas
    function formPicture(){
        const canvas = document.getElementById("myCanvas");
        //Here we tell what kind of picture we want to for (2D, 3D etc.)
        const context = canvas.getContext("2d");
        canvas.height = canvas.width;
        
        const Array = calculateCoords();
    
        //Here we specify our colors and make the dots to right places
        context.fillStyle = "white";
        for (let i = 0; i < Array.length-1; i++) {
            let x = Math.round(Array[i].x);
            let y = Math.round(Array[i].y);
            
            context.beginPath();
            context.rect(x, y, 1, 1);
            context.fill();
        }
    }
    
    //Return a list which contains selected shapes corner coordinates and startingpoint
    function chooseShape(){
        //Getting the shape that user has selected
        var selectedShape = $("#shape option:selected").val();
        console.log(selectedShape);
        var shapesCorners;
        
        /* We select a list based on what shape has been selected
           The list is in form [[startingpoint],[corner1],[corner2],...] (Starting point is always 2/3 between the corner1 and corner2) */
        switch(selectedShape){
            case "triangle":
                shapesCorners = [[660,67],[0,67],[1000,67],[500,933.02]];
                break;
            case "square":
                shapesCorners = [[660,0],[1,1],[1,999],[999,999],[1,999]];
                break;
            case "pentagon":
                shapesCorners = [[88,205],[0,534.7],[133.97,34.7],[866.3,34.7],[1000,534.7],[500,965.3]];
                break;
            case "hexagon":
                shapesCorners = [[580,67],[250,67],[750,67],[1000,500],[750,933],[250,933],[0,500]];
                break;
        }

        console.log(shapesCorners);
        return shapesCorners;
    }

    //This function calculates and makes a list of the coordinates we form the picture with
    function calculateCoords(){
        var shape = chooseShape();
        var startingPoint = shape[0];
        var coordinates = [];
    
        //Calculates x amount of points so the picture starts to form
        for(var i = 0; i < 100000; i++){
            var corner = Math.floor(Math.random() * (shape.length-1)) + 1;
            console.log(corner);
            var cornerPoint = shape[corner]; //Getting the corner by random number in between 1 - 6.
            console.log(cornerPoint);
            var point = calculateNextOne(startingPoint, cornerPoint);
    
            startingPoint = point;
    
            coordObj = {
                x: point[0],
                y: point[1]
            };
            
            coordinates[i] = coordObj;
        }
    
        console.log(coordinates);
        return coordinates;
    }

    //This function calculates the next point
    function calculateNextOne (point1,point2){
        var x = Math.round(point1[0] + ((point2[0] - point1[0])*0.66));
        var y = Math.round(point1[1] + ((point2[1] - point1[1])*0.66));
    
        var new_point = [x,y];
        
        return new_point;
    }
});