import numpy as np
import matplotlib.pyplot as plt


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


def plot_vectors_2d(vectors, labels, colors=None):
    """
    Plots 2D vectors on a Cartesian plane.
    :param vectors: List of vectors to be plotted (each should be a 2-element numpy array)
    :param labels: Labels for the vectors
    :param colors: Optional list of colors for each vector
    """

    plt.figure(figsize=(8, 6))
    for i, vector in enumerate(vectors):
        plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=colors[i] if colors else 'b')
        plt.text(vector[0], vector[1], labels[i], ha='center', va='center', color=colors[i] if colors else 'b')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('2D Vector Plot')
    plt.grid(True)
    plt.show()


def plot_vectors_3d(vectors, labels, colors=None):
    """
    Plots 3D vectors in a 3D Cartesian space.
    :param vectors: List of vectors to be plotted (each should be a 3-element numpy array)
    :param labels: Labels for the vectors
    :param colors: Optional list of colors for each vector
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i, vector in enumerate(vectors):
        ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color=colors[i] if colors else 'b')
        ax.text(vector[0], vector[1], vector[2], labels[i], ha='center', va='center', color=colors[i] if colors else 'b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Vector Plot')


def visualize_matrix_transformation(matrix, vector):
    """
    Visualizes the effect of a matrix transformation on a 2D vector.
    :param matrix: 2x2 numpy array representing the transformation matrix
    :param vector: 2-element numpy array representing the vector
    """
    transformed_vector = np.dot(matrix, vector)
    plot_vectors_2d([vector, transformed_vector], ['Original', 'Transformed'], ['r', 'g'])


def normalize_vector(vector):
    """
    Normalizes a vector to a unit vector.
    """
    norm = np.linalg.norm(vector)
    return vector / norm


def subtract_vectors(v1, v2):
    """
    Subtracts vector v2 from v1.
    """
    return np.subtract(v1, v2)


def rotate_vector(vector, angle_degrees):
    """
    Rotates a 2D vector by a given angle in degrees.
    """
    angle_radians = np.deg2rad(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians)],
                                [np.sin(angle_radians),  np.cos(angle_radians)]])
    return np.dot(rotation_matrix, vector)


def vector_projection(u, v):
    """
    Computes the projection of vector u onto vector v.
    """
    scalar_proj = np.dot(u, v) / np.dot(v, v)
    return scalar_proj * v


def plot_vectors_with_angle(u, v):
    """
    Plots two vectors and displays the angle between them.
    """
    import matplotlib.pyplot as plt
    origin = [0, 0]
    plt.quiver(*origin, u[0], u[1], color='r', angles='xy', scale_units='xy', scale=1, label='Vector u')
    plt.quiver(*origin, v[0], v[1], color='b', angles='xy', scale_units='xy', scale=1, label='Vector v')

    # Compute angle
    dot_prod = np.dot(u, v)
    cos_theta = dot_prod / (np.linalg.norm(u) * np.linalg.norm(v))
    theta_rad = np.arccos(cos_theta)
    theta_deg = np.degrees(theta_rad)
    
    plt.title(f"Angle between vectors: {theta_deg:.2f} degrees")
    plt.legend()
    plt.grid(True)
    plt.xlim(-5, 10)
    plt.ylim(-5, 10)
    plt.show()


def plot_vector_projection(u, v):
    """
    Plots vectors u, v, and the projection of u onto v.
    """
    import matplotlib.pyplot as plt
    origin = np.array([0, 0])
    plt.figure(figsize=(8,6))
    plt.quiver(*origin, u[0], u[1], color='r', angles='xy', scale_units='xy', scale=1, label='Vector u')
    plt.quiver(*origin, v[0], v[1], color='b', angles='xy', scale_units='xy', scale=1, label='Vector v')
    proj = vector_projection(u, v)
    plt.quiver(*origin, proj[0], proj[1], color='g', angles='xy', scale_units='xy', scale=1, label='Projection of u onto v')
    plt.legend()
    plt.grid(True)
    plt.xlim(-1, max(u[0], v[0], proj[0]) + 2)
    plt.ylim(-1, max(u[1], v[1], proj[1]) + 2)
    plt.show()
