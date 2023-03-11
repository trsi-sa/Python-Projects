import turtle as tu

tree = tu.Turtle()
wn = tu.Screen()
wn.bgcolor("#000000")
wn.title("Fractal Tree Pattern")
tree.left(90)
tree.speed(2000)

def draw(x):
  if(x < 10):
    return
  else:
    tree.pensize(2)
    tree.pencolor("#DB80BD")
    tree.forward(x)
    tree.left(30)
    draw(3 * x / 4)
    tree.right(60)
    draw(3 * x / 4)
    tree.left(30)
    tree.backward(x)
draw(20)
tree.right(90)
tree.speed(2000)

def draw(x):
  if(x < 10):
    return
  else:
    tree.pensize(2)
    tree.pencolor("#66CDAF")
    tree.forward(x)
    tree.left(30)
    draw(3 * x / 4)
    tree.right(60)
    draw(3 * x / 4)
    tree.left(30)
    tree.backward(x)
draw(20)
tree.left(270)
tree.speed(2000)

def draw(x):
  if(x < 10):
    return
  else:
    tree.pensize(2)
    tree.pencolor("#FFBB94")
    tree.forward(x)
    tree.left(30)
    draw(3 * x / 4)
    tree.right(60)
    draw(3 * x / 4)
    tree.left(30)
    tree.backward(x)
draw(20)
tree.right(90)
tree.speed(2000)

def draw(x):
  if(x < 10):
    return
  else:
    tree.pensize(2)
    tree.pencolor("#7C80AD")
    tree.forward(x)
    tree.left(30)
    draw(3 * x / 4)
    tree.right(60)
    draw(3 * x / 4)
    tree.left(30)
    tree.backward(x)
draw(20)

def draw(x):
  if(x <10):
    return
  else:
    tree.pensize(4)
    tree.pencolor("#7C80AD")
    tree.forward(x)
    tree.left(30)
    draw(4 * x / 5)
    tree.right(60)
    draw(4 * x / 5)
    tree.left(30)
    tree.backward(x)
draw(40)
tree.right(90)
tree.speed(2000)

def draw(x):
  if(x <10):
    return
  else:
    tree.pensize(4)
    tree.pencolor("#DB80BD")
    tree.forward(x)
    tree.left(30)
    draw(4 * x / 5)
    tree.right(60)
    draw(4 * x / 5)
    tree.left(30)
    tree.backward(x)
draw(40)
tree.left(270)
tree.speed(2000)

def draw(x):
  if(x <10):
    return
  else:
    tree.pensize(4)
    tree.pencolor("#66CDAF")
    tree.forward(x)
    tree.left(30)
    draw(4 * x / 5)
    tree.right(60)
    draw(4 * x / 5)
    tree.left(30)
    tree.backward(x)
draw(40)
tree.right(90)
tree.speed(2000)

def draw(x):
  if(x <10):
    return
  else:
    tree.pensize(4)
    tree.pencolor("#FFBB94")
    tree.forward(x)
    tree.left(30)
    draw(4 * x / 5)
    tree.right(60)
    draw(4 * x / 5)
    tree.left(30)
    tree.backward(x)
draw(40)

def draw(x):
  if(x < 10):
    return
  else:
    tree.pensize(2)
    tree.pencolor("#FFBB94")
    tree.forward(x)
    tree.left(30)
    draw(4 * x / 5)
    tree.right(60)
    draw(4 * x / 5)
    tree.left(30)
    tree.backward(x)
draw(60)
tree.right(90)
tree.speed(2000)

def draw(x):
  if(x < 10):
    return
  else:
    tree.pensize(2)
    tree.pencolor("#7C80AD")
    tree.forward(x)
    tree.left(30)
    draw(4 * x / 5)
    tree.right(60)
    draw(4 * x / 5)
    tree.left(30)
    tree.backward(x)
draw(60)
tree.left(270)
tree.speed(2000)

def draw(x):
  if(x < 10):
    return
  else:
    tree.pensize(2)
    tree.pencolor("#DB80BD")
    tree.forward(x)
    tree.left(30)
    draw(4 * x / 5)
    tree.right(60)
    draw(4 * x / 5)
    tree.left(30)
    tree.backward(x)
draw(60)
tree.right(90)
tree.speed(2000)

def draw(x):
  if(x < 10):
    return
  else:
    tree.pensize(2)
    tree.pencolor("#66CDAF")
    tree.forward(x)
    tree.left(30)
    draw(4 * x / 5)
    tree.right(60)
    draw(4 * x / 5)
    tree.left(30)
    tree.backward(x)
draw(60)
wn.exitonclick()