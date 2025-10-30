import numpy as np
import matplotlib.pyplot as plt

def run(A=None, t_max=5):
    if A is None:
        A = np.array([[-1, 1], [-1, -1]])
    else:
        A = np.array(A)

    eigvals, eigvecs = np.linalg.eig(A)
    V, V_inv = eigvecs, np.linalg.inv(eigvecs)
    t_vals = np.linspace(0, t_max, 200)

    entries_real = [[] for _ in range(4)]
    entries_imag = [[] for _ in range(4)]

    for t in t_vals:
        eDt = np.diag(np.exp(eigvals*t))
        eAt = V @ eDt @ V_inv
        entries = [eAt[0,0], eAt[0,1], eAt[1,0], eAt[1,1]]
        for i, val in enumerate(entries):
            entries_real[i].append(val.real)
            entries_imag[i].append(val.imag)

    colors = ["red", "orange", "green", "blue"]
    labels = [r"$(e^{At})_{11}$", r"$(e^{At})_{12}$", r"$(e^{At})_{21}$", r"$(e^{At})_{22}$"]

    for title, data, part in [("Real part", entries_real, "Real"), ("Imaginary part", entries_imag, "Imaginary")]:
        plt.figure(figsize=(8,6))
        for i in range(4):
            plt.plot(t_vals, data[i], color=colors[i], label=labels[i])
        plt.xlabel("t")
        plt.ylabel(part)
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"outputs/matrix_exp_{part}.png", dpi=300)
        plt.close()
