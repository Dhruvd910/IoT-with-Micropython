window=5
buf=[]
while True:
    x=float(input('Value: '))
    buf.append(x)
    if len(buf)>window: buf.pop(0)
    print(sum(buf)/len(buf))