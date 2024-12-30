import numpy as np

def neutrosophic_scaling(value, neutrosophic_state):
    """
    Applies a basic neutrosophic scaling to a value.

    Args:
        value: The value to scale.
        neutrosophic_state: A dictionary with 'T', 'I', and 'F' components.

    Returns:
        The scaled value.
    """
    T = neutrosophic_state.get("T", 1.0)
    I = neutrosophic_state.get("I", 0.0)
    F = neutrosophic_state.get("F", 0.0)

    return T * value + I * np.random.uniform(0, value) - F * value
