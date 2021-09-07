import gym_multilayerthinfilm as mltf
import numpy as np

pathInGaAlP = 'materials\\nInGaAlP.txt'
pathGaP600 = 'materials\\nGaP600.txt'
pathGaP560 = 'materials\\nGaP560.txt'
pathITOcontact = 'materials\\nITOcontact.txt'
pathITOadhesion = 'materials\\nITOadhesion.txt'
pathSiO2 = 'materials\\nSiO2.txt'
pathNb2O5 = 'materials\\nNb2O5.txt'
#pathAu = 'materials\\nAu.txt'
pathAu = 'materials\\Au.txt'
pathNew = 'materials\\n_Al15GaAs_Te.txt'

material_path_list = [pathSiO2, pathAu, pathNew]
mode = 'reflectivity'  # 'transmittivity' or 'reflectivity'
maximum_number_of_layers = 10
ticks_angle = 90
angle_min = 0
angle_max = 90
spectra = np.linspace(400, 1000, 601).reshape(1, -1)
# np.vstack((np.linspace(830, 870, 40), np.linspace(920, 960, 40)))
# np.array([550]).reshape(1, 1)
angle = np.linspace(angle_min, angle_max, ticks_angle)


lambda_min = np.min(spectra)
lambda_max = np.max(spectra)
ticks_spectrum = max(int(lambda_max - lambda_min), 1)
lam_vac = np.linspace(lambda_min, lambda_max, ticks_spectrum) * (10 ** (-9))

target_array = np.ones((ticks_angle, ticks_spectrum))

wl = np.linspace(lambda_min, lambda_max, ticks_spectrum) * 1e-9
target = {'direction': angle, 'spectrum': wl, 'target': target_array, 'mode': mode}

N = mltf.get_N(material_path_list, lambda_min, lambda_max, points=ticks_spectrum, complex_n=True)
N = np.vstack((N, np.ones((1, N.shape[1]))))
env = mltf.MultiLayerThinFilm(N, maximum_number_of_layers, target)

env.reset()
layer_material_list = [1, 2]
tuple_list = []
for layer in layer_material_list:
    env.step(env.create_action(layer, thickness=10e-9))

# substrate:
substrate_material_list = [3]
substrate_thickness_list = [np.inf]
_, _, substrate_dict = env.create_stack(substrate_material_list, substrate_thickness_list)
#ambient:
ambient_material_list = [2]
ambient_thickness_list = [np.inf]
_, _, ambient_dict = env.create_stack(ambient_material_list, ambient_thickness_list)
env.set_cladding(substrate_dict, ambient_dict)

d = np.array([530e-9, 300e-9])
fom = env.rcerror(d)
_ = env.render()

print(':)')
