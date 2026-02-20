from manim import *
from typing import Union

def write_on_screen(scene:Scene,msg, already_existing:Union[Text,None]):
    if already_existing:
        scene.remove(already_existing)
        # already_existing.set_text(msg)
        # return already_existing
    txt=Text(msg).move_to([-3, -3, 0])
    scene.add(txt)
    return txt