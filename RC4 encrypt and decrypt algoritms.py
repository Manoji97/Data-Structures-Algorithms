## RC4 algorithm
def RC4(pas):
    t = [0] * 256
    for i in range(256):
        t[i] = pas[i%len(pas)]
    
    ne = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + ne[i] +  ord(t[i])) %256
        ne[i],ne[j] = ne[j],ne[i]
    return ne


# encrypr decrypt
def encrypt_decrypt(txt):
    ne = RC4('kyc@pass.key')
    l = len(txt)
    i = 0
    j = 0
    k = []
    while l>0:
        i = (i+1)%256
        j = (j + ne[i])%256
        ne[i],ne[j] = ne[j],ne[i]
        k.append(ne[(ne[i] + ne[j]) % 256])
        l -= 1
    
    op = []
    for i in range(len(txt)):
        op.append(ord(txt[i]) ^ k[i])
    
    return ''.join(chr(i) for i in op)

encrypt_decrypt('627836436')

ls = [ord('!'),ord('@'),ord('#'),ord('$'),ord('%'),ord('^'),ord('&'),ord('*')
      ,ord('('),ord(')'),ord('-'),ord('='),ord('_'),ord(':'),ord(';'),ord('+'),48,49,50,51,52,53,54,55,56,57]




txt = '563657467835575'
ne = RC4('kyc@pass.key')
l = len(txt)
i = 0
j = 0
k = []
while l>0:
    i = (i+1)%256
    j = (j + ne[i])%256
    ne[i],ne[j] = ne[j],ne[i]
    k.append(ne[(ne[i] + ne[j]) % 256])
    l -= 1

op = []
for i in range(len(txt)):
    op.append(ord(txt[i]) ^ k[i])
o = ''.join(chr(i) for i in op)