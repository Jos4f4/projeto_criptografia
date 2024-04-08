# Quebrando a cifra de César

import sys
from string import lowercase as lc

file = open(sys.argv[1], 'r').read().lower()

for key in range(1, 26):
    result = ''
    print('Key: ', key)
    for lt in file:
        if lt in lc:
            idx = lc.find(lt)
            idx = (idx - key)%26
            result += lc[idx]
        else:
            result += lt
    print(result,)	
