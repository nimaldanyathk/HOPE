import numpy as np
import json
from scipy.special import hermite
from math import factorial, pi, sqrt

def quantum_wavefunction(n, x):
    norm = 1 / np.sqrt(2**n * factorial(n) * np.sqrt(pi))
    hermite_poly = hermite(n)(x)
    return norm * hermite_poly * np.exp(-x**2 / 2)

def handler(request):
    try:
        # Fix query parameter reading
        n = int(request.query_params.get("n", 0))

        x = np.linspace(-4, 4, 200)
        y = quantum_wavefunction(n, x)

        # Fix JSON response (stringify body)
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "x": x.tolist(),
                "y": y.tolist()
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
