import numpy as np
import matplotlib.pyplot as plt

def run(n_values=None, num_mats_n=100, bound=1.5):
    if n_values is None:
        n_values = np.logspace(np.log10(2), np.log10(200), 6, dtype=int)

    cmap = plt.cm.plasma
    fig, axes = plt.subplots(2, 3, figsize=(12,8))
    axes = axes.flatten()

    for idx, n in enumerate(n_values):
        eigs_all = []
        for _ in range(num_mats_n):
            R = np.random.randn(n, n)
            eigs = np.linalg.eigvals(R) / np.sqrt(n)
            eigs_all.append(eigs)
        eigs_all = np.concatenate(eigs_all)

        ax = axes[idx]
        color = cmap(idx / len(n_values))
        ax.scatter(eigs_all.real, eigs_all.imag, s=5, color=color, alpha=0.7)
        ax.set_xlim(-bound, bound)
        ax.set_ylim(-bound, bound)
        ax.set_title(f"n={n}")
        ax.grid(True, ls="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig("outputs/random_matrix_eigs.png", dpi=300)
    plt.close()
