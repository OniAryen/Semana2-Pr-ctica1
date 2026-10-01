Weather Stations

A Python program that simulates one week of weather data for 10 stations
along the Pacific coast of Puntarenas, Costa Rica. It was made for the
ITI-321 Programación II course.

## What it does

The program creates fake readings of temperature, humidity and pressure
for every station, day and hour (10 stations x 7 days x 24 hours = 1680
readings). Then you pick a station and it shows:

1. The expected temperature for each hour of the day.
2. The hottest day and hour of the week.
3. The pressure change (fluctuation) for each day.
4. Heat alerts: readings above 32 °C with more than 80 % humidity.

## Files

| File | Purpose |
|---|---|
| `gestorJson.py` | The list of stations and the days of the week |
| `simulador.py` | Makes the fake readings |
| `consultas.py` | The four queries on the data |
| `main.py` | The console menu |

## How to run

You need Python 3. No extra libraries are needed.

```
python main.py
```

Type the number of a station and press Enter. Choose "Salir" to exit.

## Rules of the assignment

- Data is stored only in lists and dictionaries.
- No manual counters and no nested loops to process the data.
- Queries use list and dict comprehensions, `filter`, `max`, `sorted` and `lambda`.

## Notes

- The temperature changes with the time of day. Humidity and pressure are random.
- Temperature ranges were chosen using IMN forecasts for Puntarenas as a guide.