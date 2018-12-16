
operacion = input("¿Qué operación quieres realizar? (Multiplicar/Dividir/Sumar/Restar): ").upper()

primer_numero = int(input("Ecribe aquí el primer número: "))

segundo_numero=int(input("Ecribe aquí el segundo número: "))

if operacion== "MULTIPLICAR":
    resultado=primer_numero*segundo_numero

elif operacion=="DIVIDIR":
    resultado=primer_numero / segundo_numero

elif operacion=="SUMAR":
    resultado=primer_numero+segundo_numero

elif operacion=="RESTAR":
    resultado=primer_numero-segundo_numero

else:
    print("No me has dicho la operación que quieres que haga, vuelve a empezar")

if operacion=="MULTIPLICAR" or operacion=="DIVIDIR" or operacion=="SUMAR" or operacion=="RESTAR":
    print("El resultado de la operacióm es {}".format(resultado))
