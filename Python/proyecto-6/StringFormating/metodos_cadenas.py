cadena1 = "000Esto0es0una0cadena0alfa0numerica000"
cadena2 = "Esto no es una cadena alfa numerica"

print(cadena1.isalnum())
print(cadena2.isalnum())

cadena4 = cadena1.strip("0")

spliteo_de_cadena4 = cadena4.split("0")

cadena_final = ""

for palabra in spliteo_de_cadena4:
    cadena_final += palabra 

print(cadena_final)

