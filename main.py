import turtle 
# window = turtle.Screen()
# window.setup(500,500)
# random_turtle = turtle.Turtle()
# random_turtle.speed(10)

# def polygon(sides, length):
#   sides = int(sides)
#   for i in range(sides):
#     random_turtle.forward(length)
#     random_turtle.left(360/sides)
# sides = input("how may sides do you want? ")
# length = input("how long do you want each side? ")
# polygon(sides, length) 



#final project
import pygame, sys, time, random

pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Cube.io Game")


cubSize = 20
yellow = (255, 255, 0)
white = (255, 255, 255)
starting_color = (255, 0, 0)
ending_color = (0, 0, 255)
violet = (70, 0, 80)

food = [random.randrange(1, 500), random.randrange(1, 500), 10, 10]
bad_food = [random.randrange(1, 500), random.randrange(1, 500), 10, 10]

speed = 5
cubeX = 250
cubeY = 250
cubeSize = 20

run = True 
while run:
  pygame.time.delay(10)
  window.fill(violet)
  food_status = True
  bad_food_status = True

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False 
      #stop Game

  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    if cubeX >= 400:
      cubeX = 400
    else:
      cubeX += speed
  elif keys[pygame.K_LEFT]:
    if cubeX <= 0:
      cubeX = 0
    else:
      cubeX -= speed
  elif keys[pygame.K_DOWN]:
    if cubeY <= 200:
      cubeY = 200
    else:
      cubeY += speed
  elif keys[pygame.K_UP]:
    if cubeY <= 0:
      cubeY = 0
    else:
      cubeY -= speed
  cube = pygame.Rect(cubeX, cubeY, cubeSize, cubeSize)

  if cubeSize <= 100:
    pygame.draw.rect(window, starting_color, cube)
  else:
    pygame.draw.rect(window, ending_color, cube)
  
  if cube.colliderect(food):
    cubeSize -= 10
    bad_food_status = False


  if food_status == False:
    food = [random.randrage(1, 500), random.randrange(1, 500), 10, 10]

  if bad_food_status == False:
    bad_food = [random.randrage(1, 500), random.randrange(1, 500), 10, 10]

  pygame.draw.rect(window, ending_color, pygame.Rect(food))

  pygame.display.update()
pygame.quit()





