class compra :
    def precio_unitario(precio,articulo_precio):
        precio = articulo_precio 
        return precio


    def cantidad(cantidad,articulo_cantidad):
        cantidad = articulo_cantidad
        return cantidad
    

    def decuento(descuento,articulo_cantidad, articulo_precio):
        if articulo_cantidad >= 10 and articulo_precio > 100:
            descuento = 0.10
            return descuento
        else: 
            descuento = 0
            return descuento

    def total(total, articulo_cantidad, articulo_precio, descuento):
        total = (articulo_cantidad * articulo_precio) * ((1-descuento))
        return total
    