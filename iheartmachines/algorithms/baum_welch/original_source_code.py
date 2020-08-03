

def number(num):
    return float(num)


def normalize(arr):
    """ Normalize the values and make sure they sum to 1.zero """
    sumarr = number(sum(arr))
    if sumarr != 0.0:
        for i in range(len(arr)):
            arr[i] = arr[i] / sumarr


# A probable and finite automaton model's state (I,F,S,T
# I - ...
# F - ...
# S - ...
# T - ...


# This creates a model that has zero probabilities
def empty_model(num_states, alphabet):
    """ creates a model that has zero probabilities """
    pass


def random_model(num_states, alphabet):
    """ creates a model that is fully connected and has random probabilities """
    pass


def compute_probability_recursion(I, F, S, T, sequence, index, state, dp_dict):
    """ calculates the string probabilities using recursion """
    pass


def compute_probability(I, F, S, T, sequence, dp_dict):
    """ Calculates the string probabilities forward using recursion """
    pass


def compute_probabilities(I, F, S, T, sett):
    """ Calculates all the probabilities from an example list """
    pass


def compute_probability_recursion_reverse(I, F, S, T, sequence, index, state, dp_dict):
    """ Calculates the string probabilities backward using recursion """
    pass


def compute_probability_reverse(I, F, S, T, sequence, dp_dict):
    """ Compute string probabilities backward using A recursion """
    pass


def compute_probabilities_reverse(I, F, S, T, sett):
    """ Computes all probabilities from an example list """
    pass


def iterate_em(I, F, S, T, sett):
    """ Unknown purpose... """
    pass


def loglikelihood(probs):
    """ Unknown purpose... """
    pass


def readset(f):
    """ Unknown purpose... """
    pass


def writeprobs(probs, f):
    """ Unknown purpose... """
    pass




