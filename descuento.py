def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Primer ejemplo: solo el monto total
monto_total_1 = 1000  # Monto de la compra
descuento_1 = calcular_descuento(monto_total_1)  # Se usa el descuento por defecto (10%)
monto_final_1 = monto_total_1 - descuento_1

# Segundo ejemplo: monto total y porcentaje de descuento
monto_total_2 = 500
porcentaje_descuento_2 = 20  # Descuento del 20%
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2

# Mostrar los resultados
print(f"Monto de la compra: ${monto_total_1}")
print(f"Descuento (10%): ${descuento_1}")
print(f"Monto final a pagar: ${monto_final_1}\n")

print(f"Monto de la compra: ${monto_total_2}")
print(f"Descuento (20%): ${descuento_2}")
print(f"Monto final a pagar: ${monto_final_2}")


