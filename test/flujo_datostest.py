#AGREGAR EL " _ " AL NOMBRE PARA QUE HAGA EL TEST

from src.flujo_datos import flujo
igual = flujo()

manzana = 8
pera = 6
piña = 2

resultado = igual.datos( manzana, pera, piña)
def test_datos():
    assert resultado == 20
