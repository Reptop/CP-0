# Author: Raed K
# Date April 30th 2024

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm


def is_convex(values):
    # Check if the second difference is non-negative
    return all(
        values[i - 2] - 2 * values[i - 1] + values[i] >= 0
        for i in range(2, len(values))
    )


def is_log_convex(values):
    # Check if the second difference of the log of the values is non-negative
    log_values = np.log(values)
    return all(
        log_values[i - 2] - 2 * log_values[i - 1] + log_values[i] >= 0
        for i in range(2, len(log_values))
    )


# Define the matrix A as a function of time t, scaled to prevent overflow
def matrix_A():
    # scale_factor = 1 / (1 + np.abs(t))

    # return np.array(
    # return np.array([[0.23, -0.18, -0.61], [-0.59, 0.25, -0.2], [-0.45, -0.56, 0.56]])
    # [[0.23, 0.18, 0.61], [0.59, 0.25, 0.2], [0.45, 0.56, 0.56]]

    # )

    intermediate = np.round(np.random.rand(3, 3), 2)
    # intermediate[0][0] = -intermediate[0][0]
    # intermediate[1][1] = -intermediate[1][1]
    # intermediate[2][2] = -intermediate[2][2]

    return intermediate


# return np.round(np.random.rand(3, 3), 2)
# [-0.0028, 1.3e-8], [5000, -0.016]]


# )


def matrix_D():
    # Convert the list to a numpy array before creating the diagonal matrix
    # return np.diag(np.array([0.4, 0.5, 0.1]))

    return np.diag([0.62875, 1])


# diag_entries = np.random.rand(3)
# return np.diag(diag_entries)


def spectral_radius(matrix):
    if not np.isfinite(matrix).all():
        print("Matrix contains inf or NaN:", matrix)
        return 0  # Or handle the error as appropriate

    eigenvalues = np.linalg.eigvals(matrix)
    return max(abs(eigenvalues))


# Time range for the model
# time_steps = range(0, 150)

constant_B = matrix_A()
constant_A = -constant_B

print("Constant A Below: ")
print(constant_A)


constant_D = np.diag(np.random.rand(3))  # Create negative random diagonal entries


time_steps = np.linspace(0.0, 5.0, 100)

# Compute the spectral radius for each time step
spectral_radii = []
finite_values = True  # Flag to indicate if all values are finite


for t in time_steps:
    A_tau = expm(constant_A * t)  # Compute e^(A*t) using the constant matrix A

    # overflow check
    if not np.isfinite(A_tau).all():
        print(f"Overflow occurred at time step {t}")
        finite_values = False
        break

    # D_A_tau = np.dot(matrix_D(), A_tau)  # Compute D * e^(A*t)
    D_A_tau = np.dot(constant_D, A_tau)
    # Compute D * e^(A*t) using the constant matrix D

    spectral_radius_value = spectral_radius(D_A_tau)

    if spectral_radius_value <= 0:
        print(f"Spectral radius non-positive at time step {t}")
        finite_values = False
        break

    spectral_radii.append(spectral_radius_value)

for i in range(len(spectral_radii)):
    print(spectral_radii[i])


if finite_values:  # Only proceed with plotting and checks if all values are finite
    log_spectral_radii = np.log(spectral_radii)

    # Plotting the spectral radius
    plt.figure(figsize=(10, 5))
    plt.plot(time_steps, spectral_radii, label="Spectral Radius")
    plt.title("Spectral Radius of De^A(tau) Over Time")
    plt.xlabel("Time")
    plt.ylabel("Spectral Radius")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Plotting the log of the spectral radius
    # plt.figure(figsize=(10, 5))
    # plt.plot(time_steps, log_spectral_radii)
    # plt.title("Log of Spectral Radius of De^A(tau) Over Time")
    # plt.xlabel("Time")
    # plt.ylabel("Log of Spectral Radius")
    # plt.grid(True)
    # plt.show()

    # Checking for convexity and log-convexity
    convex = is_convex(spectral_radii)
    # log_convex = is_log_convex(spectral_radii)

    # Output the results of the convexity checks
    print(f"The graph is {'convex' if convex else 'not convex'}.")
    # print(f"The graph is {'log-convex' if log_convex else 'not log-convex'}.")
else:
    print("Calculation stopped due to non-finite matrix values.")
