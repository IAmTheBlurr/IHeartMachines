
from typing import List, Tuple


def forward_backward(observations: List, states: List[int], start_probability: List, transition_probability, emission_probability, end_state) -> Tuple:
    """
    Original implementation (with modifications for clarity) from the Markov Model book

    Args:
        observations (List):
        states (List[Tuple]):
        start_probability (List):
        transition_probability ():
        emission_probability ():
        end_state ():

    Returns:
        Tuple: Forward, Backward, Posterior

    """
    forward = []
    forward_previous = []
    forward_current = []
    backward = []
    backward_previous = {}
    backward_current = []

    # Contains merger of both the forward and backward parts
    posterior = []

    # This is the forward part of the algorithm
    for index, observation in enumerate(observations):
        forward_current = {}

        for state in states:
            if index == 0:
                # bae case for the forward part
                previous_forward_sum = start_probability[state]
            else:
                previous_forward_sum = sum(forward_previous[k_state] * transition_probability[k_state][state] for k_state in states)

            forward_current[state] = emission_probability[state][observation] * previous_forward_sum

        forward.append(forward_current)
        forward_previous = forward_current

    previous_forward = sum(forward_current[state] * transition_probability[state][end_state] for state in states)

    # This is the backward part of this algorithm
    for index, observation_plus in enumerate(reversed(observations[1:] + [None, ])):     # TODO -> Original code used `(None,)` as a tuple, Pycharm claimed "unexpected"
        backward_current = {}

        for state in states:
            if index == 0:
                # base case for backward part
                backward_current[state] = transition_probability[state][end_state]
            else:
                backward_current[state] = sum(transition_probability[state][l_state] * emission_probability[l_state][observation_plus] * backward_previous[l_state] for l_state in states)

        backward.insert(0, backward_current)
        backward_previous = backward_current

    previous_backward = sum(start_probability[l_state] * emission_probability[l_state][observations[0]] * backward_current[l_state] for l_state in states)

    for index in range(len(observations)):
        posterior.append({state: forward[index][state] * backward[index][state] / previous_forward for state in states})

    assert previous_forward == previous_backward
    return forward, backward, posterior
