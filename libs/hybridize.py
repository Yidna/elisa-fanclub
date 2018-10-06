import numpy as np
from scipy import signal


def hybrid_image(a, b, sigma):
    blur_img = np.zeros(a.shape)
    high_freq = np.zeros(b.shape)

    blur_img[:, :, 0] = gaussconvolve2d(a[:, :, 0], sigma)
    blur_img[:, :, 1] = gaussconvolve2d(a[:, :, 1], sigma)
    blur_img[:, :, 2] = gaussconvolve2d(a[:, :, 2], sigma)

    high_freq[:, :, 0] = gaussconvolve2d(b[:, :, 0], sigma)
    high_freq[:, :, 1] = gaussconvolve2d(b[:, :, 1], sigma)
    high_freq[:, :, 2] = gaussconvolve2d(b[:, :, 2], sigma)

    high_freq = (np.clip((blur_img / 255) - (high_freq / 255), 0, 1)) * 255

    return np.clip((blur_img.astype(np.float64) + high_freq), 0, 255)


def gaussconvolve2d(array, sigma):
    """
    Performs a convolution of the array with a gaussian filter of sigma.
    :param array: input numpy array
    :param sigma: input sigma (int, float)
    :return: numpy array
    """
    gauss_filter = gauss2d(sigma)
    return signal.convolve2d(array, gauss_filter, 'same')


def gaussian(sigma, x_dist):
    """
    Applies gaussian function over sigma and the x distance
    :param sigma: int, float
    :param x_dist: numpy float array
    :return: numpy float array
    """
    return np.exp(-(x_dist ** 2) / (2 * sigma ** 2))


def gauss1d(sigma):
    """
    Return a 1-d gaussian filter of size next or current odd of the ceiling of 6*sigma
    :param sigma: int, float
    :return: numpy array of size of ceiling of 6*sigma
    """
    # Take the celiing of the sigma * 6
    array_length = math.ceil(sigma * 6)
    # Ensure that array length is odd
    if array_length % 2 == 0:
        array_length = array_length + 1
    # Find the center of the array
    center = array_length / 2
    # Create the distance array starting from -center to center
    x_dist = np.arange(-center, center)
    # Apply gaussian on each element
    ret = gaussian(sigma, x_dist)
    # Return normalized result
    return ret / np.sum(ret)


def gauss2d(sigma):
    """
    Creates a 2-D gaussian filter.
    :param sigma: int, float
    :return: numpy array
    """
    # Create the new dimension
    gauss2d_temp = gauss1d(sigma)[np.newaxis]
    # calculate a transpose of the array
    gauss2d_temp_trans = gauss2d_temp.T
    # Gaussian 2D = convolution of 1D Gaussian with its transpose
    gauss2d_result = signal.convolve2d(gauss2d_temp, gauss2d_temp_trans)
    return gauss2d_result