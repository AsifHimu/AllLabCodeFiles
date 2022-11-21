import pygame

pygame.init()
win = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Bezier Curve")

f = pygame.font.get_fonts()[0]
font = pygame.font.SysFont(f, 32)

point_text_0 = font.render("P0", True, (255, 255, 255))
point_text_1 = font.render("P1", True, (255, 255, 255))
point_text_2 = font.render("P2", True, (255, 255, 255))
point_text_3 = font.render("P3", True, (255, 255, 255))

text_rect_0 = point_text_0.get_rect()
text_rect_1 = point_text_0.get_rect()
text_rect_2 = point_text_0.get_rect()
text_rect_3 = point_text_0.get_rect()

p0 = 100.0, 500.0
p1 = 200.0, 100.0
p2 = 600.0, 80.0
p3 = 650.0, 410.0

speed = 0.004
t = 0

run = True
while run:
    for event in pygame.event.get():
        pygame.time.delay(70)
        if event.type == pygame.QUIT:
            run = False
    while t < 1:
        t += speed
        bz0 = (pow(1-t, 3)) * p0[0], (pow(1-t, 3)) * p0[1]
        bz1 = (pow(1-t, 2)) * t * 3 * p1[0], (pow(1-t, 2)) * t * 3 * p1[1]
        bz2 = 3 * t * t * (1-t) * p2[0], 3 * t * t * (1-t) * p2[1]
        bz3 = (pow(t, 3)) * p3[0], (pow(t, 3)) * p3[1]

        p = bz0[0] + bz1[0] + bz2[0] + bz3[0], bz0[1] + bz1[1] + bz2[1] + bz3[1]
        x, y = round(p[0]), round(p[1])

        text_rect_0.center = p0
        text_rect_1.center = p1
        text_rect_2.center = p2
        text_rect_3.center = p3

        win.blit(point_text_0, text_rect_0)
        win.blit(point_text_1, text_rect_1)
        win.blit(point_text_2, text_rect_2)
        win.blit(point_text_3, text_rect_3)

        pygame.draw.line(win, (255, 0, 0), p0, p1, 1)
        pygame.draw.line(win, (0, 255, 0), p2, p3, 1)
        pygame.draw.circle(win, (0, 0, 255), (x, y), 1)

        pygame.display.update()

pygame.quit()