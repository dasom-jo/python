def average(*scores):
    #합계/개수
    #return sum(scores) / len(scores)
    total = 0 
    for s in scores:
        total += s
        length = len(scores)
        return total/length

print(average(10,60,80,50,1,2))