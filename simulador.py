import random
from gestorJson import gestorJSON


def read(est, day, hour):
    if hour < 6:
        base = 24
    elif hour < 10:
        base = 28
    elif hour < 16:
        base = 34
    elif hour < 20:
        base = 30
    else:
        base = 26

    temp = round(base + random.uniform(-1, 1), 1)
    hum = round(random.uniform(60, 95), 1)
    pres = round(random.uniform(1008, 1013), 1)

    return {
        'Estacion': est,
        'Dia': day,
        'Hora': hour,
        'Temperatura': temp,
        'Humedad': hum,
        'Presion': pres
    }

def generate():
	return [
		read(est["NombreDestino"],day, hour)
		for est in gestorJSON.dest #10 Stations
		for day in gestorJSON.days #7 Days
		for hour in range(0, 24) #24 hours

	]
