class Shape {
    // Base class for shapes
    area() {
        throw new Error("Method 'area()' must be implemented.");
    }

    perimeter() {
        throw new Error("Method 'perimeter()' must be implemented.");
    }
}

class Rectangle extends Shape {
    constructor(length, width) {
        super();
        this.length = length;
        this.width = width;
    }

    area() {
        return this.length * this.width;
    }

    perimeter() {
        return 2 * (this.length + this.width);
    }
}

class Circle extends Shape {
    constructor(radius) {
        super();
        this.radius = radius;
    }

    area() {
        return Math.PI * this.radius ** 2;
    }

    perimeter() {
        return 2 * Math.PI * this.radius;
    }
}

class Triangle extends Shape {
    constructor(side1, side2, side3) {
        super();
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
    }

    area() {
        const s = this.perimeter() / 2;
        return Math.sqrt(s * (s - this.side1) * (s - this.side2) * (s - this.side3));
    }

    perimeter() {
        return this.side1 + this.side2 + this.side3;
    }
}

// Example usage
const rect = new Rectangle(10, 5);
console.log("Rectangle Area:", rect.area());
console.log("Rectangle Perimeter:", rect.perimeter());

const circle = new Circle(7);
console.log("\nCircle Area:", circle.area());
console.log("Circle Perimeter:", circle.perimeter());

const triangle = new Triangle(3, 4, 5);
console.log("\nTriangle Area:", triangle.area());
console.log("Triangle Perimeter:", triangle.perimeter());