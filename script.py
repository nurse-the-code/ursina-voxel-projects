import ursina as u
from ursina.color import random_color
from ursina.prefabs.first_person_controller import FirstPersonController  # not imported by default

from floor import Floor
from voxel import Voxel

app = u.Ursina()

# Create floor to place voxels on and so player doesn't fall through world infinitely
floor = Floor()

player = FirstPersonController()

app.run()  # CTRL + ALT + ESC to stop

# Allow `esc` key to quit app -- may need to rework if causing conflict with other input streams
def input(key):
    if key == 'escape':
        quit()
