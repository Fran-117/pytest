from src.calculadora import calculadora

igual = calculadora()

a = 5
b = 5

suma = igual.sum(a,b)
def test_suma():
    assert suma == 10

resta = igual.res(a,b)
def test_resta():
    assert resta == 0

multiplicacion = igual.mul(a,b)
def test_mul():
    assert multiplicacion == 25

division = igual.div(a,b)
def test_div():
    assert division == 1.0


print("La suma de sus numeros es: ", suma)
print("La resta de sus numeros es: ", resta)
print("La multiplicacion de sus numeros es: ", multiplicacion) 
print("La division de sus numeros es: ", division)
