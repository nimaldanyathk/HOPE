import numpy as np
from scipy.special import hermite
from math import factorial, pi, sqrt

def quantum_wavefunction(n, x):
    norm = 1 / sqrt(2**n * factorial(n) * sqrt(pi))
    hermite_poly = hermite(n)(x)
    return norm * hermite_poly * np.exp(-x**2 / 2)

def handler(request):
    n = int(request.query.get("n", 0))

    x = np.linspace(-4, 4, 200)
    y = quantum_wavefunction(n, x)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": {
            "x": x.tolist(),
            "y": y.tolist()
        }
    }