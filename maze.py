from cell import Cell
from time import sleep
import random
random.seed(42)

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()



    def _create_cells(self):
        self._cells = [[Cell(self.win) for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        for i,row in enumerate(self._cells):
            for j,_ in enumerate(row):
                self._draw_cell(i,j)
        pass

    def _draw_cell(self,i,j):
        x1 = self.x1 + self.cell_size_x*i
        x2 = self.x1 + self.cell_size_x*(i+1)
        y1 = self.y1 + self.cell_size_y*j
        y2 = self.y1 + self.cell_size_y*(j+1)

        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()


    def _animate(self,t = 0.001):
        if self.win is None: return
        self.win.redraw()
        sleep(t)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

    def _break_walls_r(self,i,j):
        current = self._cells[i][j]
        current.visited = True
        # print("current: ",i,j)
        while True:
            to_visit = []
            neighbors = []
            for k,l in zip([i-1,i,i,i+1],[j,j-1,j+1,j]):
                neighbors.append((k,l))
            # print("neighbors: ",neighbors)
            not_visited = [(k,l) for k,l in neighbors
                if 0<=k<self.num_cols
                and 0<=l<self.num_rows
                and not self._cells[k][l].visited]
            # print("not visited",not_visited)
            if len(not_visited)==0:
                self._draw_cell(i,j)
                return
            target_xy = not_visited[random.randrange(0,len(not_visited))]
            x,y = target_xy
            direction = neighbors.index(target_xy)
            if x<0 or y<0 or x>self.num_cols or y>self.num_rows:
                continue
            target = self._cells[target_xy[0]][target_xy[1]]


            # print("direction choice:",direction)
            match direction:
                case 0:#left
                    self._break_walls_r(i-1,j)
                    current.has_left_wall=False
                    target.has_right_wall=False
                case 1:#up
                    self._break_walls_r(i,j-1)
                    current.has_top_wall=False
                    target.has_bottom_wall=False

                case 2:#down
                    self._break_walls_r(i,j+1)
                    current.has_bottom_wall=False
                    target.has_top_wall=False

                case 3:#right
                    self._break_walls_r(i+1,j)
                    current.has_right_wall=False
                    target.has_left_wall=False

            # sleep(0.05)
    def _reset_cells_visited(self):
        for col in self._cells:
            for c in col:
                c.visited = False
        print("Maze Ready.")
