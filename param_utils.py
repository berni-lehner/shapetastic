from itertools import product

def expand_parameter_lists(parameters):
    # Expand generators in the dict into list of values
    parameters = {
        key: list(val) if hasattr(val, '__iter__') and not isinstance(val, list) and not isinstance(val, str) else val
        for key, val in parameters.items()
    }

    return parameters


def create_parameter_combinations(parameters):
    # Expand generators in the dict into list of values
    parameters = expand_parameter_lists(parameters)

    # Turn all non-list values into a list to make it compatible with itertools.product()
    parameters = {key: [val] if not isinstance(val, list) else val for key, val in parameters.items()}

    # Create all possible combinations of parameter values
    combinations = product(*parameters.values())

    # Turn each combination into a separate dict within a list
    keys = parameters.keys()
    combinations = [dict(zip(keys, combination)) for combination in combinations]

    return combinations