from PIL import Image
import numpy as np

def load_image(image_path):

  image = Image.open(image_path)
  image = image.resize((200, 200))
  image = image.convert('RGB')
  rgb_matrix = np.array(image)

  red = rgb_matrix[:, :, 0]/255
  green = rgb_matrix[:, :, 1]/255
  blue = rgb_matrix[:, :, 2]/255

  return red, green, blue