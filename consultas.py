from simulador import generate
from statistics import mean
from gestorJson import gestorJSON

datos = generate()

puntarenas = [l for l in datos if l["Estacion"] == "Puntarenas" and l["Hora"] == 13]
temps = [l["Temperatura"] for l in puntarenas]


promedios = {
    hour: mean([l["Temperatura"] for l in datos if l["Estacion"] == "Puntarenas" and l["Hora"] == hour])
    for hour in range(24)
}

def promPerHour(est):
    return {
        hour: round(mean([l["Temperatura"] for l in datos if l["Estacion"] == est and l["Hora"] == hour]),1)
        for hour in range(24)
    }

def heatPerStation():
    return {
        e["NombreDestino"]: max(
            [l for l in datos if l["Estacion"] == e["NombreDestino"]],
            key=lambda l: l["Temperatura"]
        )
        for e in gestorJSON.dest
    }

def fluctuation(est, day):
    pressure = [l["Presion"] for l in datos if l["Estacion"] == est and l["Dia"] == day]
    return round(max(pressure) - min(pressure), 1)


def barometricFluctuation(dayStart):
    dias = gestorJSON.days[gestorJSON.days.index(dayStart):]
    return {
        e["NombreDestino"]: {dia: fluctuation(e["NombreDestino"], dia) for dia in dias}
        for e in gestorJSON.dest
    }


def heatAlert(temp_min=32, hum_min=80):
    criticas = list(filter(lambda l: l["Temperatura"] > temp_min and l["Humedad"] > hum_min, datos))

    por_estacion = {
        e["NombreDestino"]: [l for l in criticas if l["Estacion"] == e["NombreDestino"]]
        for e in gestorJSON.dest
    }

    return sorted(
        filter(lambda par: par[1], por_estacion.items()),
        key=lambda par: len(par[1]),
        reverse=True
    )

resultado = barometricFluctuation("Miércoles")
print("\n".join(
    f"{est}: " + ", ".join(f"{d} {v} hPa" for d, v in dias.items())
    for est, dias in resultado.items()
))