import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))


font = pg.font.Font(None, 32)
color = (0, 0, 0)
text = ''

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(text)
                text = ''
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

    screen.fill((255, 255, 255))
    txt_surface = font.render(text, True, color)
    screen.blit(txt_surface, (50, 100))

    pygame.display.flip()
    clock.tick(30)
