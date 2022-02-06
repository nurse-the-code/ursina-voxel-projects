import ursina as u


class Voxel(u.Button):  # voxels are buttons so that you can create another voxel next to it
    """
    Simple Minecraft-styled blocks
    """

    def __init__(
            self,
            block_position: tuple = (0, 0, 0),
            block_texture: str = 'white_cube',
            block_color: u.color.Color = u.color.white,
            block_highlight_color=u.color.lime,
            is_color_random: bool = True
    ):
        if is_color_random:
            block_color = u.color.random_color()
        super().__init__(
            parent=u.scene,  # scene of the game
            position=block_position,  # will be changed later when game is set up
            model='cube',
            origin_y=0.5,  # the height in free-space of the quad
            texture=block_texture,  # initial default texture
            color=block_color,  # you need both a texture and a color
            highlight_color=block_highlight_color
        )

    def input(self, key):
        if self.hovered:
            # to create new voxels
            if key == 'left mouse down':
                # self.position is the position of the voxel the mouse is hovering on
                # mouse.normal is the surface of the voxel the mouse is hovering on
                voxel = Voxel(block_position=self.position + u.mouse.normal)

            # to destroy voxels
            if key == 'right mouse down':
                u.destroy(self)
