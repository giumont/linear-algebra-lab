import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def reconstruct(U, S, Vt, k):
    return (U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :])

def run(image_path="data/demo_image.jpg", k_values=None):
    if k_values is None:
        k_values = [1, 5, 10, 20, 50, 100]
    img = mpimg.imread(image_path)
    if img.ndim == 3:
        img_gray = img.mean(axis=2)
    else:
        img_gray = img

    U, S, Vt = np.linalg.svd(img_gray)
    plt.figure(figsize=(8,6))
    plt.plot(S); plt.yscale("log"); plt.grid(True)
    plt.title("Singular values (log scale))")
    plt.savefig("outputs/singular_values.png", dpi=300); plt.close()

    fig, axes = plt.subplots(2, 3, figsize=(12,8))
    axes = axes.flatten()
    for idx, k in enumerate(k_values[:6]):
        approx = reconstruct(U, S, Vt, k)
        axes[idx].imshow(approx, cmap="gray")
        axes[idx].set_title(f"k={k}")
        axes[idx].axis("off")
    plt.tight_layout()
    plt.savefig("outputs/image_reconstructions.png", dpi=300)
    plt.close()
