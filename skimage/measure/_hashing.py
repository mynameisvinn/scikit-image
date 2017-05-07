from skimage.color import rgb2gray
from skimage.transform import resize
import numpy as np

__all__ = ['average_hash']

def average_hash(image, hash_size=8):
	"""Compute the average hash for a given image.
	
	Parameters
	----------
	image : ndarray
		Image. Any dimensionality.
	hash_size : int, optional
		Size of calculated hash.

	Returns
	-------
	image_hash : ndarray
		1-dimensional ndarray.

	Notes:
	------
	Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html
	"""
	if hash_size < 0:
		raise ValueError("Hash size must be positive")

	image = resize(rgb2gray(image), (hash_size, hash_size))
	avg = np.mean(image)
	diff = image > avg
	image_hash = diff.flatten().astype(int)
	return image_hash