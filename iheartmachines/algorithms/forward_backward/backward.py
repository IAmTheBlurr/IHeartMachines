""" ./iheartmachines/algorithms/forward_backward/backward.py """


class Backward(object):
    """ Object model for the "backward" part of the Forward/Backward algorithm """
    def __init__(self):
        self.current = None
        self.previous = None
