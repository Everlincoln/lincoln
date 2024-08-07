numbers=["0","1","10","999","-1","1.2","1.1.1",".1","abc","a1","⅔","2²","D"]

for n in numbers:
    print(f'{n}.isdigit(): {n.isdigit()}')    
    print(f'{n}.isnumeric(): {n.isnumeric()}')    
    print(f'{n}.isdecimal(): {n.isdecimal()}')
    print()