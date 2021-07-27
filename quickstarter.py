import gym_multilayerthinfilm as gym_mltf
import numpy as np

pathAu = 'default_materials\\Au.txt'
pathNb2O5 = 'default_materials\\Nb2O5.txt'
pathSiO2 = 'default_materials\\SiO2.txt'
material_path_list = [pathAu, pathNb2O5, pathSiO2]
maximum_number_of_layers = 12
ticks_angle = 180
angle_min = 0
angle_max = 90
ticks_spectrum = 900
wl_min = 300 * (10**(-9))
wl_max = 1200 * (10**(-9))

N = gym_mltf.get_N(material_path_list, wl_min * 10**9, wl_max * 10**9, points=ticks_spectrum, complex_n=True)

target_array = np.ones((ticks_angle, ticks_spectrum))
angle = np.linspace(angle_min, angle_max, ticks_angle)
wl = np.linspace(wl_min, wl_max, ticks_spectrum)
target = {'direction': angle, 'spectrum': wl, 'target': target_array}

env = gym_mltf.MultiLayerThinFilm(N, maximum_number_of_layers, target)
print('This is an action:')
print(env.action_space.sample())

env.reset()
env.step(env.action_space.sample())
env.step(env.action_space.sample())
env.step(env.action_space.sample())
env.step(env.action_space.sample())
env.render()
env.step(env.action_space.sample())
env.render()
print(':)')
