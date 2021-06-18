

def BestSum(Target, arr, memo = {}):
    if Target in memo: return memo[Target]
    if Target == 0: return []
    if Target < 0: return None

    best_result = None
    for num in arr:
        Target_remain = Target - num
        result = BestSum(Target_remain, arr, memo)
        if result is not None:
            result.append(num)
            print(result)
            if (best_result is None) or (len(result) < len(best_result)):
                best_result = result[:]
        
    memo[Target] = best_result
    return best_result


arr = [5,10,12,13,15,18]
ans = BestSum(30, arr)
if ans is None:
    print('No solution')
else:
    print(ans)

