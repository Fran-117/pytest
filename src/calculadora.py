from metodo_test import calculadora

igual = calculadora()

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

suma = igual.sum(a,b)
resta = igual.res(a,b)
multiplicacion = igual.mul(a,b)
division = igual.div(a,b)


print("La suma de sus numeros es: ", suma)
print("La resta de sus numeros es: ", resta)
print("La multiplicacion de sus numeros es: ", multiplicacion) 
print("La division de sus numeros es: ", division)
