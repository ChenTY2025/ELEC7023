def draw_rainbow():
    import turtle as t
    c = ["red","orange","yellow","green","blue","cyan","violet"]
    t.speed(10)
    t.pensize(20)

    for i in range(7):
        t.penup()
        t.goto(-100+i*20,0)
        t.setheading(90)
        t.color(c[i])
        t.pendown()
        t.circle(-200+i*20,180)


def draw_seashell():
    import turtle
    p = turtle.Pen()
   
    p.pensize(5)
    p.pencolor('blue')
    p.speed(0)
    for i in range(15):
        p.circle(i*15)
   
    turtle.done()


print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for rainbow, 2 for shell)\n"
              "Your selection is: ")
    #try:
    a = eval(a)
    if a == 1:
        draw_rainbow()
    elif a == 2:
        draw_seashell()
    else:
        print("Please input the value in [1,2]")
    #except:
        #print("Please input the value in [1,2]")
