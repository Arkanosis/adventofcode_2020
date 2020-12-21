#! /usr/bin/env python3

class Image:

  def __init__(self, id):
    self.id = id
    self.rows = []
    self.rotation = 0
    self.hf = False
    self.vf = False

  def add_row(self, row):
    self.rows.append(row)

  def compute(self):
    self.top = self.rows[0]
    self.bottom = self.rows[-1]
    self.left = ''.join([row[0] for row in self.rows])
    self.right = ''.join([row[-1] for row in self.rows])

  def rotate(self):
    self.rotation = (self.rotation + 1) % 4
    old_top = self.top
    self.top = self.right
    self.right = self.bottom[::-1]
    self.bottom = self.left
    self.left = old_top[::-1]

  def hflip(self):
    self.hf = not self.hf
    self.left, self.right = self.right, self.left
    self.top = self.top[::-1]
    self.bottom = self.bottom[::-1]

  def vflip(self):
    self.vf = not self.vf
    self.top, self.bottom = self.bottom, self.top
    self.left = self.left[::-1]
    self.right = self.right[::-1]

  def display(self):
    print(self)
    for row in self.rows:
      print(row)

  def __repr__(self):
    return f'{self.id} (r={self.rotation}, hf={self.hf}, vf={self.vf})'

def display_image(image):
  mx, Mx = min([x for x, _ in image.keys()]), max([x for x, _ in image.keys()])
  my, My = min([y for _, y in image.keys()]), max([y for _, y in image.keys()])
  for y in range(my, My + 1):
    print('y =', y)
    for x in range(mx, Mx + 1):
      print('x =', x)
      if (x, y) in image:
        image[x, y].display()
    print()

tiles = []
image = None
with open('20.input', 'r') as file:
  for line in file:
    line = line.strip()
    if line.startswith('Tile '):
      if image:
        image.compute()
        tiles.append(image)
      image = Image(int(line[5:-1]))
    elif line:
      image.add_row(line)
  else:
    if image:
        image.compute()
        tiles.append(image)

tiles.sort(key=lambda image: image.id)

left_count = len(tiles)
image = {(0, 0): tiles.pop(0)}
while tiles:
  if left_count == len(tiles):
    print('Unable to position:')
    tiles[0].display()
    print('Already positioned:')
    display_image(image)
    break
  left_count = len(tiles)
  #print(left_count, "left")
  left = []
  for tile in tiles:
    #print('Trying tile', tile.id)
    found = False
    for orientation in range(4):
      for hflip in False, True:
        for vflip in False, True:
          for (x, y), other in image.items():
            if tile.top == other.bottom:
              #print(f'{tile} at {x}, {y-1}, on bottom of {other} at {x}, {y}')
              image[x, y - 1] = tile
              found = True
              break
            elif tile.bottom == other.top:
              #print(f'{tile} at {x}, {y+1}, on top of {other} at {x}, {y}')
              image[x, y + 1] = tile
              found = True
              break
            elif tile.left == other.right:
              #print(f'{tile} at {x+1}, {y-1}, on right of {other} at {x}, {y}')
              image[x + 1, y] = tile
              found = True
              break
            elif tile.right == other.left:
              #print(f'{tile} at {x-1}, {y-1}, on left of {other} at {x}, {y}')
              image[x - 1, y] = tile
              found = True
              break
          if found:
            break
          #print('vflipping')
          tile.vflip()
        if found:
          break
        #print('hflipping')
        tile.hflip()
      if found:
        break
      #print('rotating')
      tile.rotate()
    if not found:
      #print('keeping for the moment')
      left.append(tile)
  tiles = left

mx, Mx = min([x for x, _ in image.keys()]), max([x for x, _ in image.keys()])
my, My = min([y for _, y in image.keys()]), max([y for _, y in image.keys()])
print(image[mx, my].id * image[mx, My].id * image[Mx, My].id * image[Mx, my].id)
