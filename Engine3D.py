from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import *

width = 1200
height = 675


rend = Renderer(width, height)
rend.background = Texture("models/stadium.bmp")
rend.glClearBackground()

rend.active_shader = rgbGlow
rend.active_texture = Texture("models/Ivysaur.bmp")
rend.glLoadModel("models/ivysaur.obj",
                 translate = V3(3, 0, -10),
                 rotate = V3(0, 90, 0), 
                 scale = V3(2,2,2))

rend.active_shader = heatmap
rend.glLoadModel("models/groudon.obj",
                 translate = V3(-.9, -0.8, -1.5),
                 rotate = V3(0, 0, 45), 
                 scale = V3(1,1,1))

rend.active_shader = static
rend.active_texture = Texture("models/mimikyu.bmp")
rend.glLoadModel("models/mimikyu.obj",
                 translate = V3(-3, 0, -10),
                 rotate = V3(0, -45, 0), 
                 scale = V3(2,2,2))


rend.active_shader = white
rend.glLoadModel("models/charizard.obj",
                 translate = V3(6, 3, -11),
                 rotate = V3(-45, -145, -90), 
                 scale = V3(4.5,4.5,4.5))

rend.active_shader = purpleGlow
rend.glLoadModel("models/mewtwo.obj",
                 translate = V3(-0.2, -0.5, -3),
                 rotate = V3(0, 45, 0), 
                 scale = V3(1,1,1))

rend.glFinish("output.bmp")
