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
            None
        """
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError("Length and width must be numeric values.")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive.")
        
        self.length = length
        self.width = width
    
    def area(self):
        # Logical error: Incorrect formula for area.
        return self.length * self.length  # Should be self.length * self.width.

    def perimeter(self):
        # Logical error: Incorrect formula for perimeter.
        return 2 * self.length * self.length  # Should be 2 * (self.length + self.width).

class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a numeric value.")
        if radius < 0:
            raise ValueError("Radius must be non-negative.")
        
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if not all(isinstance(side, (int, float)) for side in [side1, side2, side3]):
            raise TypeError("All sides must be numeric values.")
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All sides must be positive.")
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("The provided sides do not form a valid triangle.")
        
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        # Use Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Example usage
if __name__ == "__main__":
    try:
        rect = Rectangle(10, -5)  # Should raise a ValueError.
        print("Rectangle Area:", rect.area())
        print("Rectangle Perimeter:", rect.perimeter())
    except Exception as e:
        print("Error with Rectangle:", e)
    
    try:
        circle = Circle("seven")  # Should raise a TypeError.
        print("\nCircle Area:", circle.area())
        print("Circle Perimeter:", circle.perimeter())
    except Exception as e:
        print("Error with Circle:", e)
    
    try:
        triangle = Triangle(1, 2, 10)  # Should raise a ValueError (not a valid triangle).
        print("\nTriangle Area:", triangle.area())
        print("Triangle Perimeter:", triangle.perimeter())
    except Exception as e:
        print("Error with Triangle:", e)
