# kicad_python 
# Read Me
# Introduction
Welcome to my GitHub page! This repository is dedicated to a comprehensive tutorial on using Python with KiCad, the popular open-source software suite for electronic design automation. Whether you're new to KiCad or looking to enhance your workflow with Python scripting, this tutorial will guide you through the essential steps, from setting up your environment to automating complex tasks. Dive in and start exploring how Python can help you streamline your PCB design process with KiCad!
The code example below demonstrates how to:

Set up a path for your KiCad schematic.
Clone and move schematic elements.
Modify component values.
Save your changes to the schematic.

# Credit
Special thanks to psychogenic's [KiCad Skip](https://github.com/psychogenic/kicad-skip?tab=readme-ov-file)repository, which inspired this tutorial and provided valuable insights into integrating Python with KiCad.
# Load the library
We are using the library called kicad-skip.

`pip install kicad-skip`

or try this if previous one doesn't work

`pip3 install kicad-skip`
# Step-by-Step Guide

## 1. Set Up the Schematic Path
To begin, you need to specify the path to the KiCad schematic file you want to manipulate. Use the following line of code to set up the path:

```python
from skip import Schematic

# Specify the path to your KiCad schematic file
sch = Schematic("file path")
```
Make sure to replace the path with the location of your own schematic file.


## Clone the object
```python
a = sch.symbol.R2.clone()
```
Cloning a component makes an exact copy of the specified element, which can then be manipulated. You can't add an new element, you can only clone an existed one. 


## Move the object 
```python

sch.symbol.R2.move(100,100)
```
We could move any elements use the fucntion `move(x_value, y_value)`

in this case, the component is moved 50 units to the right and 100 units down.
