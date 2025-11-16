import numpy as np
import json
from scipy.special import hermite
from math import factorial, pi, sqrt

def quantum_wavefunction(n, x):
    norm = 1 / np.sqrt(2**n * factorial(n) * np.sqrt(pi))
    Hn = hermite(n)(x)
    return norm * Hn * np.exp(-x**2 / 2)

def handler(request):
    try:
        # Correct reading of query param
        n = int(request.query_params.get("n", 0))
    except Exception as e:
        n = 0

    x = np.linspace(-4, 4, 200)
    y = quantum_wavefunction(n, x)

    # Stringify the body
    body = {
        "x": x.tolist(),
        "y": y.tolist()
    }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }
