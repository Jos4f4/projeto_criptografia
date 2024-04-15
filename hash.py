import sys, hashlib

#Executar um input e leitura de variável

dgst = hashlib.md5(sys.argv[1]).hexdigest|()
dgst1 = hashlib.sha224(sys.argv[1]).hexdigest|()
dgst2 = hashlib.sha512(sys.argv[1]).hexdigest|()

print(dgst) 
print(dgst1)
print(dgst2)