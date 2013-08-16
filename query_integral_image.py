
import numpy as np

def query_integral_image( integral_image, size_x, size_y):
     x = integral_image.shape[0]
     y = integral_image.shape[1]
     area, i, j=0,0,0
     hits = 0
     
    # count how many possible locations
     for i in xrange(x - size_x):
          for j in xrange(y - size_y):
               area = integral_image[i, j] + integral_image[i + size_x, j + size_y]
               area -= integral_image[i + size_x, j] + integral_image[i, j + size_y]
               if not area:
                    hits += 1
     if not hits:
          # no room left
          return None
    # pick a location at random
     goal = np.random.randint(hits)
     hits = 0
     for i in xrange(x - size_x):
          for j in xrange(y - size_y):
               area = integral_image[i, j] + integral_image[i + size_x, j + size_y]
               area -= integral_image[i + size_x, j] + integral_image[i, j + size_y]
               if not area:
                    hits += 1
                    if hits == goal:
                         return i, j
