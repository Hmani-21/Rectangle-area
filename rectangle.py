class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    def display_area(self):
        area = self.calculate_area()
        print(f"The area of the rectangle is: {area}")
if __name__ == "__main__":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle = Rectangle(length, width)
    rectangle.display_area()