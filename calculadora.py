class calculadora:
    def sum(result, a, b):
        result.value = a + b
    
    def res(result, a, b):
        result.value = a - b

    def mul(result, a, b):
        result.value = a * b
    
    def div(result, a, b):
        if b != 0:
            result.value = a / b
        else:
            result.value = "No válido porque es cero"

