#Definimos las preguntas y respuestas correctas mediante un rango
PR=["¿Cristobal Colon descubrió América?","¿La independencia del Perú fue en el año 1821?","¿Perú se encuentra ubicado en América del Sur?"]
RE=["Si","Si","Si"]

#Realizamos un bicle para las preguntas con for y variantes if
for preguntas in range(len(PR)):
    respuesta = input(PR[preguntas]+"  (Responde con 'Si' o 'No'):")
    
    if respuesta != RE[preguntas]:
        print("Respuesta incorrecta. Vuelve a intentarlo.")
        break
else:
    print("¡Felicitaciones! Respondiste todas las preguntas correctamente.")