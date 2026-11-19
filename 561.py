import sys

to_meters = {
    "mile": 1609,
    "yard": 0.9144,
    "foot": 30.48 * 0.01,
    "inch": 2.54 * 0.01,
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
}

for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    parts = line.split()
    number = float(parts[0])
    unit_from = parts[1]
    unit_to = parts[3]

    meters = number * to_meters[unit_from]
    result = meters / to_meters[unit_to]
    print(f"{result:.2e}")