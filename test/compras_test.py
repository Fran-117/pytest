
#Si el precio es mayor a 100 y se llevan mas de 10 unidades, se aplica un descuento del 10% al precio total.
#Si el precio es <= 100 y la cantidad es menor a 15 unidades no se aplica descuento.
from src.compras.compra import compra

producto = compra()
int = articulo_precio = 101
int = articulo_cantidad = 50



precio = producto.precio_unitario(articulo_precio)
def test_precio_unitario():
    assert precio == 101


cantidad = producto.cantidad(articulo_cantidad)
def test_cantidad():
    assert cantidad == 50

descuento = producto.decuento(articulo_cantidad, articulo_precio)
print("El descuento aplicado es de: ", descuento*100, "%")

def test_descuento():
    if articulo_cantidad >= 10 and articulo_precio > 100:
        assert descuento == 0.10

total = producto.total(articulo_cantidad, articulo_precio, descuento)
def test_total():
    assert total == (articulo_cantidad * articulo_precio) * (1 - descuento)

