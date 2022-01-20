import ursina as u
from ursina.color import random_color
from ursina.prefabs.first_person_controller import FirstPersonController  # not imported by default
from voxel import Voxel

app = u.Ursina()

# Create an 16 x 16 voxel platform on the horizontal plane
for z in range(16):
    for x in range(16):
        voxel = Voxel(block_position=(x, 0, z))

player = FirstPersonController()

app.run()  # CTRL + ALT + ESC to stop
