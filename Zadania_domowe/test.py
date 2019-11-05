import turtle
chessboard = turtle.Turtle()
chessboard.speed(8) #szybkosc rysowania szachownicy
for i in range(4): #petla obroci sie 4 razy
    chessboard.forward(900) #idź do przodu
    chessboard.right(90) #idź w prawo
a = 0 #for controlling alternate colors in a row
b = 0 #for controlling alternate colors in a column
for i in range(8): #petla bedzie sie obracac 8 razy bo na planszy mamy 8 rzedów
    if(b == 0):
        a=1
    else:
        a=0
    for j in range(8): #petla bedzie sie obracac 8 razy bo na planszy mamy 8 kolumn
        chessboard.penup()
        chessboard.goto(j*100, i*100*(-1))
        chessboard.pendown()
        if(a==0):
            chessboard.fillcolor('black')
            a=1
        else:
            chessboard.fillcolor('white')
            a=0
        chessboard.begin_fill()
        for k in range(4):
            chessboard.forward(100)
            chessboard.right(90)
        chessboard.end_fill()
    if(b==0):
        b=1
    else:
        b=0