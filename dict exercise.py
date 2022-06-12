peak = {
    "name": "Castle Peak",
    "height": 14264,
    "summit_log": [],
    "cell_reception": {
        "AT&T": "no reception",
        "T-Mobile": "poor"
    }
}

peak["range"] = "Elk Mountains"

peak["first_climbed"] = 1873

peak["height"] = 14265

peak["cell_reception"]["Verizon"] = "good"

peak["summit_log"].append("Daniil")

el = peak.pop("height")
peak["elevation"] = el

for value in peak.values():
    print(value)

for key, value in peak.items():
    print(f"{key} -> {value}")

peak.clear()

print(peak)