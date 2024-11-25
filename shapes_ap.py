import math

class Shape:
    """Base class for different shapes."""
    def area(self):
        """Compute the area of the shape."""
        raise NotImplementedError("This method should be overridden in subclasses.")
    
    def perimeter(self):
        """Compute the perimeter of the shape."""
        raise NotImplementedError("This method should be overridden in subclasses.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a rectangle object.
        
        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        
        Returns:
            None: This method initializes the object and does not return anything.
        """
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 2 * self.length * self.length
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        """Initialize a new triangle object with three sides.
        
        Args:
            side1 (float): The length of the first side of the triangle.
            side2 (float): The length of the second side of the triangle.
            side3 (float): The length of the third side of the triangle.
        
        Returns:
            None: This method initializes the object and does not return anything.
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        # Use Heron's formula
        """Calculate the area of a triangle using Heron's formula.
        
        This method computes the area of a triangle using Heron's formula, which calculates
        the area based on the semi-perimeter and the lengths of the three sides.
        
        Returns:
            float: The area of the triangle.
        
        Note:
            This method assumes that the triangle's side lengths are stored as attributes
            (side1, side2, side3) and that a perimeter() method exists to calculate
            the triangle's perimeter.
        """
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Example usage
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print("Rectangle Area:", rect.area())
    print("Rectangle Perimeter:", rect.perimeter())

    circle = Circle(7)
    print("\nCircle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())

    triangle = Triangle(3, 4, 5)
    print("\nTriangle Area:", triangle.area())
    print("Triangle Perimeter:", triangle.perimeter())