import pygame

pygame.init()

screen = pygame.display.set_mode((1024, 480))  # 设置窗口的大小
background = pygame.Surface(screen.get_size())  # 创建一个surface，名字叫background，大小和screen一样
background.fill((255, 255, 255))  # 用白色填充background；255,255,255是RGB的白色
background = background.convert()  # 对background进行convert()，可以加快后面添加时速度
screen.blit(background, (0, 0))

clock = pygame.time.Clock()  # 创建clock对象
FPS = 30  # 定义帧率的上限，就是帧率的最大值

mainloop = True

while mainloop:
    clock.tick(FPS)  # 设置最大帧率

    for event in pygame.event.get():  # 这一部分就是事件处理
        if event.type == pygame.QUIT:  # 如果按下右上角的叉叉
            mainloop = False  # 退出主循环
        elif event.type == pygame.KEYDOWN:  # 如果按下了键盘
            if event.key == pygame.K_ESCAPE:  # 而且按下的还是ESC键
                mainloop = False  # 退出主循环

    # 在这里做一些游戏相关的运算，这里暂时省略
    text = "FPS: {0:.2f}".format(clock.get_fps())
    pygame.display.set_caption(text)

    pygame.display.flip()  # 刷新显示

pygame.quit()
