import random
from gestorJson import gestorJSON


def read(est, day, hour):
	temp = round(random.uniform(24, 25), 1)
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
		for est in gestorJSON.dest
		for day in gestorJSON.days
		for hour in range(0, 24)

	]

datos = generate()
l = datos[0]
print(f"{l['Estacion']} | {l['Dia']} | {l['Hora']}:00 | {l['Temperatura']} °C | {l['Humedad']} % | {l['Presion']} hPa")