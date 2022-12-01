$(document).ready(function(){
    $("#shape").change(function(){
        formPicture();
    });

    $("#openSummary").click(function(){
        $("#summary").slideToggle();
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
            context.rect(x, y, 0.5, 0.5);
            context.fill();
        }
    }
    
    //Return a list which contains selected shapes corner coordinates and startingpoint
    function chooseShape(){
        //Getting the shape that user has selected
        var selectedShape = $("#shape option:selected").val();
        var shapesCorners;
        
        /* We select a list based on what shape has been selected
           The list is in form [[startingpoint],[corner1],[corner2],...] (Starting point is always 2/3 between the corner1 and corner2) */
        switch(selectedShape){
            case "triangle":
                shapesCorners = [[0.5],[250,33.5],[0,33.5],[500,33.5],[250,466.51]];
                break;
            case "square":
                shapesCorners = [[0.60],[330,0],[0,0],[0,500],[500,500],[500,0]];
                break;
            case "pentagon":
                shapesCorners = [[0.66],[44,102.5],[0,267.35],[66.985,17.35],[433.15,17.35],[500,267.35],[250,482.65]];
                break;
            case "hexagon":
                shapesCorners = [[0.66],[290,33.5],[125,33.5],[375,33.5],[500,250],[375,466.5],[125,466.5],[0,250]];
                break;
        }

        return shapesCorners;
    }

    //This function calculates and makes a list of the coordinates we form the picture with
    function calculateCoords(){
        var shape = chooseShape();
        var startingPoint = shape[1];
        var scale = shape[0][0];
        var coordinates = [];
    
        //Calculates x amount of points so the picture starts to form
        for(var i = 0; i < 1000000; i++){
            var corner = Math.floor(Math.random() * (shape.length-2)) + 2;
            var cornerPoint = shape[corner];
            var point = calculateNextOne(startingPoint, cornerPoint, scale);
    
            startingPoint = point;
    
            coordObj = {
                x: point[0],
                y: point[1]
            };
            
            coordinates[i] = coordObj;
        }

        return coordinates;
    }

    //This function calculates the next point
    function calculateNextOne (point1,point2,scale){
        var x = Math.round(point1[0] + ((point2[0] - point1[0])*scale));
        var y = Math.round(point1[1] + ((point2[1] - point1[1])*scale));
    
        var new_point = [x,y];
        
        return new_point;
    }
});