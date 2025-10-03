print('Hola Mundo esto es una prueba para github')
for a in range(10):
    print(a)
print('Fin del programa')
print('Otra linea de codigo')
print('hola')
print('lol')
print('lol')
print("hola")

print("mundo")

for i in range (8):
    print(i)

a=2
b=3
c=5

def suma():
    print("suma", a+b+c)
suma()

# --- IGNORE ---
def generar_datos_ventas ():
    dias= ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    ventas= [150, 200, 250, 300, 350, 400, 450]
    return dias, ventas
    return datos_ventas
def resumen_analitica():
    dias, ventas= generar_datos_ventas()
    total= sum(ventas)
    promedio= total/ len(ventas)
    return{
        "dias": dias,
        "ventas": ventas,
        "total": total,
        "promedio": promedio
    }
datos=resumen_analitica()
print(datos["total"])
print(datos["promedio"])