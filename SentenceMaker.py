from string import maketrans

word = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
word1 = "map"

"""
print word
for x in ['k']:
    if x in word:
        word = word.replace(x,"m")

for y in ['o']:
    if y in word:
        word = word.replace(y,"q")

for z in ['e']:
    if z in word:
        word = word.replace(z,"g")


print word
"""

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = maketrans(intab, outtab)

print word.translate(trantab)
print word1.translate(trantab)
