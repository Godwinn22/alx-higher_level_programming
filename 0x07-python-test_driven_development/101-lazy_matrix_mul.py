#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.
        
    Raises:
        ValueError: If the matrices cannot be multiplied due to incompatible dimensions.
    """
    # Convert input lists to NumPy arrays
    np_a = np.array(m_a)
    np_b = np.array(m_b)

    # Perform matrix multiplication
    result = np.matmul(np_a, np_b)

    return result
