""" ./iheartmachines/algorithms/forward_backward/forward.py """


class Forward(object):
    """ Object model for the "forward" part of the Forward/Backward algorithm """
    def __init__(self):
        self.current = None
        self.previous = None
