from flask import Flask, jsonify, render_template
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from scipy.constants import hbar, m_e

app = Flask(__name__)

# Function to calculate the probability density of a particle in a 1D box
def quantum_probability(n, x):
    L = 1e-9  # Box length (1 nm)
    psi = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)  # Wavefunction
    return psi**2  # Probability density (ψ²)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate/<int:n>')
def simulate(n):
    x = np.linspace(0, 1e-9, 1000)  # Define space range
    probability_density = quantum_probability(n, x)  # Compute ψ²
    
    # Create a base64-encoded plot
    plt.figure(figsize=(6, 4))
    plt.plot(x * 1e9, probability_density, color='blue', lw=2)
    plt.fill_between(x * 1e9, probability_density, color='cyan', alpha=0.5)
    plt.xlabel('Position (nm)')
    plt.ylabel('Probability Density')
    plt.title(f'Quantum Probability Density (n={n})')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    encoded = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return jsonify({"image": f"data:image/png;base64,{encoded}"})

if __name__ == '__main__':
    app.run(debug=True)