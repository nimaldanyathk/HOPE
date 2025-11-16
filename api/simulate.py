import numpy as np
from scipy.constants import hbar, m_e
import matplotlib.pyplot as plt
import io
import base64

def quantum_probability(n, x):
    L = 1e-9  # Box length (1 nm)
    psi = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
    return psi**2

def handler(request):
    # Read n from query like /api/simulate?n=2
    n = int(request.args.get("n", 1))

    x = np.linspace(0, 1e-9, 1000)
    prob = quantum_probability(n, x)

    # make plot → base64
    plt.figure(figsize=(6, 4))
    plt.plot(x * 1e9, prob, lw=2)
    plt.fill_between(x * 1e9, prob, alpha=0.5)
    plt.xlabel("Position (nm)")
    plt.ylabel("Probability Density")
    plt.title(f"Quantum Probability Density (n={n})")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    encoded = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return {
        "image": f"data:image/png;base64,{encoded}"
    }
