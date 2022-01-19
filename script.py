import ursina as u
from ursina.color import random_color
from ursina.prefabs.first_person_controller import FirstPersonController # not imported by default



class Voxel(u.Button): # voxels are buttons so that you can create another voxel next to it
    def __init__(self, position = (0, 0, 0)):
        '''
        0, 0, 0 appears to be in the center of the upper face of the voxel.
        '''

        super().__init__(
            parent = u.scene, # that is the scene of the game
            position = position, # will be changed later when game is set up
            model = 'cube',
            origin_y = 0.5, # the height in freespace of the cube
            texture = 'white_cube', # initial default texture
            color = u.color.white, # you need both a texture and a color
            highlight_color = u.color.lime
        )



    def input(self, key):
        if self.hovered:
            # to create new voxels
            if key == 'left mouse down':
                # self.position is the the position of the voxel the mouse is hovering on
                # mouse.normal is the surface of the voxel the mouse is hovering on
                voxel = Voxel(position = self.position + u.mouse.normal)

            # to destroy voxels
            if key == 'right mouse down':
                u.destroy(self)

app = u.Ursina()

# Create an 16 x 16 voxel platform on the horizontal plane
for z in range(16):
    for x in range(16):
        voxel = Voxel(position = (x, 0, z))


player = FirstPersonController()


app.run() # CTRL + ALT + ESC to stop