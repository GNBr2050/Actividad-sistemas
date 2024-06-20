CO=input("¡Bienvendio a las tiendas GN! La mejor experiencia y precios de la ciudad. Por favor seleccione el tipo de producto que desee adquirir: Camisas o Polos ")
DE=input("Introduce su clave de descuento: ")

#Definimos los precios
P20201=(200)
P20202=(220)
P20203=(180)
P20211=(120)
P20212=(140)
P20213=(100)

#Creamos las variables if para Camisas y polos con los dos codigos de descuento y agregamos else en caso de introducir un valor no válido
if CO=="Camisas" and DE=="UCSS1":
    print("Artículo camisa: Vintage 201 amarillo","Clave: 20201","Precio original:",P20201,"Precio de descuento:",(P20201*(0.9)))
    print("Artículo Camisa: Camila Yerna 102 blanco","Clave: 20202","Precio original:",P20202,"Precio de descuento:",(P20202*(0.9)))
    print("Artículo Camisa: Black Morde 302 gris","Calve: 20203","Precio original:",P20203,"Precio de descuento:",(P20202*(0.9)))
elif CO=="Camisas" and DE=="UCSS2":
    print("Artículo camisa: Vintage 201 amarillo","Clave: 20201","Precio original:",P20201,"Precio de descuento:",(P20201*(0.8)))
    print("Artículo Camisa: Camila Yerna 102 blanco","Clave: 20202","Precio original:",P20202,"Precio de descuento:",(P20202*(0.8)))
    print("Artículo Camisa: Black Morde 302 gris","Calve: 20203","Precio original:",P20203,"Precio de descuento:",(P20202*(0.8)))
elif CO=="Polos" and DE=="UCSS1":
    print("Atículo polo: Armando 301 rojo","Codigo: 20211","Precio original:",P20211,"Precio de descuento:",(P20211*(0.9)))
    print("Atículo polo: Yermo Capital 150 azul y amarillo","Codigo: 20212","Precio original:",P20211,"Precio de descuento:",(P20211*(0.9)))
    print("Atículo polo: Guillermo Verna 22 celeste","Codigo: 20213","Precio original:",P20211,"Precio de descuento:",(P20211*(0.9)))
elif CO=="Polos" and DE=="UCSS2":
    print("Atículo polo: Armando 301 rojo","Codigo: 20211","Precio original:",P20211,"Precio de descuento",(P20211*(0.8)))
    print("Atículo polo: Yermo Capital 150 azul y amarillo","Codigo: 20212","Precio original:",P20212,"Precio de descuento",(P20211*(0.8)))
    print("Atículo polo: Guillermo Verna 22 celeste","Codigo: 20213","Precio original:",P20213,"Precio de descuento",(P20211*(0.8)))
else:
    print("Usted introdujo un nombre o código incorrecto, vuelva a intentarlo")