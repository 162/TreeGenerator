from random import randint


def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5


def push_point(array, point):
    xp = point[0]
    yp = point[1]
    width = point[2]
    for x in range(xp-width, xp+width+1):
        for y in range(yp-width, yp+width+1):
            try:
                if get_distance(xp, yp, x, y) <= width:
                    array[x][y] = 1
            except IndexError:
                pass
    return array


def push_line(array, start, finish, breaks):
    points = [start]
    breaks = int(breaks)
    for i in range(1, breaks):
        points.append([start[0] + i*(finish[0]-start[0])/breaks,
                       start[1] + i*(finish[1]-start[1])/breaks,
                       start[2] + i*(finish[2]-start[2])/breaks])
    points.append(finish)
    for point in points:
        array = push_point(array, point)
    return array


class Brunch():
    def __init__(self, start, finish, width1, width2, breaks, shift):
        self.start = start
        self.finish = finish
        self.width1 = width1
        self.width2 = width2
        self.breaks = int(breaks)
        self.shift = shift
        points = [self.start+[self.width1]]
        for i in range(1, self.breaks):
            points.append([self.start[0] + i*(self.finish[0]-self.start[0])/self.breaks+randint(-self.shift, self.shift),
                           self.start[1] + i*(self.finish[1]-self.start[1])/self.breaks+randint(-self.shift, self.shift),
                           self.width1 - i*(self.width1-self.width2)/self.breaks])
        points.append(self.finish+[self.width2])
        self.points = points

    def push(self, array):
        for i in range(1, len(self.points)):
            array = push_line(array, self.points[i-1], self.points[i], self.breaks)
        return array


