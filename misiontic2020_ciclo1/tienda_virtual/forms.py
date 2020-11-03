#archivo forms.py
from django.forms import Form, CharField, ChoiceField

class agregar_producto(Form):
    productos = ()
    cantidad = ((i, i) for i in range(16))

    producto = ChoiceField(label = "Producto", required=True, choices=productos)
    cantidad = ChoiceField(label = "Cantidad", required=True, choices=cantidad)

class pagar_carrito(Form):
    metodos = (('Tarjeta de Crédito', 'Tarjeta de Crédito'), ('Pago en Efectivo', 'Pago en Efectivo'), ('Tarjeta Débito', 'Tarjeta Débito'))

    metodo_pago = ChoiceField(label = "Método de Pago", required=True, choices=metodos)
    comprador = CharField(label = "Nombres", required=True)
    direccion = CharField(label = "Dirección de Envío", required=True)
    observaciones = CharField(label = "Observaciones", required=False)