import math
def minmax(cur,node,maxTurn,scores,target):
    if cur==target:
        return scores[node]
    if(maxTurn):
        return max(minmax(cur+1,node*2,False,scores,target),minmax(cur+1,node*2+1,False,scores,target))
    else:
        return min(minmax(cur+1,node*2,True,scores,target),minmax(cur+1,node*2+1,True,scores,target))
scores=[3,8,1,25,14,7,3,9]
treedepth=math.log(len(scores),2)
print("The optimal value is: ",end=" ")
print(minmax(0,0,True,scores,treedepth))