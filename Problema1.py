#Juan Clavijo - 202225709
#Problema 1

a=0
while a==0:
    cantidad=int(input("Digite la cantidad de personas a encuestar:"))
    if cantidad>0:
        a+=1
    else:
        print("Ese número no es válido")
        print("")

mujeresMIO=0
hombresB=0
b=0
while a==1:
    print("")
    sexo=int(input("Digite el sexo (1-Masculino,2-Femenino):"))
    mdt=int(input("¿Qué medio de transporte prefiere? (1-MIO,2-Vehículo,3-Bicicleta):"))
    if (sexo==1 or sexo==2)and(mdt==1 or mdt==2 or mdt==3):
        b+=1
    else:
        print("Esos válores no son válidos")
    if b==cantidad:
        a+=1
    if sexo==2 and mdt==1:
        mujeresMIO+=1
    if sexo==1 and mdt==3:
        hombresB+=1

porcentajeHB=(hombresB/cantidad)*100
print("")
print("A partir de la encuesta, podemos sacar los siguientes datos:")
print("La cantidad de mujeres que se transportan en MIO es:",mujeresMIO)
print("El porcentaje de hombres que se transportan en bicicleta es del",porcentajeHB,"%")
