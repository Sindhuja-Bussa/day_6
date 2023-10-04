
'''#tower of hanoi
def toh(n,src,aux,des):
    if n>0:
        toh(n-1,src,des,aux)
        print(src,des)
        toh(n-1,aux,src,des)
n=int(input())
toh(n,'a','b','c')

#tower of hanoi_count
count=0
def toh(n,src,aux,des):
    global count
    if n==1:
        count=count+1
        return
    toh(n-1,src,des,aux)
    count=count+1
    toh(n-1,aux,src,des)
n=int(input())
src,aux,des='a','b','c'
toh(n,src,aux,des)
print(count)

#generate parentheses
l=[]
res=[]
def backtrack(n,opencount=0,closecount=0):
    if opencount==closecount==n:z
        res.append("".join(l))
    if opencount<n:
        l.append('(')
        backtrack(n,opencount+1,closecount)
        l.pop()
    if closecount<opencount:
        l.append(')')
        backtrack(n,opencount,closecount+1)
        l.pop()
    return res
n=int(input())
print(backtrack(n))

#n queen problem

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=[]
        posdiag=[]
        negdiag=[]
        board=[["."]*n for i in range(n)]
        ans=[]
        def backtracking(r):
            if r==n:
                l=["".join(i) for i in board]
                ans.append(l)
                return
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                board[r][c]='Q'
                col.append(c)
                posdiag.append(r+c)
                negdiag.append(r-c)

                backtracking(r+1)

                board[r][c]="."
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
        backtracking(0)
        return ans

#no.of solutions in n queen problem
class Solution:
    def totalNQueens(self, n: int) -> int:
        col=[]
        posdiag=[]
        negdiag=[]
        board=[["."]*n for i in range(n)]
        ans=[]
        def backtracking(r):
            if r==n:
                l=["".join(i) for i in board]
                ans.append(l)
                return
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                board[r][c]='Q'
                col.append(c)
                posdiag.append(r+c)
                negdiag.append(r-c)

                backtracking(r+1)

                board[r][c]="."
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
        backtracking(0)
        return len(ans)
        
#subset sum
from itertools import combinations
def subset(arr,tar):
    for i in range(len(arr)+1):
        for j in combinations(arr,i):
            if sum(j)==tar:
                return True



l=[]
nums=(input().split(','))
for i in nums:
      l.append(int(i))
target=int(input())
print(subset(l,target))'''
