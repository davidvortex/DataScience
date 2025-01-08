nombre = "Juan"
fehca = "27/novi/20224"
saludos = "Buenos dias"
CambioDolar = 1380

bienvenida = nombre +" "+saludos+" "+fehca+". Welcome user"
print(bienvenida)

EurosRecibir = CambioDolar * 0.88
print(EurosRecibir)

billetes100 = EurosRecibir // 100
billetes50 = (EurosRecibir - (billetes100 * 100)) // 50
billetes20 = (EurosRecibir - (billetes50 * 50)) // 20
monedas10 = (EurosRecibir - (billetes20 * 20))// 10
monedas5 = (EurosRecibir - (monedas10 * 10)) // 5
monedas2 = (EurosRecibir - (monedas5 * 5)) // 2
monedas1 = EurosRecibir % 1

print(bienvenida)
print("Cantidades de dolares a cambiar:")
print(CambioDolar)
print("Euros que va a recibir:")
print(EurosRecibir)
print("Recibir el dinero de la siguiente manera")
print("billetes de 100:")
print(billetes100)
print("billetes de 50:")
print(billetes50)
print("billetes de 20:")
print(billetes20)
print("monedas de  10:")
print(monedas10)
print("monedas de 5:")
print(monedas5)
print("monedas de 2:")
print(monedas2)
print("monedas de 1:")
print(monedas1)

