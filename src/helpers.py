from ortools.sat.python import cp_model

"""
This module defines variable and value selection heuristics for
Google OR-Tools CP-SAT solver. It provides both heuristic strategies
and utility functions to retrieve them by name.
"""

# ======================================================
# VARIABLE SELECTION HEURISTICS
# ======================================================

def heuristica_mrv():
    """
    Return the MRV (Minimum Remaining Values) heuristic.

    This heuristic selects the variable with the smallest domain size first,
    which tends to reduce the branching factor and speed up the search.

    Returns:
        cp_model.DecisionStrategyProto.VariableSelectionStrategy:
            The OR-Tools constant representing MRV behavior.
    """
    return cp_model.CHOOSE_MIN_DOMAIN_SIZE


def heuristica_first_unbound():
    """
    Return the "first unbound" heuristic.

    This heuristic selects the first variable in the internal list
    that has not yet been assigned a value. It is the simplest
    and most direct strategy.

    Returns:
        cp_model.DecisionStrategyProto.VariableSelectionStrategy:
            The OR-Tools constant for choosing the first unbound variable.
    """
    return cp_model.CHOOSE_FIRST


def heuristica_random_variable():
    """
    Return a random variable selection heuristic.

    This heuristic selects variables in random order.
    It can be useful for exploring different solutions
    or escaping local optima.

    Returns:
        cp_model.DecisionStrategyProto.VariableSelectionStrategy:
            The OR-Tools constant for random variable selection.
    """
    return cp_model.CHOOSE_RANDOM_VARIABLE


# ======================================================
# VALUE SELECTION HEURISTICS
# ======================================================

def heuristica_lcv():
    """
    Return the LCV (Least Constraining Value) heuristic.

    In practice, this selects the smallest possible value for a variable,
    which usually represents the least constraining assignment in the domain.

    Returns:
        cp_model.DecisionStrategyProto.ValueSelectionStrategy:
            The OR-Tools constant for selecting the minimum value.
    """
    return cp_model.SELECT_MIN_VALUE


def heuristica_max_value():
    """
    Return the maximum-value selection heuristic.

    This heuristic always selects the largest available value
    within the variable's domain.

    Returns:
        cp_model.DecisionStrategyProto.ValueSelectionStrategy:
            The OR-Tools constant for selecting the maximum value.
    """
    return cp_model.SELECT_MAX_VALUE


def heuristica_random_value():
    """
    Return a random value selection heuristic.

    This heuristic assigns random values within the variable's domain,
    allowing stochastic exploration of the solution space.

    Returns:
        cp_model.DecisionStrategyProto.ValueSelectionStrategy:
            The OR-Tools constant for random value selection.
    """
    return cp_model.SELECT_RANDOM_VALUE


# ======================================================
# UTILITY FUNCTIONS
# ======================================================

def escolher_heuristica_variaveis(nome: str):
    """
    Select a variable heuristic strategy by name.

    Args:
        nome (str): The name of the heuristic.
            Accepted values: "mrv", "first", "random".

    Returns:
        cp_model.DecisionStrategyProto.VariableSelectionStrategy:
            The corresponding heuristic constant.

    Raises:
        ValueError: If the heuristic name is not recognized.
    """
    nome = nome.lower()
    if nome == "mrv":
        return heuristica_mrv()
    elif nome == "first":
        return heuristica_first_unbound()
    elif nome == "random":
        return heuristica_random_variable()
    else:
        raise ValueError(f"Unknown variable heuristic: {nome}")


def escolher_heuristica_valores(nome: str):
    """
    Select a value heuristic strategy by name.

    Args:
        nome (str): The name of the heuristic.
            Accepted values: "lcv", "max", "random".

    Returns:
        cp_model.DecisionStrategyProto.ValueSelectionStrategy:
            The corresponding heuristic constant.

    Raises:
        ValueError: If the heuristic name is not recognized.
    """
    nome = nome.lower()
    if nome == "lcv":
        return heuristica_lcv()
    elif nome == "max":
        return heuristica_max_value()
    elif nome == "random":
        return heuristica_random_value()
    else:
        raise ValueError(f"Unknown value heuristic: {nome}")


