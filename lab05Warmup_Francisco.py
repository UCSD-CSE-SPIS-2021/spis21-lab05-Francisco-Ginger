# Imports the Image portion form the PIL image library in Python.
from PIL import Image

# Creates a new image object by grabbing the file from bear.png and storing it within bear variable.
bear = Image.open( "bear.png" )
# Creates a new image object grabbing the file from batman.png and storing it within batman variable.
batman = Image.open("batman.png")

print(bear.size)

pixel = bear.getpixel( ( 100, 200) )

print(pixel)

# Creates a black line for x-coordinates from 0-100 and static y-coordinate of 200
for i in range(100):
    
    bear.putpixel( (i, 200) , (0, 0, 0) )


def invert( im ):
    ''' Invert the colors in the input image, im '''
    # Find the dimensions of the image
    (width, height) = im.size
    # Loop over the entire image
    for x in range( width ):
        for y in range( height ):
            (red, green, blue, opaqueness) = im.getpixel((x, y))
            # Complete this function by adding your lines of code here.
            # You need to calculate the new pixel values and then to change them
            red = 255 - red
            green = 255 - green
            blue = 255 - blue
            # in the image using putpixel()
            im.putpixel( (x,y) , (red, green, blue) )

def invert_block( im ):
    ''' Invert the colors back to the original image only for the top left quadrant in the input image, im '''
    # Find the dimensions of the image
    (width, height) = im.size
    # Loop over the entire image
    for x in range( width // 2):
        for y in range( height // 2 ):
            (red, green, blue, opaqueness) = im.getpixel((x, y))
            # Complete this function by adding your lines of code here.
            # You need to calculate the new pixel values and then to change them
            red = 255 - red
            green = 255 - green
            blue = 255 - blue
            # in the image using putpixel()
            im.putpixel( (x,y) , (red, green, blue) )

invert(bear)
invert_block(bear)

# Allows the image to be modified and saved everytime it is ran
bear.save("tmp_Francisco.png") # create/overwrite tmp_Name.png with current image

invert(batman)
batman.save("tmp_batman.png")

