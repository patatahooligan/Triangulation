from random import randint, seed
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

    def get_coordinates(self):
        """ Return a tuple of the points x,y.
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

    def get_points(self):
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
            self.imd.point((point.get_coordinates()), fill="black")

    def paint_lines (self, lines):
        """ Draws all the given lines.
        """

        for line in lines:
            (start,end) = line.get_points()
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
        """ Creates given number of points as xy coordinates.
        """

        points = []
        for i in range (no_of_points):
            points.append(Point())

        return points

    def connect(self, point1, point2):
        """ Connects two points on the plane.
        """

        self.lines.append(Line(point1.get_coordinates(), point2.get_coordinates()))

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
