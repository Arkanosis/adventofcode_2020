#! /usr/bin/env python3

d = ([], [])
p = -1
with open('22.input', 'r') as file:
  for line in file:
    line = line.strip()
    if ':' in line:
      p += 1
    elif line:
      d[p].append(int(line))

#game_id = 1

winner = {}

def play_game(d0, d1):
  #global game_id
  #g = game_id
  #game_id += 1
  #print(f'=== Game {g} ===')
  gid = (str(d0), str(d1))
  if gid in winner:
    return winner[gid]
  known = set()
  #r = 1
  while True:
    id = (str(d0), str(d1))
    if id in known:
      #print(f'Player 1 wins game {g}!')
      winner[gid] = 0
      return 0
    known.add(id)
    #print(f'\n-- Round {r} (Game {g}) --')
    #print (f'1: {d0}')
    #print (f'2: {d1}')
    c0, c1 = d0.pop(0), d1.pop(0)
    if len(d0) >= c0 and len(d1) >= c1:
      if play_game(d0[:c0], d1[:c1]):
        d1.extend([c1, c0])
        #print(f'Player 2 wins round {r} of game {g}!')
      else:
        d0.extend([c0, c1])
        #print(f'Player 1 wins round {r} of game {g}!')
    else:
      if c0 > c1:
        d0.extend([c0, c1])
        #print(f'Player 1 wins round {r} of game {g}!')
      elif c1 > c0:
        d1.extend([c1, c0])
        #print(f'Player 2 wins round {r} of game {g}!')
      else:
        pass
    if not len(d0):
      winner[gid] = 1
      return 1
    elif not len(d1):
      winner[gid] = 0
      return 0
    #r += 1

play_game(d[0], d[1])

p = 1
s = 0
for c in (d[0] + d[1])[::-1]:
  s += c * p
  p += 1

print(s)
