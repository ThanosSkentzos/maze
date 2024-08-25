from cell import Cell
from time import sleep


class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self.win) for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        for i,row in enumerate(self._cells):
            for j,_ in enumerate(row):
                self._draw_cell(i,j)
        pass

    def _draw_cell(self,i,j):
        x1 = self.x1 + self.cell_size_x*i
        x2 = self.x1 + self.cell_size_x*(i+1)
        y1 = self.y1 + self.cell_size_y*j
        y2 = self.y1 + self.cell_size_y*(j+1)

        self._cells[i][j].draw(x1,x2,y1,y2)
        self._animate()


    def _animate(self,t = 0.001):
        if self.win is None: return
        self.win.redraw()
        sleep(t)
