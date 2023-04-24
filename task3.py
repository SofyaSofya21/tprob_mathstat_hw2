# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

import formulae as f

n = 144
p = 0.5
k = 70

res = f.bernulli(n,k,p) # 0.0628

print(res)