#! /usr/bin/env python3

grid = set()
with open('24.input', 'r') as file:
  for line in file:
    line = line.strip()
    pos = 0
    x, y, z = 0, 0, 0
    while pos < len(line):
      if line[pos] == 'e':
        x += 1
        y -= 1
        pos += 1
      elif line[pos] == 'w':
        x -= 1
        y += 1
        pos += 1
      elif line[pos] == 's':
        if line[pos + 1] == 'e':
          y -= 1
          z += 1
        else:
          x -= 1
          z += 1
        pos += 2
      elif line[pos] == 'n':
        if line[pos + 1] == 'e':
          x += 1
          z -= 1
        else:
          y += 1
          z -= 1
        pos += 2
    if (x, y, z) in grid:
      grid.remove((x, y, z))
    else:
      grid.add((x, y, z))

def mutate(grid):
  counts = {}
  for x, y, z in grid:
    for coords in [
      (x + 1, y - 1, z + 0),
      (x + 0, y - 1, z + 1),
      (x - 1, y + 0, z + 1),
      (x - 1, y + 1, z + 0),
      (x + 0, y + 1, z - 1),
      (x + 1, y + 0, z - 1),
    ]:
      counts[coords] = counts.get(coords, 0) + 1

  to_del = []
  to_flip = []

  for coords, count in counts.items():
    if count == 2 and coords not in grid:
      to_flip.append(coords)
  for coords in grid:
    if coords not in counts or counts[coords] > 2:
      to_del.append(coords)

  for coords in to_flip:
    grid.add(coords)
  for coords in to_del:
    grid.remove(coords)

#print(f'Day 0: {len(grid)}')
for day in range(1, 101):
  mutate(grid)
  #print(f'Day {day}: {len(grid)}')
print(len(grid))
