import sys
from src import (
    matrix_exponentials,
    random_matrix_eigs,
    molecular_inertia,
    eigen_svd_perturbations,
    svd_image_compression
)

def main():
    print("=== Linear Algebra Experiments ===")
    print("1. Exponential of a 2x2 matrix (e^{At})")
    print("2. Eigenvalues of random matrices")
    print("3. Molecular moment of inertia (.xyz)")
    print("4. Eigenvalue and SVD perturbation analysis")
    print("5. Image compression using SVD")
    print("0. Exit")

    choice = input("Select an experiment: ").strip()
    print()

    if choice == "1":
        matrix_exponentials.run()
    elif choice == "2":
        random_matrix_eigs.run()
    elif choice == "3":
        molecular_inertia.run('data/demo_dataset.xyz')
    elif choice == "4":
        eigen_svd_perturbations.run()
    elif choice == "5":
        svd_image_compression.run('data/demo_image.jpg')
    elif choice == "0":
        sys.exit("Exiting program.")
    else:
        sys.exit("Invalid selection. Program terminated.")

    print("\nExperiment completed successfully!")
    print("All generated plots and results are saved in the 'outputs/' directory.")

if __name__ == "__main__":
    main()
