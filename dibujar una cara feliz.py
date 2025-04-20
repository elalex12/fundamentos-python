import turtle
# configuracion de la pantalla y la library turtle que se usara
turtle.setup(width=400, height=400)
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()

#se inicia el proceso de dibujo de la cara
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.pencolor("white")
turtle.pensize(2)
turtle.circle(100)

# se empieza el dibujo de los ojos
turtle.penup()
turtle.goto(-30, 50)
turtle.pendown()
turtle.pencolor("light blue")
turtle.circle(10)
turtle.penup()
turtle.goto(30, 50)
turtle.pendown()
turtle.pencolor("orange")
turtle.circle(10)

#se finaliza con el dibujo de la boca
turtle.penup()
turtle.goto(-25, -25)
turtle.pendown()
turtle.pencolor("yellow")
turtle.setheading(-90)
turtle.begin_poly()
turtle.circle(30, 180)
turtle.end_poly()

#se finaliza al completo
turtle.done()