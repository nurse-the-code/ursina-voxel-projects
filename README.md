# ursina-voxel-projects

## Intro
This is one of my first non-trivial projects. Inspiration came from [Minecraft](https://www.minecraft.net/en-us) and
other related games.

[Ursina](https://www.ursinaengine.org/index.html) is an easy to use game engine built on top of
[Python](https://www.python.org) and [Panda3d](https://www.panda3d.org) (which is also a game engine).

This is project was initially based on my refactoring of ClearCode's walk through of "Creating Minecraft in Python"
([YouTube](https://www.youtube.com/watch?v=DHSRaVeQxIk),
[GitHub](https://github.com/clear-code-projects/Minecraft-in-Python)). Unfortunately, some of my original code base was
deleted while I was learning Git, so I am currently in the process of slowly adding back in old features that I had
created.

This project will in all likelihood be split into a series of projects.

## Getting Started

### On a Mac
<ol>
  <li>Make sure that the following are installed on your machine:
    <ul>
      <li><a href="https://brew.sh">Homebrew</a> (optional, but this is a popular tool for installing packages)
      <li><a href="https://git-scm.com">Git</a>
      <li><a href="https://github.com/pyenv/pyenv">pyenv</a> (Useful tool for managing different Python versions)
      <li><a href="https://python-poetry.org">Poetry</a> (Python Dependency management tool)
    </ul>
  <li>Use pyenv to install Python (e.g. <code>pyenv install 3.10.0</code>). You will need to install at Python 3.6 (or
higher). I recommend using Python 3.9 or 3.10, since that is what I am using for development.
  <li>Run the `script.py` file in the main directory. Left-clicking blocks create a new block adjacent to the block
surface you clicked. Right-clicking a block will destroy the block. Use WASD controls to move and hit the space bar to
jump. Your mouse controls the view window.
  <li>`Shift+Q` quits the program.
</ol>

## Roadmap
<ol>
  <li>Integrate my old code into this repo (the working bits).
  <li>Recreate my VoxelArray class. This will be a type of 3D array, with the ability to import 1D and 2D arrays. I will eventually include some array manipulation techniques.
  <li>Add back in block printing. This will allow block text (and in the future <a href="https://en.wikipedia.org/wiki/Pixel_art">pixel art</a> as well).
  <li>Develop a <a href="https://minecraft.fandom.com/wiki/Chunk">chunking system</a> to store and render voxel data. It will inherit from the VoxelArray class.
  <li>Create a system for making persistent changes to blocks. This will probably involve writing to a file system at first, but I may decide to incorporate a database instead.
  <li>Build a palette system to allow for there to be more diverse block types.
  <li>Make the voxel rendering more efficient by rendering each chunk as a single mesh and not rendering opaque voxel faces that are adjacent to another voxel.
  <li>TBD
</ol>
