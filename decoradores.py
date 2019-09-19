""""
decoradores
Funciones que a su vez añaden funcionalidades a otras funciones
Decorar anotras funcionenes añadienco funcionalidades

Estructura de un decorador:
3 funciones(A, B, C)
A RECIBE COMO PARAMETRO B PARA DEVOLVER C


def A(B):
    return C
Las funciones se declaran con el simbolo @
Es una manera super util de definir si una funcion debe ejecutarse o no:
Ejemplo:
    Si un servidor web debe ejecutar ciertas funciones solo para un usuario que se loguea.

LOS DECADORES NORMALMENTE SON HABITUALES ENTRE PYTHON Y SUS FRAMEWORKS.
"""

def decorador(func):
    def deco(param):
        pass
    return deco


@decorador
def funcion():
    pass



def proteger(func):
    # La encapsulamos dentro de proteger
    def envolver(password):
        if password == "ibecon":
            return func()
        else:
            print("Contraseña incorrecta")

    return envolver

# Estamos decorando la funcion proteger_login.
# se llama decorar
# implementando por detras
@proteger
def proteger_login():
    print("Tu contraseña es correcta")

# punto de incio
if __name__ == '__main__':
    password = str(input("Introduce tu contraseña: "))
    proteger_login(password)