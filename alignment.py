class EditDistance(object):
 def getSeq1(self):
  return self.__seq1
 def setSeq1(self,value):
  self.__seq1=value
 def getSeq2(self):
  return self.__seq2
 def setSeq2(self,value):
  self.__seq2=value
 def __init__(self, seq1, seq2):
  self.setSeq1(seq1)
  self.setSeq2(seq2)
 def Matrix(self, matrix):
  self.__mat=[[0 for x in range(matrix[1])] for x in range(matrix[0])]
  self.__mat[0] = [x for x in range(matrix[1])] 
  for i in range(matrix[0]-1):
   self.__mat[i+1][0] = i+1
  return self.__mat
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
  self.__row = len(self.__seq1)
  self.__col = len(self.__seq2)
  self.__mat = self.Matrix((self.__row+1,self.__col+1))
  for i in range(self.__row):
   for j in range(self.__col):
    self.__mat[i+1][j+1] = self.score(self.__seq1[i],self.__seq2[j],i+1,j+1,self.__mat)
  return self.__mat[self.__row][self.__col]
 def getMatrix(self):
  return self.__mat
 def showResult(self):
  self.result=['Edit Distance Matrix']
  for line in self.__mat: self.result.append(str(line))
  self.result.extend([' ','Minimum Distance :'+' '+str(self.calDistance())])
  print '\n'.join(self.result)


wonji = EditDistance("GCTGA","GGGTGA")
wonji.calDistance()
wonji.showResult()
