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

def trace(C):
  Tr = 0
  for i in range(len(C)):
    Tr += C[i][i]
  return Tr

def covariance(matrix1, matrix2):
  combined_matrix = np.column_stack((matrix1, matrix2))
  return np.cov(combined_matrix, rowvar=False)

def FID_helper(image1, image2):
  
  mu1 = image1.mean(axis=0)
  mu2 = image2.mean(axis=0)

  ms = np.sum((mu1 - mu2) ** 2)

  c1, c2 = covariance(image1, mu1), covariance(image2, mu2)
  C = (c1 + c2 - 2 * np.sqrt(c1 * c2))
  Tr = trace(C)

  return ms + Tr

def FID(image1, image2):

  r1, g1, b1 = load_image(image1)
  r2, g2, b2 = load_image(image2)

  fid_score_r = FID_helper(r1, r2)
  fid_score_g = FID_helper(g1, g2)
  fid_score_b = FID_helper(b1, b2)

  return (fid_score_r + fid_score_g + fid_score_b)/3

from FrechetInceptionDistance import FID

if __name__ == '__main__':
    # example usage
    genrated_image = 'path/to/generated/image.png'
    real_image = '/path/to/real/image.png'

    fid_score = FID(genrated_image, real_image)
    print(f"FID Score: {fid_score}")