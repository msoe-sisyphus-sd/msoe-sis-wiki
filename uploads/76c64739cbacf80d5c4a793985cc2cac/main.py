import math
import matplotlib.pyplot as plt

def get_circe_intersection(y):
    x = math.sqrt(1 - math.pow(y, 2))
    return (-1 * x, x)


def convert_rectangular_to_polar(p):
    rho = math.sqrt(math.pow(p[0], 2) + math.pow(p[1], 2))
    theta = math.acos(p[0] / rho)
    if p[1] < 0:
        theta *= -1
    theta -= math.pi / 2
    # if theta < -(math.pi / 2): then +2pi since it's always left hand
    return (theta, rho)

def main():
    HEIGHT = 2.0
    SECTIONS = 75 # needs to be odd
    POINTS_PER_DISTANCE = 20
    points = []
    min_distance = None
    section_height = HEIGHT / SECTIONS
    y_pos = 1 - section_height
    ltr = True
    while (y_pos > -1):
        (left, right) = get_circe_intersection(y_pos)
        section_width = right - left
        if min_distance is None or section_width < min_distance:
            min_distance = section_width
        section_step = min_distance / POINTS_PER_DISTANCE
        point = (left, y_pos)
        if not ltr:
            point = (right, y_pos)
        if ltr:
            while point[0] < right:
                points.append(point)
                point = (point[0] + section_step, y_pos)
        else:
            while point[0] > left:
                points.append(point)
                point = (point[0] - section_step, y_pos)
        y_pos = y_pos - section_height
        ltr = not ltr
    for i in range(len(points)):
        tr_point = convert_rectangular_to_polar(points[i])
        points[i] = tr_point
    print(points)
    (x, y) = zip(*points)
    # circ = plt.Circle((0, 0), 1, color='r', alpha=0.05)
    # fig, ax = plt.subplots()
    # ax.axhline(y=0, color='k')
    # ax.axvline(x=0, color='k')
    # ax.add_artist(circ)
    # ax.scatter(x, y)
    # ax.plot(x, y)
    # plt.polar(x, y)
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='polar')
    # c = ax.scatter(x, y)
    # plt.show()
    with open('lateral-erase.thr', 'w') as theta_rho_file:
        theta_rho_file.write('# Lateral Erase\n')
        for point in points:
            theta_rho_file.write(f'{point[0]} {point[1]}\n')

if __name__ == '__main__':
    main()
