def MinimumCost(weight,cost,kgs):
  result=[]
  for i in range(len(cost)):
    minimum_price = min(cost)
    kgs_min_price = kgs[cost.index(minimum_price)]
    x =weight // kgs_min_price
    if x!=0 :
      result.append(minimum_price*x)
      cost.remove(minimum_price)
      kgs.remove(kgs_min_price)
    weight = weight - kgs_min_price*x
  if weight!=0:
    return -1
  else:
    return sum(result)
def removeNegativeweights(weight,cost ):
  kgs = [1,2,3,4,5]
  count_of_negatives = cost.count(-1)
  for i in range(count_of_negatives):
    x=cost.index(-1)
    cost.pop(x)
    kgs.pop(x)
  return MinimumCost(weight,cost,kgs)

