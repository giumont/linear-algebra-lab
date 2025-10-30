import numpy as np
import matplotlib.pyplot as plt

def run(eps_max=1e-5, num_points=200):
    eps_vals = np.linspace(0, eps_max, num_points)
    eigs_real, eigs_imag, val_princ = [], [], []

    for eps in eps_vals:
        A = np.array([[0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3], [eps, 0, 0, 0]])
        eigs = np.linalg.eigvals(A)
        eigs_real.append(eigs.real)
        eigs_imag.append(eigs.imag)
        _, S, _ = np.linalg.svd(A)
        val_princ.append(S)

    eigs_real, eigs_imag, val_princ = map(np.array, [eigs_real, eigs_imag, val_princ])

    plt.figure(figsize=(10,8))
    for i in range(4):
        plt.plot(eps_vals, eigs_real[:,i], label=f"Re(lambda{i+1})")
    plt.xlabel("epsilon"); plt.ylabel("Re(lambda)")
    plt.title("Eigenvalues - Real part")
    plt.grid(True); plt.legend()
    plt.savefig("outputs/perturb_eigs_real.png", dpi=300); plt.close()

    plt.figure(figsize=(10,8))
    for i in range(4):
        plt.plot(eps_vals, eigs_imag[:,i], label=f"Im(lambda{i+1})")
    plt.xlabel("epsilon"); plt.ylabel("Im(lambda)")
    plt.title("Eigenvalues - Imaginary part")
    plt.grid(True); plt.legend()
    plt.savefig("outputs/perturb_eigs_imag.png", dpi=300); plt.close()
