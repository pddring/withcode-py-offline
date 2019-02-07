import tkinter

class Image:
    def __init__(self, width, height):
        self.w = width
        self.h = height

    # draw an image represented by an array of data
    def draw(self, data):
        color = "unknown"
        master = tkinter.Tk()

        win = tkinter.Canvas(master, width=self.w, height=self.h)
        master.title("withcode")
        win.pack()

        # get type of data
        if type(data) is list:

            # see if it's a 2d array
            if type(data[0]) is list:

                #see if it's a 3d array:
                if type(data[0][0]) is list:
                    color = "RGB"



                # get dimensions
                h = len(data)
                w = len(data[0])

                if color != "RGB":
                    # determine if it's black and white (0-1) or grayscale (0-255)
                    largest_val = 0
                    for x in range(w):
                        for y in range(h):
                            if data[y][x] > largest_val:
                                largest_val = data[y][x]
                    if largest_val <= 1:
                        color = "BW"
                    else:
                        color = "GRAY"

                # determine pixel width / height
                width = self.w / w
                height = self.h / h

                def int2hex(intval):
                    color = hex(intval)[2:]
                    if len(color) < 2:
                        color = "0" + color
                    return color

                # draw each pixel
                for x in range(w):
                    for y in range(h):
                        if color == "BW":
                            if data[y][x] == 1:
                                fill = "black"
                            else:
                                fill = "white"
                        if color == "GRAY":
                            fill = "#" + (int2hex(data[y][x]) * 3)
                        if color == "RGB":
                            fill = "#" + int2hex(data[y][x][0]) + int2hex(data[y][x][1]) + int2hex(data[y][x][2])

                        # draw pixel
                        win.create_rectangle(x * width, y * height, width * (x+1), height * (y+1), fill=fill)

            else: # 1D array
                print("1D array")
        else:
            print("not an array")


        tkinter.mainloop()
