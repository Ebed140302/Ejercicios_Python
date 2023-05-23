print ('Bienvenido al sistema, tienes 3 intentos para ingresar al sistema')
contrasena = 1
while contrasena <= 3:
    intento = input('Introduce la contrasena: ')
    if intento == '3223' :
        print ('Haz ingresado correctamente al sistema')
        contrasena = 4
    else:
        print('La contraseña es incorrecta')
        if contrasena == 3:
            print('Agotaste tus intentos, comunicate con el admin')
        contrasena = contrasena + 1