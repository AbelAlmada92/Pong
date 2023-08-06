import turtle

#Pantalla
s = turtle.Screen()
s.title("Pong en python")
s.bgcolor("black")
s.setup(width = 800, height = 600)
s.tracer(0)

# Marcador de los jugadores
Puntuacion1 = 0
Puntuacion2 = 0

#Jugador 1
Jugador1 = turtle.Turtle()
Jugador1.speed(0)
Jugador1.shape("square")
Jugador1.color("blue")
Jugador1.penup()
Jugador1.goto(-350, 0)
Jugador1.shapesize(stretch_wid=5, stretch_len=1)

#Jugador 2
Jugador2 = turtle.Turtle()
Jugador2.speed(0)
Jugador2.shape("square")
Jugador2.color("red")
Jugador2.penup()
Jugador2.goto(350, 0)
Jugador2.shapesize(stretch_wid=5, stretch_len=1)

#Pelota:
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)

#Velocidad de la pelota
pelota.dx = 1
pelota.dy = 1

#Linea de division:
division = turtle.Turtle()
division.color("white")
division.goto(0, 400)
division.goto(0, -400)

#Puntuacion
puntos = turtle.Turtle()
puntos.speed(0)
puntos.color("white")
puntos.penup()
puntos.hideturtle()
puntos.goto(0, 260)
puntos.write("Jugador1 : 0      JugadorB: 0",align="center", font=("Courier", 24, "normal"))

#Funciones de movimiento:
def jugador1_up():
    y = Jugador1.ycor()
    y += 20
    Jugador1.sety(y)

def jugador1_down():
    y = Jugador1.ycor()
    y -= 20
    Jugador1.sety(y)

def jugador2_up():
    y = Jugador2.ycor()
    y += 20
    Jugador2.sety(y)

def jugador2_down():
    y = Jugador2.ycor()
    y -= 20
    Jugador2.sety(y)

# Teclas a utilizar:
s.listen()
s.onkeypress(jugador1_up, "w")
s.onkeypress(jugador1_down, "s")
s.onkeypress(jugador2_up, "Up")
s.onkeypress(jugador2_down, "Down")

# Bucle de funcionamiento del juego
while True:
    s.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

#Bordes:
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

#Bordes de los lados:
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        Puntuacion1 += 1
        puntos.clear()
        puntos.write("Jugador1 : {}      JugadorB: {}".format(Puntuacion1, Puntuacion2),align="center", font=("Courier", 24, "normal"))
        
    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        Puntuacion2 += 1
        puntos.clear()
        puntos.write("Jugador1 : {}      JugadorB: {}".format(Puntuacion1, Puntuacion2),align="center", font=("Courier", 24, "normal"))
        
    if ((pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < Jugador2.ycor() + 50 and pelota.ycor() > Jugador2.ycor() -50)):
        pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < Jugador1.ycor() + 50 and pelota.ycor() > Jugador1.ycor() -50)):
        pelota.dx *= -1