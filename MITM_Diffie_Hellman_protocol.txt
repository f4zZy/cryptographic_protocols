# Michał Plesiński WCY20KY1S1
from __future__ import print_function

#procedura generowanie parametrów dziedziny
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
	
	
#procedura generacja pary kluczy publiczny/prywatny
#wejscie:
#p – charakterystyka ciała Fp;
#n – rząd podgrupy cyklicznej;
#g – generator podgrupy cyklicznej rzędu n.
#wyjscie:
#kpriv - klucz prywatny
#kpub - klucz publiczny

def generujA(p, n, g):
    secretA = randint(1, n-1)
    kpubA = power_mod(g, secretA, p)
    return secretA, kpubA
	
def generujB(p, n, g):
    secretB = randint(1, n-1)
    kpubB = power_mod(g, secretB, p)
    return secretB, kpubB
def generujC(p, n, g):
    secretC = randint(1, n-1)
    kpubC = power_mod(g, secretC, p)
    return secretC, kpubC

#procedura obliczania klucza sesyjnego
#wejscie:
#kpub - klucz publiczny
#kpriv - klucz prywatny
#p – charakterystyka ciała Fp;

def sessionKey(kpub, kpriv, p):
    sessionKey = power_mod(kpub, kpriv, p)
    return sessionKey
	
	
#procedura sprawadzajaca czy klucze są równe 
#wejscie:
#sessionKeyA - klucz sesji dla A
#sessionKeyB - klucz sesji dla B
#sessionKeyC - klucz sesji dla C
#wyjscie:
#"Tak" jeśli  sessionKeyA == sessionKeyB == sessionKeyC
#"Nie" w kazdym innym wypadku
def is_equal(sessionKeyA, sessionKeyB, sessionKeyC):
	print("Czy klucze sa takie same ? ")
	if (sessionKeyA == sessionKeyB == sessionKeyC):
		print("Tak")
	else:
		print("Nie")


#Kolejne kroki protokołu

b = 512
p, n, g = generateDomain(b)
print("Wygenerowano p: ", p)
print("Wygenerowano n: ", n)
print("Wygenerowano g: ", g)

#Generacja kluczy publicznych oraz kluczy prywatnych dla kazdego uczestnika protokołu
secretA, kpubA = generujA(p, n, g)
secretB, kpubB = generujB(p, n, g)
secretC, kpubC = generujC(p, n, g)


#Przesyłanie kluczy
#Uzytkownik A przesyła kpubA do B, uzytkownik B przesyła kpubB do C, uzytkownik C przesyła kpubC do A
#A posiada kpubC
#B posiada kpubA
#C posiada kpubB

print("\nUżytkownik A przesłał swoj klucz publiczny do B. kpubA =  ", kpubA)
print("Użytkownik B przesłał swoj klucz publiczny do C. kpubB =  ", kpubB)
print("Użytkownik C przesłał swoj klucz publiczny do A. kpubC =  ", kpubC)


#Uzytkownicy obliczają nowe klucze.
#A oblicza kpubCA i przesyła do B
#B oblicza kpubAB i przesyła do C
#C oblicza kpubBC i przesyła do A

kpubCA = sessionKey(kpubC, secretA, p)
kpubAB = sessionKey(kpubA, secretB, p)
kpubBC = sessionKey(kpubB, secretC, p)

print("\nUzytkownik A obliczyl kpubCA = ", kpubCA)
print("Uzytkownik B obliczyl kpubAB = ", kpubAB)
print("Uzytkownik C obliczyl kpubBC = ", kpubBC)

#Nastepnie uzytkownik A przesyła klucz kpubCA do B, uzytkownik B przesyła klucz kpubAB do C, a uzytkownik C przesyla kpubBC do A

print("\nUżytkownik A przesłał swoj nowy klucz publiczny do B. kpubCA=  ", kpubCA)
print("Użytkownik B przesłał swoj nowy klucz publiczny do C. kpubAB=  ", kpubAB)
print("Użytkownik C przesłał swoj nowy klucz publiczny do A. kpubBC=  ", kpubBC)

#Uzytkownicy A, B i C liczą ostatni, właściwy klucz sesji
#A oblicza kpubBCA
#B oblicza kpubCAB
#C oblicza kpubABC

kpubBCA = sessionKey(kpubBC, secretA, p)
kpubCAB = sessionKey(kpubCA, secretB, p)
kpubABC = sessionKey(kpubAB, secretC, p)

#Sprawdzenie czy klucze są równe
is_equal(kpubBCA, kpubCAB, kpubABC)
print("Obliczone klucze: ")
print("Klucz kpubBCA =  ", kpubBCA)
print("Klucz kpubCAB =  ", kpubCAB)
print("Klucz kpubABC =  ", kpubABC)







