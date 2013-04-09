from random import randint, seed
from copy import copy
import Image
import ImageDraw


class Point(object):
    """ A single point on the plane
    """

    def __init__(self, x=None, y=None):
        """ Creates a point from given coordinates. If none are given, randomly generate them.
	"""

        if x is None:
            x = randint (0,500)
        if y is None:
            y = randint (0,500)

        (self.x, self.y) = (x, y)

    @property
    def coordinates(self):
        """ Return a tuple of the point's x,y.
        """

        return (self.x, self.y)

    def __str__(self):
        """ Prints the Point in a (x,y) format.
        """

        return "("+str(self.x)+","+str(self.y)+")"


class Line(object):
    """ A single line on the plane. Starting and ending point are given as (x,y) tuples.
    """

    def __init__(self, start, end):
        """
	"""
        self.start = start
        self.end = end

    @property
    def points(self):
        """ Returns a tuple of the start and end coordinates in the form of
        ((startx,starty),(endx,endy))
        """

        return (self.start, self.end)


class Graph(object):
    """ Graphical representation of the Plane
    """

    def __init__(self, dims = (500,500)):
        """ Creates a blank image and awaits further instructions.
	"""

        self.im = Image.new("1", dims, color="white")
        self.imd = ImageDraw.Draw(self.im)

    def paint_points(self, points):
        """ Draws all the given points
        """

        for point in points:
            self.imd.point((point.coordinates), fill="black")

    def paint_lines (self, lines):
        """ Draws all the given lines.
        """

        for line in lines:
            (start,end) = line.points
            self.imd.line([start,end], fill="black")

    def show(self):
        """ Show the image
        """

        self.im.show()


class Plane(object):
    """ Creates and holds all the points. Is also the key to the universe
    """

    def __init__(self, no_of_points=100, size=(500,500)):
        """
	"""

        seed()                  # Initialize the random seed
        self.size = size
        self.points = self.create_points (no_of_points)
        self.lines = []

    def create_points(self, no_of_points):
        """ Creates given number of points with random coordinates.
        """

        points = []
        for i in range (no_of_points):
            points.append(Point())

        return points

    def connect(self, point1, point2):
        """ Connects two points on the plane.
        """

        self.lines.append(Line(point1.coordinates, point2.coordinates))

    def compute_convex_hull(self):
        """ Compute the convex hull of all the points on the plane
        """

        # Sort all points by their x coordinate
        self.points.sort(key=lambda x:x.coordinates[0])

        # Start calculating the upper and lower parts of the hull from
        # the rightmost and leftmost points respectively
        upper_hull = [self.points[0]]
        lower_hull = [self.points[-1]]

        for i in range(1, len(self.points)):
            if len(upper_hull) > 1:
                (x,y) = self.points[i].coordinates
                (prevx, prevy) = upper_hull[-1].coordinates
                (Ox, Oy) = upper_hull[-2].coordinates

                while (prevy-Oy)*(x-Ox) >= (y-Oy)*(prevx-Ox):
                    upper_hull.pop()
                    if len(upper_hull)<2:
                        break
                    else:
                        (prevx, prevy) = upper_hull[-1].coordinates
                        (Ox, Oy) = upper_hull[-2].coordinates
            upper_hull.append(self.points[i])

            if len(lower_hull) > 1:
                (x,y) = self.points[i].coordinates
                (prevx, prevy) = lower_hull[-1].coordinates
                (Ox, Oy) = lower_hull[-2].coordinates

                while (prevy-Oy)*(x-Ox) >= (y-Oy)*(prevx-Ox):
                    lower_hull.pop()
                    if len(lower_hull)<2:
                        break
                    else:
                        (prevx, prevy) = lower_hull[-1].coordinates
                        (Ox, Oy) = lower_hull[-2].coordinates
            lower_hull.append(self.points[i])

            # TODO : add lower_hull part

        for i in range (1, len(upper_hull)):
            start = upper_hull[i-1].coordinates
            end = upper_hull[i].coordinates
            self.lines.append(Line(start,end))

        for i in range (1, len(lower_hull)):
            start = lower_hull[i-1].coordinates
            end = lower_hull[i].coordinates
            self.lines.append(Line(start,end))

    def show_points(self):
        """ Creates and displays an image with all the points of the plane.
        """

        graph = Graph(self.size)
        graph.paint_points(self.points)
        graph.show()

    def show_shape(self):
        """ Creates an image with all the points and lines on the plane.
        """

        graph = Graph(self.size)
        graph.paint_points(self.points)
        graph.paint_lines(self.lines)
        graph.show()

    def __str__(self):
        """ Prints all the points on the plane.
        """

        ret = ""
        for point in self.points:
            ret += " "+str(point)
        return ret
