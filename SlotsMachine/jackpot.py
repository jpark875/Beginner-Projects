import random
def pull_machine(symbols=['sevens', 'lemons', 'gold bars', 'cherries']):
    pull_nlist=[]
    for i in range(3):
        a=random.randint(0,(int(len(symbols))-1))
        pull_nlist.append(symbols[a])
    return pull_nlist

def jackpot():
    count=0
    while True:
        a=pull_machine()
        count += 1
        if (a==[a[0],a[0],a[0]]):
            return count
pull_machine()
