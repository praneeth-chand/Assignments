weight = 5
cost = [20,10,4,50,100]
kgs = [1,2,3,4,5]
result=[]
def removeNegativeweights(cost ,kgs):
  count_of_negatives = cost.count(-1)
  for i in range(count_of_negatives):
    x=cost.index(-1)
    cost.pop(x)
    kgs.pop(x)
removeNegativeweights(cost,kgs)
def MinimumCost(weight,cost,kgs):
  for i in range(len(cost)2):
    minimum_price = min(cost)
    kgs_min_price = kgs[cost.index(minimum_price)]
    x =weight // kgs_min_price
    if x!=0 :
      result.append(minimum_price*x)
      cost.remove(minimum_price)
      kgs.remove(kgs_min_price)
    weight = weight - kgs_min_price*x
  if weight!=0:
    return "cant buy"
  else:
    return sum(result)
print(MinimumCost(weight,cost,kgs))
