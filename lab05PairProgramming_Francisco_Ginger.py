
# Imports the Image portion form the PIL image library in Python.
from PIL import Image
import random

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
    ''' Invert the colors in the input image to grayscale, im '''
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
    for x in range(width // 2,  width):
        for y in range( height // 2 ):
            (red, green, blue, opaqueness) = im.getpixel((x, y))
            # Complete this function by adding your lines of code here.
            # You need to calculate the new pixel values and then to change them
            red = 255 - red
            green = 255 - green
            blue = 255 - blue
            # in the image using putpixel()
            im.putpixel( (x,y) , (red, green, blue) )

def grayscale( im ):
    ''' change colors to grayscale using luminescence '''
    # Find the dimensions of the image
    (width, height) = im.size
    # Loop over the entire image
    for x in range( width ):
        for y in range( height ):
            (red, green, blue, opaqueness) = im.getpixel((x, y))
            # Complete this function by adding your lines of code here.
            # You need to calculate the new pixel values and then to change them
            red = int(red * 0.21)
            green = int(green * 0.72)
            blue = int(blue * 0.07)
            color = red + green + blue
            # in the image using putpixel()
            im.putpixel( (x,y) , (color, color, color) )

def binarize( im, thresh, startx, starty, endx, endy ):
    ''' change colors to white or black using a threshold '''
    # Find the dimensions of the image
    (width, height) = im.size
    # Loop over the entire image
    if thresh > 255 or thresh < 0:
        print("Pick a number between 0 and 255")
    elif startx < 0 or startx > width or endx < 0 or endx > width or starty < 0 or starty > height or endy < 0 or endy > height:
        print("Pick a new set of parameters within the images dimensions")
    else:
        for x in range( startx, endx ):
            for y in range( starty, endy ):
                (red, green, blue, opaqueness) = im.getpixel((x, y))
                # Complete this function by adding your lines of code here
                # You need to calculate the new pixel values and then to change them
                red = int(red * 0.21)
                green = int(green * 0.72)
                blue = int(blue * 0.07)
                luminence = red + green + blue
                if(luminence < thresh):
                     im.putpixel( (x,y) , (0, 0, 0))
                else:
                    im.putpixel( (x,y), (255, 255, 255))

def mirrorVert( im ):
    ''' Apply a vertical mirror effect to your image '''
    # Find the dimensions of the image
    (width, height) = im.size
    # Loop over entire width and half of height
    for x in range( width ):
        for y in range( height // 2):
            (red, green, blue, opaqueness) = im.getpixel((x, y))
            
            im.putpixel( (x, height - y - 1) , (red, green, blue))

def mirrorHoriz( im ):
    ''' Apply a horizontal mirror effect to your image '''
    # Find the dimensions of the image
    (width, height) = im.size
    # Loop over entire height and half of width
    for x in range( width // 2):
        for y in range( height):
            (red, green, blue, opaqueness) = im.getpixel((x, y))
            
            im.putpixel( (width - x - 1, y) , (red, green, blue))

def flipVert(im):
  '''Flip the image so the bottom is at the top and top is at the bottom'''
  (width, height) = im.size
  for x in range( width ):
        for y in range( height // 2):
          #creates temp for opposite pixel
            (redtemp, greentemp, bluetemp, opaqueness) = im.getpixel((x, height - 1 - y))
          #color at (x, y)
            (red, green, blue, opacity) = im.getpixel((x, y))
          #sets opposite pixel to color at (x, y)
            im.putpixel( (x, height - y - 1) , (red, green, blue))
          #sets pixel to color on bottom
            im.putpixel((x, y), (redtemp, greentemp, bluetemp))

def scale(im):
  '''takes image im as parameter and scales it to be half the original size, creates a modified copy of image and RETURNS it'''
  (width, height) = im.size
  #creates a new image (in color), with a certain width and height given by tuple
  new = Image.new('RGB', (width // 2, height // 2))
  #index of pixel in new image are defined by newx and newy
  newx = 0
  #loops through entire image but only every other pixel
  for x in range(0, width-3, 2):
    #define inside loop because when x increases by 1 y should reset to 0 (start at top of picture)
    newy = 0
    for y in range(0, height-3, 2):
      (red, green, blue, opacity) = im.getpixel((x,y))
      #print("Current new coordinates: " + str(newx) + ", " + str(newy))
      new.putpixel((newx, newy), (red, green, blue))
      newy += 1
    newx += 1
  new.show()
  return new
#scale_image = scale(bear)
#scale_image.save("scale2.png")
#print(scale_image.size)

def blur(im):
  #groups of 4 pixels
  #ex: (0,0) (1,0) (0,1) (1,1)
  #(x,y) are coordinates of upper left corner, in example that's (0,0)
  #get rgb @ (x,y),(x+1,y),(x,y+1),(x+1,y+1)
    (width, height) = im.size
    new = Image.new('RGB', (width, height))
    for x in range(0, width-2, 2):
        for y in range(0, height-2,2):
            (red1, green1, blue1, opacity1) = im.getpixel((x,y))
            (red2, green2, blue2, opacity2) = im.getpixel((x, y+1))
            (red3, green3, blue3, opacity3) = im.getpixel((x+1, y))
            (red4, green4, blue4, opacity4) = im.getpixel((x+1, y+1))
            red_av = (red1 + red2 + red3 + red4)//4
            green_av = (green1 + green2 + green3 + green4) // 4
            blue_av = (blue1 + blue2 + blue3 + blue4) // 4
            new.putpixel((x,y), (red_av, green_av, blue_av))
            new.putpixel((x+1,y), (red_av, green_av, blue_av))
            new.putpixel((x,y+1), (red_av, green_av, blue_av))
            new.putpixel((x+1,y+1), (red_av, green_av, blue_av))
    new.show()
    return new

blur_image = blur(bear)
blur_image.save("blur.png")


#bear.save("scale.png") 
# create/overwrite tmp_Name.png with current image
