import numpy as np
from ase.io import read

def calc_I(rel_positions, masses):
    I = np.zeros((3, 3))
    for j in range(3):
        for k in range(3):
            if j == k:
                I[j][j] = np.sum(masses * (np.sum(rel_positions**2, axis=1) - rel_positions[:, j]**2))
            else:
                I[j][k] = -np.sum(masses * rel_positions[:, j] * rel_positions[:, k])
    return I

def run(path="data/demo_dataset.xyz"):
    DataSet = read(path, index=":")
    sfer, prol, obl, asymm = [[] for _ in range(4)]

    for molecule in DataSet:
        mol_positions = molecule.get_positions()
        mol_masses = molecule.get_masses()
        cm = np.sum(mol_positions * mol_masses[:, np.newaxis], axis=0) / np.sum(mol_masses)
        I = calc_I(mol_positions - cm, mol_masses)
        a, b, c = np.sort(np.linalg.eigvals(I))

        if np.isclose(a, b, rtol=1e-3) and np.isclose(b, c, rtol=1e-3):
            sfer.append(molecule)
        elif np.isclose(b, c, rtol=1e-3):
            prol.append(molecule)
        elif np.isclose(a, b, rtol=1e-3):
            obl.append(molecule)
        else:
            asymm.append(molecule)

    result = {"sferiche": len(sfer), "prolate": len(prol), "oblate": len(obl), "asimmetriche": len(asymm)}
    print("Classificazione molecolare:", result)
    return result
