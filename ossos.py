ossos = {
    "Grizzly": "enfadado",
    "Pardo":"amistoso", 
    "polar":"amistoso"
    }

print(ossos)

for oso in ossos.keys():
    if oso == "amistoso":
        print("Hola, "+oso + "!")
    else:
        print("corre, corre, corre es un %s!"%(oso))

