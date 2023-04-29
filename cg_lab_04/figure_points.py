# This Python file uses the following encoding: utf-8
import math

def four_sim_points(dot, centre):
    return [(dot[0], dot[1]), (dot[0], 2 * centre[1] - dot[1]), (2 * centre[0] - dot[0], dot[1]), (2 * centre[0] - dot[0], 2 * centre[1] - dot[1])]

def eighth_sim_points(dot, centre):
    sim_points = list()
    sim_points += four_sim_points(dot, centre)
    sim_points += [(dot[1] - centre[1] + centre[0], dot[0] - centre[0] + centre[1]),
                    (-dot[1] + centre[1] + centre[0], dot[0] - centre[0] + centre[1]),
                    (dot[1] - centre[1] + centre[0], -dot[0] + centre[0] + centre[1]),
                    (-dot[1] + centre[1] + centre[0], -dot[0] + centre[0] + centre[1])]

    return sim_points

def draw_circle_canon(centre, radius):
    points = []
    r_square = radius ** 2
    end = round(centre[0] + radius / math.sqrt(2))


    for x in range(centre[0], end + 1):
        y = round(centre[1] + math.sqrt(r_square - (x - centre[0]) ** 2))
        points += eighth_sim_points([x, y], centre)

    return points

def draw_ellipse_canon(centre, radius_x, radius_y):
    rx_sqr = radius_x ** 2
    ry_sqr = radius_y ** 2

    points = list()

    print(centre)
    print(centre[0], centre[0] + radius_x + 1)
    for x in range(centre[0], centre[0] + radius_x + 1):
        y = round((ry_sqr - (ry_sqr * (x - centre[0]) ** 2) / rx_sqr) ** 0.5 + centre[1])
        points += four_sim_points([x, y], centre)

    for y in range(centre[1], centre[1] + radius_y + 1):
        x = round((rx_sqr - (rx_sqr * (y - centre[1]) ** 2) / ry_sqr) ** 0.5 + centre[0])
        points += four_sim_points([x, y], centre)

    return points
def draw_circle_param(centre, radius):
    points = list()

    step = 1 / radius
    angle = math.pi / 2

    while (angle >= math.pi / 4 - step):
        x = round(centre[0] + radius * math.cos(angle))
        y = round(centre[1] + radius * math.sin(angle))

        points += eighth_sim_points([x, y], centre)

        angle -= step

    return points

def draw_ellipse_param(centre, radius_x, radius_y):
    points = list()

    step = 1 / max(radius_x, radius_y)
    angle = 0

    while (angle <= math.pi / 2 + step):
        x = round(centre[0] + radius_x * math.cos(angle))
        y = round(centre[1] + radius_y * math.sin(angle))

        points += four_sim_points([x, y], centre)

        angle += step

    return points
def draw_circle_bresenham(centre, radius):
    points = list()
    x, y = 0, radius
    delta = 2 * (1 - radius)

    points += eighth_sim_points([x + centre[0], y + centre[1]], centre)
    while x < y:
        d1 = 2 * delta + 2 * y - 1
        if d1 < 0:
            x += 1
            delta += 2 * x + 1
        else:
            x += 1
            y -= 1
            delta += 2 * (x - y + 1)
        points += eighth_sim_points([x + centre[0], y + centre[1]], centre)
    return points
def draw_ellipse_bresenham(centre, radius_x, radius_y):
    points = list()
    x, y = 0, radius_y
    rx_sqr, ry_sqr = radius_x ** 2, radius_y ** 2
    delta = ry_sqr - rx_sqr * (2 * radius_y + 1)

    points += four_sim_points([x + centre[0], y + centre[1]], centre)
    while y >= 0:
        if delta < 0:
            d1 = 2 * delta + rx_sqr * (2 * y + 2)
            x += 1

            if d1 < 0:
                delta += ry_sqr * (2 * x + 1)
            else:
                y -= 1
                delta += ry_sqr * (2 * x + 1) + rx_sqr * (1 - 2 * y)
        elif delta > 0:
            d2 = 2 * delta + ry_sqr * (2 - 2 * x)
            y -= 1

            if d2 > 0:
                delta += rx_sqr * (1 - 2 * y)
            else:
                x += 1
                delta += ry_sqr * (2 * x + 1) + rx_sqr * (1 - 2 * y)
        else:
            y -= 1
            x += 1
            delta += ry_sqr * (2 * x + 1) + rx_sqr * (1 - 2 * y)

        points += four_sim_points([x + centre[0], y + centre[1]], centre)

    return points

#
def draw_circle_mid_point(centre, radius):
    points = list()
    x, y = 0, radius
    delta = round(1 - radius)

    points += eighth_sim_points([x + centre[0], y + centre[1]], centre)
    while x < y:
        if delta < 0:
            x += 1
            delta += 2 * x + 1
        else:
            x += 1
            y -= 1
            delta += 2 * (x - y) + 1
        points += eighth_sim_points([x + centre[0], y + centre[1]], centre)

    return points


def draw_ellipse_mid_point(centre, radius_x, radius_y):
    points = list()
    x, y = 0, radius_y
    rx_sqr, ry_sqr = radius_x ** 2, radius_y ** 2

    end = round(radius_x / math.sqrt(1 + ry_sqr / rx_sqr))
    delta = ry_sqr - round(rx_sqr * (radius_y - 1 / 4))

    points += four_sim_points([x + centre[0], y + centre[1]], centre)
    while x <= end:
        if delta < 0:
            x += 1
            delta += 2 * ry_sqr * x + 1
        else:
            x += 1
            y -= 1
            delta += 2 * ry_sqr * x - 2 * rx_sqr * y + 1
        points += four_sim_points([x + centre[0], y + centre[1]], centre)

    x, y = radius_x, 0

    end = round(radius_y / math.sqrt(1 + rx_sqr / ry_sqr))
    delta = rx_sqr - round(ry_sqr * (radius_x - 1 / 4))

    points += four_sim_points([x + centre[0], y + centre[1]], centre)
    while y <= end:
        if delta < 0:
            y += 1
            delta += 2 * rx_sqr * y + 1
        else:
            x -= 1
            y += 1
            delta += 2 * rx_sqr * y - 2 * ry_sqr * x + 1
        points += four_sim_points([x + centre[0], y + centre[1]], centre)

    return points
