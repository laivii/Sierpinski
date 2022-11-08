import png

width = 1000
height = 1000

img = []

for i in coords:
    for y in range(height):
        row = ()
        if i[1] == y:
            for x in range(width):
                if i[0] == x:
                    row = row + (0,0,0)
                    break
                else:
                    row = row + (255,255,255)
            img.append(row)

with open('gradient.png', 'wb') as f:
    w = png.Writer(width, height, greyscale=False)
    w.write(f, img)