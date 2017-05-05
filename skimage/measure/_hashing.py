from skimage.color import rgb2gray
from skimage.transform import resize

def average_hash(image, hash_size=8):
	"""
	Average Hash computation

	Implementation follows http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html

	Step by step explanation: https://www.safaribooksonline.com/blog/2013/11/26/image-hashing-with-python/

	"""

	# reduce size and complexity, then covert to grayscale
	image = resize(rgb2gray(image), (hash_size, hash_size))

	# find average pixel value; 'pixels' is an array of the pixel values, ranging from 0 (black) to 255 (white)image
	avg = np.mean(image)

	# create string of bits
	diff = image > avg
	# make a hash
	return diff.flatten().astype(int)