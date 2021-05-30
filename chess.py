import numpy as np 
import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

class ChessBoard :

 def render(self ,red:list, blue:list):
     self.add_red(red)
     self.add_blue(blue)
     plt.imshow(self.grid)
     result = self.is_under_attack(red,blue)
     if result == True:
         print("red is underattack")
     else:
         print("red is safe")

 def is_under_attack(self,red,blue):
   if red[0] == blue[0] or red[1] == blue[1] or self.is_diagonal(red,blue):
       return True

 def add_red(self,red):
     self.grid[red[0],red[1]] = [1,0,0]
 def add_blue(self,blue):
     self.grid[blue[0],blue[1]] = [0,0,1]
 def is_diagonal(self,point1,point2):
  """
  given coordinates for 2 points a and b
  determine if they are diagonals
  """
  dx = abs(point1[0] - point2[0])
  dy = abs(point1[1] - point2[1])
  return dx == dy
 def __init__(self) :
        self.grid = np.zeros((8,8,3))
        for i in range(8):
            for j in range(8):
                if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
                    self.grid[i,j]= [1,1,1]


chessBoard  = ChessBoard()
chessBoard.render([4,5],[2,5])

def test_chess():
    chessBoard  = ChessBoard()
    expected = ["red is underattack","red is underattack","red is underattack","red is safe"]
    actual = [chessBoard.render([4,3],[2,5]),chessBoard.render([4,3],[4,5]),chessBoard.render([4,5],[2,5]),chessBoard.render([1,3],[2,5])]
    assert expected == actual
    print("all tests passed")

chessBoard  = ChessBoard()
test_chess()
chessBoard.render([4,5],[2,5])