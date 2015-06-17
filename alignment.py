class EditDistance(object):
 __seq1="" #±‚¡∏¿« sequence#
 __seq2="" #πŸ≤Ô sequence#
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
  return min(s1,s2,s3)
 def calDistance(self):
  self.__row = len(self.__seq1)
  self.__col = len(self.__seq2)
  self.mat = self.Matrix((self.__row+1,self.__col+1))
  for i in range(self.__row):
   for j in range(self.__col):
    self.mat[i+1][j+1] = self.score(self.__seq1[i],self.__seq2[j],i+1,j+1,self.__mat)
  return self.mat
  

wonji = EditDistance("GCTGA","GGGTGA")
wonji.calDistance()



class EditDistance(object):
 def __init__(self, seq1, seq2):
  self.seq1=seq1
  self.seq2=seq2
 def Matrix(self, matrix):
  mat=[[0 for x in range(matrix[0])] for x in range(matrix[1])]
  mat[0] = [x for x in range(matrix[0])] 
  for i in range(matrix[1]-1):
   mat[i+1][0] = i+1
  return mat
 def grade(self, a, b):
  if a==b:
   return 0 #copy
  else:
   return 1 #substitution
 def score(self, a,b,i,j,s):
  s1=s[i-1][j-1]+self.grade(a,b)
  s2=s[i][j-1]+1 #insertion
  s3=s[i-1][j]+1 #deletion
  return min(s1,s2,s3)
 def calDistance(self):
  self.row = len(self.seq1)
  self.col = len(self.seq2)
  self.mat = self.Matrix((self.row+1,self.col+1))
  for i in range(self.row):
   for j in range(self.col):
    self.mat[i+1][j+1] = self.score(self.seq1[i],self.seq2[j],i+1,j+1,self.mat)
  return self.mat