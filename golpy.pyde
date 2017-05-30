class Game:
    def __init__(self, r, c, w, h):
        self.rows = r
        self.columns = c
        self.width = w
        self.height = h
                 
        self.cells = []
        for x in range(r*c):
            cell_color = 0 if random(1) > 0.5 else 255
            self.cells.append(Cell(cell_color))
        
    def draw(self):
        for i, x in enumerate(self.cells):
            x.draw((i % self.columns) * self.width, (i/self.columns) * self.height, self.width, self.height)
            
    def calculate(self):
        for i, x in enumerate(self.cells):
            r = (i / self.columns)
            c = (i % self.columns)
            x.calculate(self.cells[(r-1 if r > 0 else self.rows - 1) * self.columns + (c-1 if c > 0 else self.columns - 1)],
                    self.cells[(r-1 if r > 0 else self.rows - 1)  * self.columns + c],
                    self.cells[(r-1 if r > 0 else self.rows - 1)  * self.columns + (c+1 if c < (self.columns - 1) else 0)],
                    self.cells[r  * self.columns  + (c-1 if c > 0 else self.columns - 1)],
                    self.cells[r  * self.columns + (c+1 if c < (self.columns -1) else 0)],
                    self.cells[(r+1 if r < (self.rows - 1) else 0)  * self.columns + (c-1 if c > 0 else self.columns - 1)],
                    self.cells[(r+1 if r < (self.rows - 1) else 0)  * self.columns + c],
                    self.cells[(r+1 if r < (self.rows - 1) else 0)  * self.columns + (c+1 if c < (self.columns - 1) else 0)])
            # if x.color == 255:
            #     print ('r: ' + str(r) + ' c: ' + str(c))
            #     print 'current: ' + str(i)
            #     upper_left = ((r-1 if r > 0 else self.rows - 1) * self.columns + (c-1 if c > 0 else self.columns - 1))
            #     upper_middle = ((r-1 if r > 0 else self.rows - 1)  * self.columns + c)
            #     upper_right = ((r-1 if r > 0 else self.rows - 1)  * self.columns + (c+1 if c < (self.columns - 1) else 0))
            #     center_left = (r  * self.columns)  + (c-1 if c > 0 else self.columns - 1)
            #     center_right = (r  * self.columns) + (c+1 if c < (self.columns -1) else 0)
            #     lower_left = ((r+1 if r < (self.rows - 1) else 0)  * self.columns + (c-1 if c > 0 else self.columns - 1))
            #     lower_middle = ((r+1 if r < (self.rows - 1) else 0)  * self.columns + c)
            #     lower_right = ((r+1 if r < (self.rows - 1) else 0)  * self.columns + (c+1 if c < (self.columns - 1) else 0))
                
                
            #     print 'upper_left: ' + str((r-1 if r > 0 else self.rows - 1) * self.columns + (c-1 if c > 0 else self.columns - 1)) + 'color: ' + str(self.cells[upper_left].color)
            #     print 'upper_middle: ' + str((r-1 if r > 0 else self.rows - 1)  * self.columns + c) + 'color: ' + str(self.cells[upper_middle].color)
            #     print 'upper_right: ' + str((r-1 if r > 0 else self.rows - 1)  * self.columns + (c+1 if c < (self.columns - 1) else 0)) + 'color: ' + str(self.cells[upper_right].color)
                
            #     print 'center_left: ' + str(r  * self.columns  + (c-1 if c > 0 else self.columns - 1)) + 'color: ' + str(self.cells[center_left].color)
            #     print 'center_right: ' + str(r  * self.columns + (c+1 if c < (self.columns -1) else 0)) + 'color: ' + str(self.cells[center_right].color)
                
            #     print 'lower_left: ' + str((r+1 if r < (self.rows - 1) else 0)  * self.columns + (c-1 if c > 0 else self.columns - 1)) + 'color: ' + str(self.cells[lower_left].color)
            #     print 'lower_middle: ' + str((r+1 if r < (self.rows - 1) else 0)  * self.columns + c) + 'color: ' + str(self.cells[lower_middle].color)
            #     print 'lower_right: ' + str((r+1 if r < (self.rows - 1) else 0)  * self.columns + (c+1 if c < (self.columns - 1) else 0)) + 'color: ' + str(self.cells[lower_right].color)
                
                                    
    def update(self):
        for i, x in enumerate(self.cells):
            x.update()


class Cell:
    def __init__(self, cell_color):
        self.new_color = cell_color
        self.color = cell_color
    
    def draw(self, x, y, w, h):
        fill(self.color)
        rect(x, y, w, h)
        
    def calculate(self,
               upper_left,
               upper_middle,
               upper_right,
               center_left,
               center_right,
               lower_left,
               lower_middle,
               lower_right):
        neighbours = []
        neighbours.append(upper_left)
        neighbours.append(upper_middle)
        neighbours.append(upper_right)
        neighbours.append(center_left)
        neighbours.append(center_right)
        neighbours.append(lower_left)
        neighbours.append(lower_middle)
        neighbours.append(lower_right) 
            
        count = 0
        for i, x in enumerate(neighbours):
            if x.color == 255:
                count = count + 1
                
        if count < 2:
            self.new_color = 0
        elif count > 3:
            self.new_color = 0
        elif count == 3:
            self.new_color = 255
        else:
            self.new_color = self.color
        
    def update(self):
        self.color = self.new_color

game = Game(150, 150, 5, 5)

def setup():
    size(800,800)
    frameRate(20)

def draw():
    game.calculate()
    game.update()
    game.draw()