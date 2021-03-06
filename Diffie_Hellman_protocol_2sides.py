# Michał Plesiński 	WCY20KY1S1
from __future__ import print_function

#procedura generacja parametrów dziedziny
#wejscie:
# b - długość charakterystyki ciała p wyrażona w bitach.
#wyjscie:
#p – charakterystyka ciała Fp;
#n – rząd podgrupy cyklicznej;
#g – generator podgrupy cyklicznej rzędu n.



def generateDomain(b):
    p = next_prime(2^(b-1))
    while (not is_prime((p-1)//2)):
        p = next_prime(p)
    n = (p-1)//2
    F = GF(p)
    while True:
        g = F.random_element()
        if (g.multiplicative_order() == n):
            break
    return p, n, g

#procedura generacja pray kluczy publiczny/prywatny
#wejscie:
#p – charakterystyka ciała Fp;
#n – rząd podgrupy cyklicznej;
#g – generator podgrupy cyklicznej rzędu n.
#wyjscie:
#kpriv - klucz prywatny
#kpub - klucz publiczny

def keyGeneration(p, n, g):
    kpriv = randint(1, n-1)
    kpub = power_mod(g, kpriv, p)
    return kpriv, kpub

#procedura obliczania klucza sesji
#wejscie:
#kpub - klucz publiczny podnoszony do potęgi kpriv
#kpriv - klucz prywatny
#p – charakterystyka ciała Fp;

def sessionKey(kpub, kpriv, p):
    sessionKey = power_mod(kpub, kpriv, p)
    return sessionKey


#procedura sprawadzajaca czy klucze są równe 
#wejscie:
#sessionKeyA - klucz sesji dla A
#sessionKeyB - klucz sesji dla B
#wyjscie:
#"Tak" jesli sa takie same
#"Nie " jesli sa rozne 
def compare(sessionKeyA, sessionKeyB):
	print("Czy klucze sa takie same ? ")
	if (sessionKeyA == sessionKeyB):
		print("Tak")
	else:
		print("Nie")


#Realizacja protokołu

b = 256
print("Realizacja protokołu:")
print("Generacja dziedziny...")
p, n, g = generateDomain(b)
print("		p = ", p)
print("		n = ", n)
print("		g = ", g)

#generacja kluczy dla A
kprivA, kpubA = keyGeneration(p,n,g)
print("Klucz Prywatny dla A = ", kprivA)
print("Klucz Publiczny dla A = ", kpubA)
print("Wysyłam: " + str(kpubA) + " do B")

#generacja kluczy dla B
kprivB, kpubB = keyGeneration(p,n,g)
print("Klucz Prywatny dla B = ", kprivB)
print("Klucz Publiczny dla B = ", kpubB)
print("Wysyłam: " + str(kpubB) + " do A")

#obliczanie klucza sesji dla A
print("Obliczam klucz sesji dla A...")
sessionKeyA = sessionKey(kpubB, kprivA, p)
print("Klucz sesji dla A = ", sessionKeyA)

#obliczanie klucza sesji dla B
print("Obliczam klucz sesji dla B...")
sessionKeyB = sessionKey(kpubA, kprivB, p)
print("Klucz sesji dla B = ", sessionKeyB)

#porownanie kluczy
compare(sessionKeyA, sessionKeyB)
