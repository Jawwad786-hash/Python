print("Mohd.Jawwad Ali Farooqui, USN:1AY24AI070, SEC:O")
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height
class Circle:
    def __init__(self, center, radius):
        self.center = center  # Point
        self.radius = radius
def distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

def point_in_circle(circle, point):
    """Return True if point lies in or on the circle"""
    return distance(circle.center, point) <= circle.radius
def get_rect_corners(rect):
    """Return list of 4 corner points of the rectangle"""
    x, y = rect.corner.x, rect.corner.y
    return [
        Point(x, y), 
        Point(x + rect.width, y), 
        Point(x, y + rect.height),
        Point(x + rect.width, y + rect.height) 
    ]
def rect_in_circle(circle, rect):
    """Return True if all corners of rect lie in or on circle"""
    return all(point_in_circle(circle, corner) for corner in get_rect_corners(rect))
def rect_circle_overlap(circle, rect):
    """Return True if any corner of rect lies inside circle"""
    return any(point_in_circle(circle, corner) for corner in get_rect_corners(rect))
circle = Circle(Point(150, 100), 75)
rect1 = Rectangle(Point(120, 80), 40, 30)  
rect2 = Rectangle(Point(100, 50), 100, 100) 
rect3 = Rectangle(Point(300, 300), 20, 20)  
print("rect1 is inside circle:", rect_in_circle(circle, rect1))          
print("rect2 is inside circle:", rect_in_circle(circle, rect2))            
print("rect2 overlaps circle:", rect_circle_overlap(circle, rect2))        
print("rect3 overlaps circle:", rect_circle_overlap(circle, rect3))        
