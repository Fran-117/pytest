class calculadora:
    def sum(result, a, b):
        result = a + b
        return result
    
    def res(result, a, b):
        result = a - b
        return result

    def mul(result, a, b):
        result = a * b
        return result
    
    def div(result, a, b):
        if b != 0:
            result = a / b
            return result
        else:
            return "No válido porque es cero"

