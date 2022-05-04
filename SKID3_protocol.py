#PLESIŃSKI MICHAŁ WCY20KY2S1

import hashlib
import hmac
import binascii


key = "1234567890ABCDEF"
keyh = binascii.unhexlify(key)
B = "Bob"
A = "Alice"

#procedura wylosowania pseudolosowej liczby dla A
#wyjscie - randA
def losujA():
    randA = randint(1,100)
    print("Wylosowano dla A: ", randA)
    return randA

#procedura wylosowania pseudolosowej liczby dla B
#wyjscie - randB
def losujB():
    randB = randint(1,100)
    print("Wylosowano dla B: ", randB)
    return randB

#procedura obliczajaca HMAC dla uzytkownika B
#wejscie - keyh, randA, randB, B
#wyjscie - h.hexdigest()
def obliczHmacB(keyh, randA, randB, B):
    m = str(randA) + str(randB) + B
    h = hmac.new( keyh, m.encode(), hashlib.sha256 )
    print("Obliczono HMAC: " ,h.hexdigest() )
    return h.hexdigest()

#procedura obliczajaca HMAC dla uzytkownika A
#wejscie - keyh, randB, A
#wyjscie - h.hexdigest()
def obliczHmacA(keyh, randB, A):
    m = str(randB) + A
    h = hmac.new( keyh, m.encode(), hashlib.sha256 )
    print("Obliczono HMAC: " ,h.hexdigest() )
    return h.hexdigest()


#Realizacja protokołu

#wylosowanie liczby pseudolosowej dla uzytkownika A
print("KROK 1")
randA = losujA()

#przesłanie randA do B
print(" ")
print("KROK 2")
print("Uzytkownik A wyslal randA do uzytkownika B")

#użytkownik B wybiera liczbę losową RandB i wysyła ją do użytkownika A wraz z danymi
randB = losujB()

print(" ")
print("KROK 3")
#obliczenie HMAC dla uzytkownika B i wyslanie do A randB i HMAC
hmacB = obliczHmacB(keyh, randA, randB, B)
print("Uzytkownik B przesyla do A randB, HMAC:", randB, hmacB)

#Obliczenie HMAC po stronie A i weryfikacja wartosci
print("Uzytkownik A oblicza HMAC")
test_hmacb = obliczHmacB(keyh, randA, randB, B)
test = (test_hmacb == hmacB)
if(test):
    print("Wartosci sa identyczne")


#obliczenie HMAC dla A i przesłanie wartosci do B
print(" ")
print("KROK 4")
hmacA = obliczHmacA(keyh, randB, A)
print("Uzytkownik A przesyla do B HMAC: ", hmacA)

#Obliczenie HMAC i weryfikacja wartosci
print("Uzytkownik B oblicza HMAC")
test_hmaca = obliczHmacA(keyh, randB, A)
test1 = (test_hmaca == hmacA)
if(test1):
    print("Uwierzytelnianie sie powiodlo")
    
