# Linear Algebra Experiments

This project is a collection of numerical experiments in Linear Algebra using **Python**, **NumPy**, and **Matplotlib**.  
Each module reproduces a theoretical result or explores a fundamental numerical property of matrices.  
It is designed for **didactic purposes**, offering a **simple and introductory** approach to numerical linear algebra concepts in data science and their **basic** Python implementation.

## Project Structure

```
linear-algebra-experiments/
│
├── src/
│   ├── matrix_exponentials.py
│   ├── random_matrix_eigs.py
│   ├── molecular_inertia.py
│   ├── eigen_svd_perturbations.py
│   ├── svd_image_compression.py
│
├── data/
│   ├── dataset.xyz
│   └── demo_image.jpg
│
├── outputs/
├── main.py
└── README.md
```

Run all experiments via:
```bash
python main.py
```

Install dependencies:
```bash
pip install numpy matplotlib ase
```

---

## Modules Overview

### 1. `matrix_exponentials.py`
Computes and visualizes the **matrix exponential** \( e^{At} \) for a 2×2 real matrix.  
The implementation exploits diagonalization \( A = VDV^{-1} \) and Euler’s identity to show that:
\[
e^{At} = e^{-t} 
\begin{bmatrix}
\cos t & \sin t \\
-\sin t & \cos t
\end{bmatrix}.
\]
Plots show the real and imaginary parts of the matrix entries over time, highlighting the expected oscillatory decay.

---

### 2. `random_matrix_eigs.py`
Empirically verifies **Girko’s Circular Law**.  
For random matrices \( R_{n \times n} \) with Gaussian entries:
\[
\lambda_i(R) / \sqrt{n}
\]
tends to uniformly fill the unit disk in the complex plane as \( n \to \infty \).  
The script generates scatter plots of eigenvalue distributions for logarithmically spaced matrix sizes, confirming the law visually.

---

### 3. `molecular_inertia.py`
Computes the **moment of inertia tensor** for molecular structures read from a `.xyz` dataset (using [ASE — Atomic Simulation Environment](https://wiki.fysik.dtu.dk/ase/ase/io/io.html#ase.io.read)).  
Each molecule is classified by comparing its principal moments \( I_a \le I_b \le I_c \):

| Type | Condition |
|------|------------|
| Spherical | \( I_a \approx I_b \approx I_c \) |
| Prolate | \( I_a < I_b \approx I_c \) |
| Oblate | \( I_a \approx I_b < I_c \) |
| Asymmetric | \( I_a < I_b < I_c \) |

Returns and prints the count of molecules per category.

---

### 4. `eigen_svd_perturbations.py`
Analyzes the **stability of eigenvalues and singular values** under small perturbations.  
For
\[
A(\varepsilon) = 
\begin{bmatrix}
0 & 1 & 0 & 0 \\
0 & 0 & 2 & 0 \\
0 & 0 & 0 & 3 \\
\varepsilon & 0 & 0 & 0
\end{bmatrix},
\]
as \( \varepsilon \to 0 \), eigenvalues vary dramatically (spectral instability),  
while singular values remain stable — with three constants (1, 2, 3) and one that increases linearly with |ε|.  
Plots show both eigenvalue components and singular value evolution.

---

### 5. `svd_image_compression.py`
Demonstrates **image compression via Singular Value Decomposition (SVD)**.  
An image matrix \( P = USV^T \) is reconstructed using only the first *k* singular values:
\[
P_k = U_{:,1:k} \, \Sigma_{1:k,1:k} \, V_{1:k,:}^T.
\]
Smaller *k* gives stronger compression but lower quality.  
The script displays side-by-side reconstructions for increasing *k*, illustrating the trade-off between compression ratio and fidelity.

---

## Usage Examples

```python
from src import matrix_exponentials, svd_image_compression

# Compute e^{At} for a custom matrix
A = [[0, 1], [-2, -3]]
matrix_exponentials.run(A=A, t_max=10)

# Compress an image with SVD
svd_image_compression.run("data/demo_image.jpg", k_values=[5, 20, 50])
```

All plots and images are automatically saved in the `outputs/` directory.

---

**Author:** Giulia Montagnani  
