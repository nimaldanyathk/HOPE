import numpy as np
import json

# Constants
k = 10  # Spring constant (N/m)
m = 1   # Mass (kg)
A = 2   # Amplitude (m)

# Displacement range (-A to A)
x_values = np.linspace(-A, A, 100)

# Compute Energy Values
pe_values = 0.5 * k * x_values**2  # Parabolic PE curve
ke_values = 0.5 * k * A**2 - pe_values  # KE is complementary
tme_values = 0.5 * k * A**2  # Constant total mechanical energy

# Save to JSON
data = {
    "x": x_values.tolist(),
    "PE": pe_values.tolist(),
    "KE": ke_values.tolist(),
    "TME": [tme_values] * len(x_values)
}

with open("data.json", "w") as f:
    json.dump(data, f)

print("Data saved to data.json")