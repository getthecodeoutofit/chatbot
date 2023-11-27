from bardapi import Bard

import os


os.environ["_BARD_API_KEY"] = "dQhqUV9m23PkEG7XkITyHG7tK5CkAgqtT0PHrFikfSzHYvOGqvljYFohyz6z4fdwyz_s5g."


def AI(message):
    a = Bard().get_answer(str(message+" tell in short"))
    return a['content']