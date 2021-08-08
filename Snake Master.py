import pygame as pg
import random

pg.init()

# Background music
pg.mixer.init()
pg.mixer.music.load('bg.mp3')
pg.mixer.music.play()

# Background img
bgimg = pg.image.load("img.png")
bgimg = pg.transform.scale(bgimg, (800, 500))

# Game Window
window = pg.display.set_mode((800, 500))
pg.display.set_caption('Snake Master')
pygame_icon = pg.image.load('snake.png')
pg.display.set_icon(pygame_icon)

# Colors
black = (0, 0, 0)
blue = (0, 128, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Others
clock = pg.time.Clock()
font = pg.font.SysFont('Algerian', 35)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x, y])


def plot_snake(window, color, snake_list, snake_size):
    for x, y in snake_list:
        pg.draw.rect(window, color, [x, y, snake_size, snake_size])


# Main loop
def gameloop():

    # GAME SPECIFIC VARIABLES

    exit_game = False
    game_over = False

    # snake
    x_snake_pos = 400
    y_snake_pos = 250
    snake_size = 20
    velocity_x = 0  # initial velocity in x axis
    velocity_y = 0  # initial velocity in y axis
    snake_list = []
    snake_length = 1

    # food
    food_x = random.randint(0, 780)  # here 780 is the max width of screen up till food can be kept
    food_y = random.randint(0, 480)  # here 480 is the max width of screen up till food can be kept

    # score
    score = 0

    # GAME PROCESSING
    while not exit_game:
        if game_over:
            # window.fill(black) --> ## used earlier when img not uploaded

            # game over image
            over_img = pg.image.load("img_1.png")
            over_img = pg.transform.scale(over_img, (800, 500))
            window.blit(over_img, (0, 0))

            text_screen("Your Score: " + str(score), blue, 300, 350)  # printing score
            text_screen('Press ENTER to continue', red, 200, 400)  # here 150 n 350 are pos.of 'game over' text

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit_game = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        pg.mixer.music.load('bg.mp3')  # music will played again when 'enter' is pressed
                        pg.mixer.music.play()
                        gameloop()

        else:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit_game = True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        velocity_x = 6  # it represents the velocity of snake in both axis when pressed right key
                        velocity_y = 0

                    if event.key == pg.K_LEFT:
                        velocity_x = -6  # it represents the velocity of snake in both axis when pressed left key
                        velocity_y = 0

                    if event.key == pg.K_UP:
                        velocity_y = -6  # it represents the velocity of snake in both axis when pressed up key
                        velocity_x = 0

                    if event.key == pg.K_DOWN:
                        velocity_y = 6  # it represents the velocity of snake in both axis when pressed down key
                        velocity_x = 0

            x_snake_pos += velocity_x
            y_snake_pos += velocity_y

            if abs(x_snake_pos - food_x) < 15 and abs(y_snake_pos - food_y) < 15:
                score += 10
                food_x = random.randint(0, 780)  # here 780 is the max width of screen up till food can be kept
                food_y = random.randint(0, 480)  # here 480 is the max width of screen up till food can be kept
                snake_length += 5

            # MAIN GAME

            # window.fill(black) --> ## used earlier when img not uploaded
            window.blit(bgimg, (0, 0))

            text_screen("Score: " + str(score), green, 605, 5)  # printing score
            plot_snake(window, red, snake_list, snake_size)  # creating snake

            # snake after eating food
            head = [x_snake_pos, y_snake_pos]
            snake_list.append(head)

            # increase in snake length
            if len(snake_list) > snake_length:
                del snake_list[0]

            # Collision of snake with itself
            if head in snake_list[:-1]:
                pg.mixer.music.load('explosion.wav')
                pg.mixer.music.play()
                game_over = True

            # Collision of snake with boundary
            if x_snake_pos < 0 or x_snake_pos > 780 or y_snake_pos < 0 or y_snake_pos > 480:
                pg.mixer.music.load('explosion.wav')
                pg.mixer.music.play()
                game_over = True

            pg.draw.circle(window, blue, [food_x, food_y], 8)  # creating food

        pg.display.update()
        clock.tick(30)  # frames per sec. of the snake which it will move

    pg.quit()
    quit()


gameloop()
