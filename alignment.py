<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> f81d8ba3861f618b39f36ccc2947a369dcd6c1c5
seq1=raw_input("Enter the first sequence: ")
seq2=raw_input("Enter the second sequence: ")

def Matrix(matrix):
    mat=[[0 for x in range(matrix[1])] for x in range(matrix[0])]
    return mat
          
    indel=1
    sub=1
    copy=0

def grade(a,b):
    if a==b:
        return copy
    else:
        return sub
    
def score(a,b):
    m=len(a)+1   # length of sequence 1
    n=len(b)+1   # length of sequence 2 
<<<<<<< HEAD
    tb=Matrix((m,n))
    s=tb
=======
    s=Matrix((m,n))
    arrow=Matrix((m,n))
>>>>>>> f81d8ba3861f618b39f36ccc2947a369dcd6c1c5

    for i in range(1,n):            #set the first row and first column 
        s[0][i]=s[0][i-1]+1
    for j in range(1,m):
        s[j][0]=s[j-1][0]+1
<<<<<<< HEAD
=======

    for i in range(1,n):
        a


>>>>>>> f81d8ba3861f618b39f36ccc2947a369dcd6c1c5
    
    for i in range(1,m):
        for j in range(1,n):
            s1=s[i-1][j-1]+grade(a[i-1],b[j-1]) # score from diagonal
            s2=s[i][j-1]+indel      #score from left
            s3=s[i-1][j]+indel      #score from up
            s[i][j]=min(s1,s2,s3)
<<<<<<< HEAD
    return s 
>>>>>>> 307ffb986ae447093528be44df133d2b22c50cf2


wonji = EditDistance("GCTGA","GGGTGA")
wonji.calDistance()
wonji.showResult()
=======
    return s



i,j=m-1,n-1
oo=''

def backtrack(s):
    s1=s[i-1][j-1]  #diagonal 0 
    s2=s[i][j-1]    #left 1
    s3=s[i-1][j]    #up 2
    mi=min(s1,s2,s3)
    
    if s1==mi:
        oo+='0'
        i-=1
        j-=1
    elif s2==mi:
        oo+='1'
        j-=1
    else:
        oo+='2'
        i-=1

    ss=[]
    for ii in range(i+1):        #extract submatrix
        sss=s[0:i+1][ii][0:j+1]
        ss.append(sss)
        
    s=ss

    if s==[]:
        return oo
    else: 
        return backtrack(s)







>>>>>>> f81d8ba3861f618b39f36ccc2947a369dcd6c1c5
