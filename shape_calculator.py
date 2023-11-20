class Rectangle:

  def __init__(self, width, heigth):
    self.width = width
    self.heigth = heigth

  def set_width(self, width):
    self.width = width

  def set_height(self, heigth):
    self.heigth = heigth

  def get_width(self):
    return self.width

  def get_height(self):
    return self.heigth

  def get_area(self):
    return self.width * self.heigth

  def get_perimeter(self):
    return 2 * (self.width + self.heigth)

  def get_diagonal(self):
    return (self.width**2 + self.heigth**2)**0.5

  def get_picture(self):
    if self.width > 50 or self.heigth > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.heigth):
        picture += "*" * self.width + "\n"
    return picture

      ##print(picture, "rectangle")

  def get_amount_inside(self, shape):
    if shape.get_area() > self.get_area():
      return 0
    else:
      return int(self.get_area() / shape.get_area())

  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.get_width(),
                                                   self.get_height())


class Square(Rectangle):

  def __init__(self, side):
    self.side = side

  def set_side(self, s):
    self.side = s

  def set_width(self, s):
    self.side = s

  def set_heigth(self, s):
    self.side = s

  def get_side(self):
    return self.side

  def get_area(self):
    return self.side**2

  def get_perimeter(self):
    return 4 * self.side

  def get_diagonal(self):
    return ((2 * self.side**2)**0.5)

  def get_picture(self):
    picture = ""
    if self.side > 50:
      return "Too big for picture."
    else:
      for i in range(self.side):
          picture += "*" * self.side + "\n"
    return picture

    ##print(picture, "picture")

  def get_amount_inside(self, shape):
    if shape.get_area() > self.get_area():
      return 0
    else:
      return int(self.get_area() / shape.get_area())

  def __str__(self):
    return "Square(side={})".format(self.get_side())


class ShapeCalculator:

  def __init__(self):
    self.shapes = []

  def __str__(self):
    return "Shape Calculator"

  def get_total_area(self, shapes):
    total_area = 0
    for shape in shapes:
      total_area += shape.get_area()
    return total_area
