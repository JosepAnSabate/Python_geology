
a = [1,3,5,7,8,"b",10,20]

for i in a:
    try:
        divisio= i/2
        print(divisio)
    except Exception as e:
        print("Error en %s"%i)
        print(e) #el tipusderrorsemmagatzema en excepcio com a e
        