lst = list(range(1,101))
# print(lst)
lstpow = [n**2 for n in lst]
# print(lstpow)
print(-sum(lstpow)+sum(lst)**2)