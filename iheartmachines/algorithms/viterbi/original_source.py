
from typing import List


def dictionary_print_table(viterbi_states):
    """ I think this thing just prints bullshit out to the screen for "logging" """
    # From dictionary printing the table of steps
    yield ' '.join(('%12d' % i) for i in range(len(viterbi_states)))

    for state in viterbi_states[0]:
        yield '%.7s: ' % state + ' '.join('%.7s' % ('%f' % viterbi_datum[state]['prob'] for viterbi_datum in viterbi_states))


def viterbi(observations: List, states: List, start_probability, transition_probability, emission_probability):
    """ Original implementation (with modifications for clarity) from the Markov Model book """
    viterbi_states = [{}]

    for state in states:
        viterbi_states[0][state] = {
            'prob': start_probability[state] * emission_probability[state][observations[0]],
            'prev': None
        }

        # When t > 0, run Viterbi
        for t in range(1, len(observations)):
            viterbi_states.append({})

            for state in states:
                maximum_transition_probability = max(viterbi_states[t - 1][previous_state]['prob'] * transition_probability[previous_state][state] for previous_state in states)

                for previous_state in states:
                    if viterbi_states[t - 1][previous_state]['prob'] * transition_probability[previous_state][state] == maximum_transition_probability:
                        maximum_probability = maximum_transition_probability * emission_probability[state][observations[t]]
                        viterbi_states[t][state] = {'prob': maximum_probability, 'prev': previous_state}
                        break

        for line in dictionary_print_table(viterbi_states):
            print(line)

        opt = []

        # The highest likelihood
        maximum_probability = max(value['prob'] for value in viterbi_states[-1].values())
        previous = None

        # Get the most likely state, as well as it's backtract
        for state, data in viterbi_states[-1].items():
            if data['prob'] == maximum_probability:
                opt.append(state)
                previous = state
                break

        # Following the backtract until the first observation
        for t in range(len(viterbi_states) - 2, -1, -1):
            opt.insert(0, viterbi_states[t + 1][previous]['prev'])
            previous = viterbi_states[t + 1][previous]['prev']

        print(f'The steps of state are ${opt} with the highest probability of ${maximum_probability}')
