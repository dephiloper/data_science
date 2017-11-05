from random import randint


""" Some functions for basic linear algebra opertations based on python lists. """

def vector_add(a, b):
  #####################################################################
  # TODO (0,5):                                                       #
  # vector a + vector b as defined in the notebook                    #
  #####################################################################
  if len(a) != len(b):
    return None
  vec = []
  for i in range(len(a)):
    vec.append(a[i]+b[i])
   
  return vec
  #####################################################################
  #                       END OF YOUR CODE                            #
  #####################################################################

def vector_sub(a, b):
  #####################################################################
  # TODO (0,5):                                                       #
  # vector a - vector b as defined in the notebook                    #
  #####################################################################
  if len(a) != len(b):
    return None
  vec = []
  for i in range(len(a)):
    vec.append(a[i]-b[i])
   
  return vec
  #####################################################################
  #                       END OF YOUR CODE                            #
  #####################################################################

def vector_scalar_mul(r, a):
  #####################################################################
  # TODO (0,5):                                                       #
  # scalar r * vector a as defined in the notebook                    #
  ##################################################################### 
  vec = []
  for i in range(len(a)):
    vec.append(r*a[i])
   
  return vec
  #####################################################################
  #                       END OF YOUR CODE                            #
  #####################################################################

def vector_dot(a, b):
  #####################################################################
  # TODO (1):                                                         #
  # vec a * vec b (inner product) as defined in the notebook          #
  #####################################################################
  if len(a) != len(b):
    return None
  sum = 0
  for i in range(len(a)):
    sum = sum + a[i] * b[i]
   
  return sum
  #####################################################################
  #                       END OF YOUR CODE                            #
  #####################################################################

def create_random_matrix(n, m):
  #####################################################################
  # TODO (1):                                                         #
  # creates a NxM matrix with random numbers between 0 and 255        #
  #####################################################################
  if n == m == 0:
    return None
  mat = []
  for i in range(n):
    mat.append([])
    for j in range(m):
        mat[i].append(randint(0, 255))
        
  return mat
  #####################################################################
  #                       END OF YOUR CODE                            #
  #####################################################################

def matrix_vector_mul(mat, vec):
  #####################################################################
  # TODO (1):                                                         #
  # matrix A * vector a (inner product)	as defined in the notebook    #
  #####################################################################
  if len(mat) > 0 and len(mat[0]) != len(vec):
    return None
  result = []
  for i in range(len(mat)):
    sum = 0
    for j in range(len(mat[i])):
      sum = sum + mat[i][j] * vec[j]
    result.append(sum)
                   
  return result
  #####################################################################
  #                       END OF YOUR CODE                            #
  #####################################################################

def matrix_transpose(a):
  #####################################################################
  # TODO (1):                                                         #
  # transpose a matrix A as defined in the notebook                   #
  #####################################################################  
  mat = []

  for i in range(len(a)):
    mat.append([])
    for j in range(len(a[i])):
      mat[i].append(a[j][i])

  return mat
  #####################################################################
  #                       END OF YOUR CODE                            #
  #####################################################################