def rec_power(base,power):
    if(power==0):
        return 1
    if(power==1):
        return base
    if(power>1):
        return base*rec_power(base,power-1)
a=2
b=3
print(rec_power(a,b))