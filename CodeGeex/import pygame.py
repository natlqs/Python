import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 设置屏幕大小
width = 640
height = 480

# 创建游戏屏幕
screen = pygame.display.set_mode((width, height))

# 设置颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 设置贪吃蛇的初始位置和长度
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = 10

# 设置食物的初始位置
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

# 设置游戏速度
clock = pygame.time.Clock()

while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

       # 获取玩家的输入
       keys = pygame.key.get_pressed()
       for key in keys:
           if keys[pygame.K_UP] and snake_pos[0][1] > 0:
               snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] - snake_speed])
           if keys[pygame.K_DOWN] and snake_pos[0][1] < height:
               snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] + snake_speed])
           if keys[pygame.K_LEFT] and snake_pos[0][0] > 0:
               snake_pos.insert(0, [snake_pos[0][0] - snake_speed, snake_pos[0][1]])
           if keys[pygame.K_RIGHT] and snake_pos[0][0] < width:
               snake_pos.insert(0, [snake_pos[0][0] + snake_speed, snake_pos[0][1]])

   # 检查是否吃到食物
   if snake_pos[0] == food_pos:
       food_spawn = False
   else:
       snake_pos.pop()

   # 检查是否碰到自己或者撞墙
   if snake_pos[0] in snake_pos[1:] or snake_pos[0][0] < 0 or snake_pos[0][0] >= width or snake_pos[0][1] < 0 or snake_pos[0][1] >= height:
       pygame.quit()
       sys.exit()

   # 绘制游戏元素
   screen.fill(black)
   for pos in snake_pos:
       pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_speed, snake_speed))
   pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], snake_speed, snake_speed))

   pygame.display.flip()
   clock.tick(10)

   if not food_spawn:
       food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
       food_spawn = True