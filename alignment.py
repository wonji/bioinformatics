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
      self.result=['### Edit Distance Matrix ###']
      self.__mutation=self.backTrace()
      for line in self.__mat: self.result.append(str(line))
      self.result.extend([' ','### Minimum Distance :'+' '+str(self.calDistance()),' ','### Alignment Result ###'])
      self.result.extend(self.__mutation)
      print '\n'.join(self.result)

   def traceTool(self,i,j):
      if i==0 and j==0: return ''
      elif i==0:
         return 'i'+self.traceTool(i,j-1)
      elif j==0:
         return 'd'+self.traceTool(i-1,j)
      state=self.__mat[i][j]
      diag=self.__mat[i-1][j-1]
      left=self.__mat[i][j-1]
      up=self.__mat[i-1][j]
      if state==left+1:
         return 'i'+self.traceTool(i,j-1)
      if state==up+1:
         return 'd'+self.traceTool(i-1,j)
      if state==diag+1:
         return 's'+self.traceTool(i-1,j-1)
      if state==diag and self.__seq1[i-1]==self.__seq2[j-1]:
         return 'c'+self.traceTool(i-1,j-1)

   def backTrace(self):
         status = self.traceTool(len(self.__seq1),len(self.__seq2))[::-1]
         i,j=0,0
         ref,align='',''
         for base in status:
            if base=='c' or base=='s':
               ref+=self.__seq1[i]
               align+=self.__seq2[j]
               i+=1
               j+=1
            elif base=='i':
               ref+='-'
               align+=self.__seq2[j]
               j+=1
            elif base=='d':
               align+=self.__seq2[j]
               i+=1
               j+=1
         return [status,ref,align]
    



   homework = EditDistance("GCTGA","GGGTGA") 
   homework.calDistance()
   homework.backTrace()
   homework.showResult()
