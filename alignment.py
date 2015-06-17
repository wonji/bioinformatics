class EditDistance(object):
 __seq1=""
 __seq2=""

 indel=1
 sub=1
 copy=0

 def __init__(self, seq1, seq2):
  self.__seq1=seq1
  self.__seq2=seq2

 def Matrix(self, matrix):
  mat=[[0 for x in range(matrix[0])] for x in range(matrix[1])]
  mat[0] = [x for x in range(matrix[0])] 
  for i in range(matrix[1]-1):
   mat[i+1][0] = i+1
  return mat

 def grade(self, a, b):
  if a==b:
   return copy
  else:
   return sub
  
 def score(self, a,b,i,j,s):
  s1=s[i-1][j-1]+grade(a,b)
  s2=s[i][j-1]+indel
  s3=s[i-1][j]+indel
  s[i][j]=min(s1,s2,s3)
  return s 
