
from graphics import Line, Point, Window


def main():
    print("Creating Window")
    win = Window(800, 600)
    line = Line(Point(100,100),Point(0,0))
    win.draw_line(line)
    win.wait_for_close()


if __name__ == "__main__":
    main()
