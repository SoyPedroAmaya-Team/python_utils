def precio_descuento():
    print('estamos en la funcion precio_descuento')

def roi(costo, ingreso):
    return (ingreso - costo)/ costo

## aqui llamamos a la funcion
precio_descuento()
print('El roi es:' + str(roi(20.00,100.00)))



