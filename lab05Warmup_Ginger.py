from PIL import Image #imports image portion of PIL library
bear = Image.open( "bear.png" ) #opens an image an stores a reference to it in bear variable
pattern = Image.open( "pattern.png")

pixel = bear.getpixel((100, 200))
#pixel is a tuple representing the rgb values of pixel @ (100,200)
print(pixel)
bear.putpixel((100, 200), (0, 0, 0))
#takes 2 arguments: (x, y) and (r, g, b)
for i in range(100):
  bear.putpixel((i, 200), (0, 0, 0))
  #x 0 to 100, y = 200, black line

def invert(im):
  '''invert the colors in the input image, im'''

  #find the dimensions of the image
  (width, height) = im.size

  #loop over the entire image
  for x in range ( width ):
    for y in range ( height ):
      #calculate the new pixel values
      #put
        (red, green, blue, opacity) = im.getpixel((x, y))
        red = 255 - red
        green = 255 - green
        blue = 255 - blue
        im.putpixel((x, y), (red, green, blue))
invert(bear)
bear.save("tmp_Ginger.png") # create/overwrite tmp_Ginger.png with current image, click on file to view
invert(pattern)
pattern.save("tmp_pattern.png")