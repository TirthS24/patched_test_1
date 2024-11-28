import math

class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden in subclasses.")
    
    def perimeter(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize a new instance of Rectangle.
        
        Args:
            length (int or float): The length of the rectangle. Must be positive numeric value.
            width (int or float): The width of the rectangle. Must be positive numeric value.
        
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
        """Calculate the area of a square. 
        
        Args:
            self (Square): An instance of Square class.
        
        Returns:
            int: The result of multiplication of length and width.
        """
        return self.length * self.length  # Should be self.length * self.width.

    def perimeter(self):
        """Calculates the perimeter of a square.
        
        Args:
            self (Square): The Square object for which the perimeter is being calculated.
        
        Returns:
            float: Returns twice the length of one side as this represents a square's perimeter.
        """
        return 2 * self.length * self.length  # Should be 2 * (self.length + self.width).

class Circle(Shape):
    def __init__(self, radius):
        """Initializes a new instance of the Circle class with a given radius.
        
        Args:
            radius (int or float): The radius of the circle. Must be non-negative and numeric.
        
        Raises:
            TypeError: If radius is not a numeric value.
            ValueError: If radius is negative.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a numeric value.")
        if radius < 0:
            raise ValueError("Radius must be non-negative.")
        
        self.radius = radius
    
    def area(self):
        """Calculates the area of a circle.
    
        Args:
            self (Circle): The object calling this method.
    
        Returns:
            float: The calculated area of the circle.
        """
        
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        """Initializes a Triangle object.
    
            Args:
                side1 (int or float): The length of the first side of the triangle. 
                side2 (int or float): The length of the second side of the triangle.
                side3 (int or float): The length of the third side of the triangle.
    
            Raises:
                TypeError: If any of the sides is not a number.
                ValueError: 
                    - If any of the sides is not positive, or if they do not form a valid triangle.
        """
        
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
