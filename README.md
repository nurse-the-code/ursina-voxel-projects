# ursina-voxel-projects

## Intro
This is one of my first non-trivial projects. Inspiration came from [Minecraft](https://www.minecraft.net/en-us) and other related games.

[Ursina](https://www.ursinaengine.org/index.html) is an easy to use game engine built on top of [Python](https://www.python.org) and [Panda3d](https://www.panda3d.org) (which is also a game engine).

This is project was initially based on my refactoring of ClearCode's walk through of "Creating Minecraft in Python" ([YouTube](https://www.youtube.com/watch?v=DHSRaVeQxIk), [GitHub](https://github.com/clear-code-projects/Minecraft-in-Python)).

This project will in all liklihood be split in to a series of projects.

## Getting Started
<ol>
  <li>Clone the git repo.
  <li>
</ol>

## Roadmap
<ol>
  <li>Integrate my old code into this repo (the working bits).
  <li>Recreate my VoxelArray class. This will be a type of 3D array. I will include some array manipulation techniques and the ability to import 1D and 2D arrays.
  <li>Add back in block printing. This will allow block text (and in the future <a href="https://en.wikipedia.org/wiki/Pixel_art">pixel art</a> as well).
  <li>Develop a <a href="https://minecraft.fandom.com/wiki/Chunk">chunking system</a> to store and render voxel data. It will inherit from the VoxelArray class.
  <li>Build a palette system to allow for their to be more diverse block types
  <li>Make the voxel rendering more efficient by rendering each chunk as a single mesh and not rendering opaque voxel faces that are adjacent to another voxel.
  <li>TBD
</ol>
