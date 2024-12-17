#use as python runner2xyz.py (path to runner file) (name of new xyz)
import numpy as np
import sys
import ase
from ase.units import Hartree, Bohr
args = sys.argv
def read_structure_n2p2(f_in, unit = 1):
#    line_begin = f_in.readline()
#     print(line_begin)
    #if file is finished
#     if not line_begin:
#         return none
    #line should start with begin
#     if line_begin.strip() != 'begin':
#         raise ValueError
    lattice = []
    positions = []
    forces = []
    energy = []
    atoms = []
    for line in f_in:
        #line = f_in.readline()
        items = line.split()
        if items[0] == "lattice":
            lattice.append([float(item)*Bohr for item in items[1:4]])
        elif items[0] == "atom":
            atoms.append(items[4])
            positions.append([float(item)*Bohr for item in items[1:4]])
            forces.append([float(item) * Hartree/Bohr for item in items[7:10]])
        elif items[0] == "charge":
            pass
        elif items[0] == "energy":
            energy.append(float(items[1])*Hartree)
        elif items[0] == "end":
            break
    positions = np.array(positions) * unit
    forces = np.array(forces)
    lattice = np.array(lattice) * unit
    atoms = np.array(atoms)
    return lattice, positions, forces, energy, atoms
def write_structure_xyz(f_out, lattice, positions, forces, energy, atoms):
    natoms = len(atoms)
    f_out.write(f'{natoms:d}\n')
    lattice_form = ['{0:15.6f}'.format(x) for x in lattice.flatten().tolist()]
    lattice_ase = ''.join(str(i) for i in lattice_form )
    f_out.write('Lattice="{0}" Properties=species:S:1:pos:R:3:force_ref:R:3 energy_ref={1:10.6f} config_type=NaCl pbc="T T T"\n'.format(lattice_ase,energy[0]))
    fmt_one = '{:30.12f}'
    fmt_prop = '{:6s} ' + 3*fmt_one + 3*fmt_one + '\n'
    for i, name in enumerate(atoms):
        f_out.write(fmt_prop.format(name, *positions[i], *forces[i]))
f_out = f'{str(args[2])}'
file_in = f'{str(args[1])}'
with open(file_in) as f:
    for line in f:
        if "begin" in line:
            lattice, positions, forces, energy, atoms = read_structure_n2p2(f)
            with open(f_out,'a') as fout:
                write_structure_xyz(fout, lattice, positions, forces, energy, atoms)
