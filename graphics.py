from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = 'window'
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self,line,color="black"):
        line.draw(self.canvas,color)


class Point():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

class Line():
    def __init__(self,p1,p2) -> None:
        self.p1 = p1
        self.p2 = p2
    def draw(self,canvas,color):
        p1 = self.p1
        p2 = self.p2
        canvas.create_line(p1.x,p1.y,p2.x,p2.y,fill=color,width=2)
