from docs.DirectionalLight_example import ground
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()
Sky()

player = Entity(model='cube', color=color.blue, y=1)
ground = Entity(model='cube', scale=10, color=color.light_gray, collider='box')