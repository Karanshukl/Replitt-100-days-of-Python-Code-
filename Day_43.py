import random 

def random_numbers():
  number = random.randint(1, 90)
  return number

def printvalue():
  for row in BINGO:
    print (row)
    
# empty list for the bingo grid 
BINGO = []

# Generate 8 random numbers and sort them
numbers = [random_numbers() for _ in range(8)]
numbers.sort()

BINGO = [ [numbers[0], numbers[1], numbers[2]],
          [numbers[3], "BINGO", numbers[4]],
          [numbers[5],numbers[6], numbers[6]] ]

printvalue()




#  2nd method           (By using a class)

import random

class BingoGrid:
    def __init__(self):
        self.grid = []
        self.generate_grid()

    def enerate_grid(self):
        numbers = sorted(random.randint(1, 90) for _ in range(8))
        self.grid = [
                     [numbers[0], numbers[1], numbers[2]],
                     [numbers[3], "BINGO", numbers[4]],
                     [numbers[5], numbers[6], numbers[7]]
                                                         ]

    def print_grid(self):
        for row in self.grid:
            print(row)

# Create a BINGO grid object
bingo_grid = BingoGrid()

# Print the BINGO grid
bingo_grid.print_grid()
