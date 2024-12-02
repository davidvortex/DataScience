usuario = "admin"
contraseña = "abc123"

usu = input("ingresa usuario: ")
con = input("ingresa contraseña: ")

if usu == usuario and con == contraseña:
    print("Acceso concedido")
else:
    print("no tiene acceso")