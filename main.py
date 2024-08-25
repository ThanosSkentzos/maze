
from cell import Cell
from graphics import Line, Point, Window


def main():
    print("Creating Window")
    win = Window(800, 600)
    # line = Line(Point(100,100),Point(0,0))
    # win.draw_line(line)
    c1 = Cell(win)
    c1.has_left_wall = False
    c1.draw(350,50,400,100)

    c2 = Cell(win)
    c2.has_right_wall = False
    c2.draw(50,50,100,100)
    c2.draw_move(c1)

    win.wait_for_close()


if __name__ == "__main__":
    main()
