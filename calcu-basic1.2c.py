while True:
    print ("\033[;33m"+"       CALCULADORA BASICA 1.2c") 
    print (".........................................................")
    print (" Tips: Para sacar EL porcentaje de un numero") 
    print (" hay que multiplicar por cero coma -numero de porcentaje-.")
    print (" Por ejemplo sacar el %25: Un NUMERO por 0.25")
    print (".........................................................")
    
    comando = input (" -Presionar ENTER para empezar o tipear -salir- para finalizar: ")
    if comando == "salir" or comando == "Salir" or comando == "SALIR":
        break
    Resultado = float(input("-introducir un NUMERO y presionar ENTER-: "))
    
    Operacion= "esperando a que variable operacion sea igual"
    while Operacion != "=":
        Operacion = input(" Introducir operacion +, -, *(multi), /(div), = : ")
        if Operacion == "+":
             Suma_numero = float(input(" Introducir Numero: "))
             Resultado += Suma_numero
        if Operacion == "-":
              Resta_numero= float(input (" Introducir numero: "))
              Resultado -= Resta_numero
        if Operacion == "*":
                Multi_numero= float(input (" Introducir numero: "))
                Resultado *= Multi_numero
        if Operacion == "/":
                  Divi_numero= float(input (" Introducir numero: "))
                  Resultado /= Divi_numero

    print (("\033[;36m"+"Resultado= "), Resultado)
