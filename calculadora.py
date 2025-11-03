from metodo import calculadora

igual = calculadora()

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

suma = igual.sum(a,b)
resta = igual.res(a,b)
print("La suma de sus numeros es: ", suma)
