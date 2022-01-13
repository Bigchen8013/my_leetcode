

ss = 'abd'
sa = 'dba'

hashmap1,hashmap2 = {}, {}

for ch in ss:
    hashmap1[ch] = hashmap1.get(ch,0) + 1

for hh in sa:
    hashmap2[hh] = hashmap2.get(hh,0) + 1

print(hashmap1,'----------')
print(hashmap2,'++++++++++')

if hashmap1 == hashmap2:
    print("相等")