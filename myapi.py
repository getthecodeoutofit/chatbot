from bardapi import Bard

import os


os.environ["_BARD_API_KEY"]="dQhqUeA-ywNoXX_1D0sxuNTdoDJcmgKqDAmfC4Odq-_8BrkoqejLpXwFrrBARHClipDdXA."


def AI(message):
    a = Bard().get_answer(str(message))
    return a['content']