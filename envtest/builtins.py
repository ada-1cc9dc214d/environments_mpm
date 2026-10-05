import pandas as pd
from scipy.ndimage import gaussian_filter
import numpy as np

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'get_dataframe_summary']


def rand_array(shape):
    return np.random.rand(*shape)
def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)
def my_mat_solve(A, b):
    return A.inv()*b

def get_dataframe_summary(data_dict):
    """Converts a dictionary to a Pandas DataFrame and calculates column averages."""
    if not data_dict:
        raise ValueError("Input data cannot be empty.")

    df = pd.DataFrame(data_dict)
    numeric_means = df.select_dtypes(include='number').mean()
    return numeric_means.to_dict()
