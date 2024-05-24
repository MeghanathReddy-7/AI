MAX,MIN=float('inf'),float('-inf')
def minmax(cur,node,maxTurn,scores,alpha,beta):
    if cur==3:
        return scores[node]
    if(maxTurn):
        best=MIN
        for i in range(2):
            value=minmax(cur+1,node*2+i,False,scores,alpha,beta)
            best=max(best,value)
            alpha=max(best,alpha)
            if alpha<=beta:
                break
        return best
    else:
        best=MAX
        for i in range(2):
            value=minmax(cur+1,node*2+i,True,scores,alpha,beta)
            best=min(best,value)
            beta=min(beta,best)
            if alpha<=beta:
                break
        return best
values = [3, 5, 6, 9, 1, 2, 0, -1]
print("The optimal value is:", minmax(0, 0, True, values, MIN, MAX))
