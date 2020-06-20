# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(300, 300, )
# radius = 80
# for _ in range(3):
#     radius += 5
#     sd.circle(point, radius, color=sd.COLOR_RED, width=2)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# def bubble(point, step, color):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         color = sd.random_color()
#         sd.circle(point, radius, color, width=2)
#
#
# color = sd.COLOR_RED
# point = sd.get_point(300, 300, )
#
# bubble(point=point, step=5, color=color)

# Нарисовать 10 пузырьков в ряд
# def bubble(point, step, color):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         color = sd.random_color()
#         sd.circle(point, radius, color, width=2)
#
# color = sd.COLOR_RED

# for x in range(100, 1100, 110):
#     point = sd.get_point(x, 100)
#     bubble(point=point, step=4, color=color)

# Нарисовать три ряда по 10 пузырьков
# for y in range(100, 400, 100):
#     for x in range(100, 1100, 110):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=4, color=color)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    color = sd.random_color()
    point = sd.random_point()
    radius = 50
    for _ in range(3):
        radius += 5
        sd.circle(point, radius, color, width=2)

color = sd.COLOR_RED
point = sd.get_point(300, 300)

sd.pause()
