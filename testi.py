import png

width = 11
height = 11

coords = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]]

img = []

for y in range(height):
    row = ()
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