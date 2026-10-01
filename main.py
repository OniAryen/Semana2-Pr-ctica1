from gestorJson import gestorJSON
from consultas import (
    promPerHour,
    heatPerStation,
    barometricFluctuation,
    heatAlert,
)


def elegir(opciones, titulo):
    print(titulo)
    print("\n".join(f"  {i}. {o}" for i, o in enumerate(opciones, 1)))
    while True:
        r = input("Número: ").strip()
        if r.isdigit() and 1 <= int(r) <= len(opciones):
            return opciones[int(r) - 1]
        print("Opción no válida, intenta de nuevo.")


def mostrar_estacion(est):
    print(f"\n===== {est} =====")

    print("\nTemperaturas esperadas por hora:")
    print("\n".join(
        f"  {h:02d}:00 -> {round(t, 1)} °C"
        for h, t in promPerHour(est).items()
    ))

    l = heatPerStation()[est]
    print(f"\nMomento más caluroso: {l['Dia']} a las {l['Hora']}:00 con {l['Temperatura']} °C")

    print("\nFluctuación barométrica por día:")
    print("\n".join(
        f"  {d}: {v} hPa"
        for d, v in barometricFluctuation(gestorJSON.days[0])[est].items()
    ))

    lecs = dict(heatAlert()).get(est)
    print("\nAlerta de bochorno (más de 32 °C y más de 80 % de humedad):")
    print(
        f"  {len(lecs)} lecturas críticas, "
        f"entre las {min(l['Hora'] for l in lecs)}:00 y las {max(l['Hora'] for l in lecs)}:00"
        if lecs else "  Sin alertas esta semana."
    )


def main():
    estaciones = [e["NombreDestino"] for e in gestorJSON.dest]
    while True:
        est = elegir(estaciones + ["Salir"], "\n=== Elige tu zona ===")
        if est == "Salir":
            print("Hasta luego.")
            break
        mostrar_estacion(est)


if __name__ == "__main__":
    main()