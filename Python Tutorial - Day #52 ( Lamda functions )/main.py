# def fibonacci(n):
#   a = 0
#   b = 1
#   for _ in range(n):
#     print(a,end=" ")
#     a , b = b , a+b #Python evaluates right side and then assigns values to left side.

# fibonacci(4)

def akl(sqr, value):
  return sqr(value) # sqr has got x*x function and value 2, so it applies x*x on 2.

# avg = lambda a,b : (a+b)/2
# cube = lambda y: y*y*y

# print(cube(3))
# print(avg(4,5))

print(akl(lambda x: x*x ,2))
