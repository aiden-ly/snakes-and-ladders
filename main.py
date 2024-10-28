import sys 
import random
import time
import pygame

from pygame.locals import QUIT

pygame.init()


DISPLAYSURF = pygame.display.set_mode((1280, 1080))
pygame.display.set_caption('Snakes and Ladders')
board = pygame.image.load("images/board.webp")
font = pygame.font.SysFont('Arial', 80)
text = font.render('Snakes and Ladders', True, (0,0,0))


background = pygame.transform.scale(pygame.image.load(f"images/background.png"), (3000,1000))
DISPLAYSURF.blit(background,(0,0))
DISPLAYSURF.blit(text,(300,300))
pygame.display.update()

def rules():
  msg = """
  Welcome to Snakes and Ladders!

  Rules:
    1. Initally all players are at starting position 1. Players take turns to roll the dice and they move forward the number of 
    spaces shown on the dice.
    2. If you land at the bottom of a ladder, you can move up to the top of the ladder.
    3. If you land on the head of a snake, you must slide down to the bottom of the snake.
    4. The first player to get to the position 100 is the winner.
    5. Hit enter in the console to roll the dice.
  """
  print(msg)

piece1 = pygame.transform.scale(pygame.image.load(f"players/Red.png"), (50,50))
piece2 = pygame.transform.scale(pygame.image.load(f"players/Yellow.png"), (50,50))
piece3 = pygame.transform.scale(pygame.image.load(f"players/Green.png"), (50,50))
piece4 = pygame.transform.scale(pygame.image.load(f"players/Blue.png"), (50,50))


dicesprite = []
max_value = 100

rules()

for i in range(1,7):
  dicesprite.append(pygame.transform.scale(pygame.image.load(f"images/d{i}.png"), (225,225)))

def get_player_names():
  player1_name = None
  while not player1_name:
      player1_name = input("Please enter a valid name for first player: ").strip()

  player2_name = None
  while not player2_name:
      player2_name = input("Please enter a valid name for second player: ").strip()

  player3_name = None
  while not player3_name:
      player3_name = input("Please enter a valid name for third player: ").strip()

  player4_name = None
  while not player4_name:
      player4_name = input("Please enter a valid name for fourth player: ").strip()

  print(f"\nMatch will be played between {player1_name}, {player2_name}, {player3_name}, and {player4_name}.")
  return player1_name, player2_name, player3_name, player4_name

def dice_roll():
  global roll
  for _ in range(3):
    for i in range(6):
      DISPLAYSURF.blit(dicesprite[i],(900,0)) #cycles through the dice images 
      pygame.display.update()
      time.sleep(0.1)
  roll = random.randint(0, 5) #chooses random number and shows the number on the dice 
  DISPLAYSURF.blit(dicesprite[roll],(900,0))
  pygame.display.update()
  time.sleep(3)
  DISPLAYSURF.blit(dicesprite[roll],(-999,0))
  return roll + 1

snakes = {
  38: [20, 95, 685, -1], # [End of snake, x-coord, y-coord, direction]
  51: [10, 815, 765, 1], 
  76: [54, 575, 365, -1],
  91: [73, 655, 205, -1],
  97: [61, 95, 285, 1]
}
ladders = {
  5: [58, 255, 365, -1],
  14: [49, 735, 445, 1],
  53: [72, 735, 205, -1],
  64: [83, 255, 125, 1]
}

snake_bite = [
    "Womp womp",
    "Darn diggity!",
    "snake bite",
    ":O",
    "haha snake bite"
]

ladder_jump = [
    "Hip hip hooray!",
    "Zoo wee mama!",
    "nailed it",
    "Holy guacamole!",
    "Yippie!"
]

player1_current_position = 1
player2_current_position = 1
player3_current_position = 1
player4_current_position = 1

player1_name, player2_name, player3_name, player4_name = get_player_names()

run = True


player_info = { # [piece image, x-coord, y-coord, current position on board, direction]
  player1_name: [piece1, 95, 765, player1_current_position, 1],
  player2_name: [piece2, 95, 765, player2_current_position, 1],
  player3_name: [piece3, 95, 765, player3_current_position, 1],
  player4_name: [piece4, 95, 765, player4_current_position, 1]
}

while run:
  DISPLAYSURF.blit(background,(0,0))
  DISPLAYSURF.blit(board,(80,30))

  for i in player_info:
    info = player_info[i]
    DISPLAYSURF.blit(info[0],(info[1] ,info[2]))

  pygame.display.update()

  for i in player_info:
    input(f"{i}'s Turn! Press Enter in the Console to roll the dice. ")
    roll = dice_roll()
    info = player_info[i]
    for _ in range(roll): #info[0]: Sprite image, info[1]: x-coord, info[2]: y-coord, info[3]: current position, info[4]: direction
      if info[3] % 10 == 0:
        info[2] -= 80
        info[4] = info[4] * -1
      elif info[4] == 1:
        info[1] += 80
      elif info[4] == -1:
        info[1] -= 80

      info[3] += 1  

      DISPLAYSURF.blit(board,(80,30))

      for v in player_info:
        tempinfo = player_info[v]
        DISPLAYSURF.blit(tempinfo[0],(tempinfo[1] ,tempinfo[2]))

      pygame.display.update()
      time.sleep(0.4)

    for x in snakes:
      if x == info[3]:
        snakeinfo = snakes[x]
        info[3] = snakeinfo[0]
        info[4] = snakeinfo[3]
        info[1] = snakeinfo[1]
        info[2] = snakeinfo[2]
        DISPLAYSURF.blit(board,(80,30))

        for v in player_info:
          tempinfo = player_info[v]

          DISPLAYSURF.blit(tempinfo[0],(tempinfo[1] ,tempinfo[2]))

        print(random.choice(snake_bite))
        pygame.display.update()
        break

    for y in ladders:
      if y == info[3]:
        ladderinfo = ladders[y]
        info[3] = ladderinfo[0]
        info[4] = ladderinfo[3]
        info[1] = ladderinfo[1]
        info[2] = ladderinfo[2]
        DISPLAYSURF.blit(board,(80,30))

        for v in player_info:
          tempinfo = player_info[v]
          DISPLAYSURF.blit(tempinfo[0],(tempinfo[1] ,tempinfo[2]))

        print(random.choice(ladder_jump))
        pygame.display.update()
        break

    if info[3] >= max_value:
      print(f'{i} has won the game!')
      DISPLAYSURF.blit(background,(0,0))
      text = font.render(f'{i} has won!', True, (0,0,0))
      DISPLAYSURF.blit(text,(380,300))
      pygame.display.update()
      time.sleep(10)
      run = False
      break

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  pygame.display.update()
