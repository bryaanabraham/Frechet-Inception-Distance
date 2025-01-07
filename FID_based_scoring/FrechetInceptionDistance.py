import numpy as np
from PIL import Image
from data_loader import load_image

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