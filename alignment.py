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
    s=Matrix((m,n))
    arrow=Matrix((m,n))

    for i in range(1,n):            #set the first row and first column 
        s[0][i]=s[0][i-1]+1
    for j in range(1,m):
        s[j][0]=s[j-1][0]+1

    for i in range(1,n):
        a


    
    for i in range(1,m):
        for j in range(1,n):
            s1=s[i-1][j-1]+grade(a[i-1],b[j-1]) # score from diagonal
            s2=s[i][j-1]+indel      #score from left
            s3=s[i-1][j]+indel      #score from up
            s[i][j]=min(s1,s2,s3)
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







