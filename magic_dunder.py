#https://www.w3schools.com/python/python_magic_methods.asp

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Emil", 36)
# print(p1)   #  <__main__.Person object at 0x7306e3d22900>


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

  def __repr__(self):
    return f"Person('{self.name}', {self.age})"

p1 = Person("Tobias", 25)
print(p1)   # Tobias (25)


print(repr(p1))





class ClickCounter:
  def __init__(self):
    self.clicks = 0

  def __call__(self):
    self.clicks += 1
    return self.clicks

button_clicks = ClickCounter()

print(button_clicks())
print(button_clicks())
print(button_clicks())