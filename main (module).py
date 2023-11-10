#import mymodule as area
#from mymodule import area_of_square,area_of_triangle

from mathematic.circle.area import circle_area
from mathematic.triangle.area import triangle_area
from mathematic.square.area import square_area
from mathematic.circle.perimeter import circle_perimeter
from mathematic.triangle.perimeter import triangle_perimeter
from mathematic.square.perimeter import square_perimeter

circle_area(4)
circle_perimeter(4)
square_area(4)
square_perimeter(4)
triangle_area(4,4)
triangle_perimeter(4,4,4)

