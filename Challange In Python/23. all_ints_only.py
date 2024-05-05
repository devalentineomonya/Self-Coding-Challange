def only_ints(par1, par2):
    return isinstance(par1, int) and isinstance(par2, int)

print(only_ints(1,"w"))