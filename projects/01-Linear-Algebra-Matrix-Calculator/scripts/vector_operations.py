import numpy as np


def add_vectors(v1, v2):
    """
    Adds two vectors element-wise.
    :param v1: List or numpy array representing vector 1
    :param v2: List or numpy array representing vector 2
    :return: Element-wise sum of v1 and v2 as a numpy array
    """
    return np.add(v1, v2)


def scalar_multiply(vector, scalar):
    """
    Multiplies a vector by a scalar.
    :param vector: List or numpy array representing the vector
    :param scalar: Scalar value to multiply each element of the vector
    :return: Scaled vector as a numpy array
    """
    return np.multiply(vector, scalar)


def dot_product(v1, v2):
    """
    Computes the dot product of two vectors.
    :param v1: List or numpy array representing vector 1
    :param v2: List or numpy array representing vector 2
    :return: Dot product as a scalar value
    """
    return np.dot(v1, v2)


def cross_product(v1, v2):
    """
    Computes the cross product of two vectors (3D vectors only).
    :param v1: List or numpy array representing vector 1 (3 elements)
    :param v2: List or numpy array representing vector 2 (3 elements)
    :return: Cross product as a numpy array
    """
    return np.cross(v1, v2)


# Example usage (to be deleted in production code):
if __name__ == "__main__":
    vector_a = np.array([1, 2, 3])
    vector_b = np.array([4, 5, 6])
    print(f"Vector A: {vector_a}")
    print(f"Vector B: {vector_b}")
    print(f"Add Vectors: {add_vectors(vector_a, vector_b)}")
    print(f"Scalar Multiply: {scalar_multiply(vector_a, 2)}")
    print(f"Dot Product: {dot_product(vector_a, vector_b)}")
    print(f"Cross Product: {cross_product(vector_a, vector_b)}")
