# Josephus Sequence Problem
def Sequence_prob(n, position):
    sequence =[]
    table = []
    for i in range(1, n+1):
        table.append(i)
    j =1
    while len(table) > 1:
        person= table.pop(0)
        if  j % position  == 0:
            sequence.append(person)
        else:
            table.append(person)
        j+=1

    sequence.append(table.pop())
    return sequence
print(Sequence_prob(7,3))