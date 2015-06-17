seq1=raw_input("Enter the first sequence: ")
seq2=raw_input("Enter the second sequence: ")

def Matrix(matrix):
    mat=[[0 for x in range(matrix[0])] for x in range(matrix[1])]
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
    s1=s[i-1][j-1]+grade(a,b)
    s2=s[i][j-1]+indel
    s3=s[i-1][j]+indel
    s[i][j]=min(s1,s2,s3)
    return s



