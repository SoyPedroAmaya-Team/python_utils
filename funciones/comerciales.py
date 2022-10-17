
# * -> descripcion: A partir de un precio normal y un porcentaje expresado en un numero real, devuelve el precio con descuento
# ! -> esta version no cuenta con validaciones aun
# ? -> ¿Para que existimos?
def precio_descuento(precio_normal, descuento):
# @ -> precio_normal: precio normal que el cliente paga
# @ -> descuento: descuento ofrecido por el proveedor
# todo -> Hacer la validacion de que el porcentaje de descuento no puede exceder a 100.00
# todo -> Hacer la validacion de que no puede recibir argumentos que no sean numeros reales
    return (precio_normal * (100-descuento))/100

def roi(costo, ingreso):
    return (ingreso - costo)/ costo

## aqui llamamos a la funcion
print('El precio con descuento es: ' + str(precio_descuento(100.00,100)))
print('El roi es:' + str(roi(20.00,100.00)))
