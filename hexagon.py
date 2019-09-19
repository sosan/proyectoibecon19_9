"""
DIBUJAR HEXAGONO CON DECORADORES

"""

import turtle

# decorador donde su funcion es dibujar el hexagono
def decorador_showhexagon(func):
    def tortuga():
        ventana = turtle.Screen()
        tortuguita = turtle.Turtle()
        
        for i in (range(0, 6)):
            tortuguita.forward(100)
            tortuguita.left(60)
        
        turtle.mainloop()
    
    return tortuga

# funcion donde llamamos al decorador para dibujar el hexagon
@decorador_showhexagon
def showhexagon():
    print("completado")

# punto de entrada
if __name__ == '__main__':
    showhexagon()