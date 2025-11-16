
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()


for i in range(20):
    for j in range(20):
        box = Button(color=color.light_gray, model='cube', position=(i,0,j), texture='grass.png', colliders='box',
                     parent=scene, origin_y=0.5)

app.run()