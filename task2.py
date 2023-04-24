# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
# Какова вероятность, что ни одна из них не перегорит в первый день? 
# Какова вероятность, что перегорят ровно две?

import formulae as f

p = 0.0004
n = 5000

# Какова вероятность, что ни одна из них не перегорит в первый день? 
k1 = 0
res1 = f.bernulli(n,k1,p) # 0.135

print(res1)

# Какова вероятность, что перегорят ровно две?
k2 = 2
res2 = f.bernulli(n,k2,p) # 0.271

print(res2)