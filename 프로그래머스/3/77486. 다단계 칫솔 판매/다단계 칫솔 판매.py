def solution(enroll, referral, seller, amount):
    recommends = [-1 for i in range(len(enroll))]
    result = [0 for i in range(len(enroll))]
    dict_name = {}
    
    idx = 0
    for name in enroll:
        dict_name[name] = idx
        idx += 1
    
    for i in range(len(referral)):
        if referral[i] != '-':
            target = dict_name[referral[i]]
            recommends[i] = target
    
    for i in range(len(seller)):
        start = dict_name[seller[i]]
        money = amount[i] * 100
        tax_calculator(recommends, result, money, start)
        
    return result

def tax_calculator(follow, result, money, start):
    tax = int(money / 10)
    
    result[start] += money - tax
    
    if follow[start] == -1 or tax == 0:
        return
    else:
        tax_calculator(follow, result, tax, follow[start])