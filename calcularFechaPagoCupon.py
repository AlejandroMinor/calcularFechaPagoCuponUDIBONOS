from datetime import datetime, timedelta

def calcular_fechas_pago_cupon(fecha_vencimiento):
    # Convertir la fecha de vencimiento en un objeto datetime
    fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%d/%m/%Y")
    
    # Definir la fecha de inicio hace 5 años
    fecha_inicio = fecha_vencimiento - timedelta(days=365*5)
    
    # Calcular las fechas de pago de cupón
    fechas_pago = []
    fecha_actual = fecha_vencimiento
    while fecha_actual >= fecha_inicio:
        fecha_pago = fecha_actual - timedelta(days=182)
        fechas_pago.append(fecha_pago)
        fecha_actual = fecha_pago
    
    return fechas_pago

# Ejemplo de uso:
fecha_vencimiento = input("Ingrese la fecha de vencimiento (dd/mm/yyyy): ")
fechas_pago = calcular_fechas_pago_cupon(fecha_vencimiento)

print("Fechas de pago de cupón:")
for fecha_pago in fechas_pago:
    print(fecha_pago.strftime("%d/%m/%Y"))

fecha_referencia = datetime(2023, 1, 1)  # Fecha de referencia: 1 de enero de 2023
ultimo_pago_cercano = max(fecha for fecha in fechas_pago if fecha <= fecha_referencia)
dias_transcurridos = (fecha_referencia - ultimo_pago_cercano).days

print("Días transcurridos desde el último pago de cupón hasta el 1 de enero de 2023:", dias_transcurridos)
