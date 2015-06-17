seq1=raw_input("Enter the first sequence: ")
seq2=raw_input("Enter the second sequence: ")

def Matrix(matrix):
    mat=[[0 for x in range(matrix[1])] for x in range(matrix[0])]
    return mat
          
    indel=1
    sub=1
    copy=0

def grade(a, b):
    if a==b:
        return copy
    else:
        return sub
    
def score(a,b,s):
    m=len(a)+1   # length of sequence 1
    n=len(b)+1   # length of sequence 2 
    tb=Matrix((m,n))
    s=tb
    for i in range(1,n):            #set the first row and first column 
        s[0][i]=s[0][i-1]+1
    for j in range(1,m):
        s[j][0]=s[j-1][0]+1
    
    for i in range(1,m):
        for j in range(1,n):
            s1=s[i-1][j-1]+grade(a[i-1],b[j-1]) # score from diagonal
            s2=s[i][j-1]+indel      #score from left
            s3=s[i-1][j]+indel      #score from up
            s[i][j]=min(s1,s2,s3)
            return s


