# black and white bitmap image 
# source: https://create.withcode.uk/python/cj

import withcode

# create a 2d list of binary data
# 1 is black and 0 is white
data = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]] 

# create an image and display it
i = withcode.Image(200,200)
i.draw(data)
print("Challenges:")
print("1) Change the face to make it sad")
print("2) Make the face bigger (maybe 500 x 500 pixels)")
print("3) Draw any other image rather than a smiley face")
print("4) Make your image 10x10 pixels instead of 8x8 pixels")
