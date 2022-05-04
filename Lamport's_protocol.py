#WCY20KY1S1 Michał Plesiński Lab2b
import hashlib
import hmac
import binascii
import string
import random
#zalozenia protokołu: 
# jednokierunkowa funkcja do identyfikacj uzytkownika
# uzytkownik zapamietuje i zachowuje wartosc x0 
# xk jako wyniki dzialania f(xk-1)
# generujemy az do xn
# wysylamy xn systemowi 
# to bedzie identyfikator, a xk-1 haslo
# kroki protokolu:
# 1. uzytkownik przesyla aktualny identyfikator xk
# 2. uzytkownik sprawdza istnienie uzytkownika o otrzymanym identyfikatorze
# 3. system zada podania hasla czyli xk-1
# 4. system weryfikuje poprawnoc hasla, sprawdzajac czy f(xk-1) = xk
# jesli tak to xk-1 staje sie identyfikatorem, axk-2 nowym hasłem
#zmienne globalne


#inicjalizacja tablic 10 kluczami, w ktorych argument zerowy jest losową liczbą
#kazdy nastepny liczby wartosc na postawie argumentu poprzedniego
def zapelnienieTablicy(n):
    tab = []
    keyint = randint(2^12,2^16)
    key = str(keyint)
    skrotzKlucza = hashlib.sha3_512()
    skrotzKlucza.update(key.encode())
    hashT = skrotzKlucza.hexdigest()
    for i in range(n):
        tab.append(hashT)
        skrotzKlucza = hashlib.new('sha3_512')
        skrotzKlucza.update(tab[i].encode())
        hashT = skrotzKlucza.hexdigest()
    #else:
        #print("zapelniono tablice")
    return tab, tab[n-1]


tabA, lastA = zapelnienieTablicy(10)
tabB, lastB = zapelnienieTablicy(10)
tabC, lastC = zapelnienieTablicy(10)

def tabPop(tab):
    last = tab.pop()
    return last


    

#uzywamy tablicy 3x1 do weryfikacji
#w pierwszej iteracji tablica ma wartosci An, Bn, Cn
#w celu weryfikacji wysylaja An, Bn,Cn do systemu 
tabS = []
def tablicaSystemInicjalizacja(tabS,tabA,tabB,tabC):
    tabS.append(tabPop(tabA))
    tabS.append(tabPop(tabB))
    tabS.append(tabPop(tabC))
    print("System otrzymal od uzytkownikow A,B,C ich identyfikatory.\n")
    return tabS
tabS = tablicaSystemInicjalizacja(tabS,tabA,tabB,tabC)
print("ID A: ", tabS[0])
print("ID B: ", tabS[1])
print("ID C: ", tabS[2])
print("\n")

#teraz tablice maja po 9 wartosci, na końcu jest hasło
#w tablicy systemowej są wszedzie loginy
#system dostaje haslo i haszuje je, musi mu wyjść login
#jeśli się uda, stare hasło staje sie nowym loginem

def ktoryUzytkownik():
    ktory = randint(0,2)
    return ktory

for i in range(10):
    uzytkownik = ktoryUzytkownik()
    print("Uzytkownik nr: ",uzytkownik)
    if uzytkownik == 0:
        print("System: Prosba do uzytkownika A o identyfikator")
        print("Otrzymano identyfikator od uzytkownika A = ",lastA)
        test = (lastA == tabS[0])
        print("Czy identyfikator istnieje: ",test)
        if test == True:
            print("Wysłano prośbę o hasło użytkownika A")
            print("Otrzymano hasło użytkownika A: ",tabA[-1])
            skrotUzytkownik = hashlib.new('sha3_512')
            skrotUzytkownik.update(tabA[-1].encode())
            hashA = skrotUzytkownik.hexdigest()
            print("Oczekiwany identyfikator A obliczony na podstawie hasła: ",hashA)
            test2 = (tabS[0] == hashA)
            if test2 == True:
                print("Poprawnie zweryfikowano uzytkownika A, zaktualizowano tablice systemową")
                print("\n")
                tabS[0] = tabA.pop()
                lastA = tabS[0]
    if uzytkownik == 1:
        print("System: Prosba do uzytkownika B o identyfikator")
        print("Otrzymano identyfikator od uzytkownika B = ",lastB)
        test = (lastB == tabS[1])
        print("Czy identyfikator istnieje: ",test)
        if test == True:
            print("Wysłano prośbę o hasło użytkownika B")
            print("Otrzymano hasło użytkownika B: ",tabB[-1])
            skrotUzytkownik = hashlib.new('sha3_512')
            skrotUzytkownik.update(tabB[-1].encode())
            hashB = skrotUzytkownik.hexdigest()
            print("Oczekiwany identyfikator B obliczony na podstawie hasła: ",hashB)
            test2 = (tabS[1] == hashB)
            if test2 == True:
                print("Poprawnie zweryfikowano uzytkownika B, zaktualizowano tablice systemową")
                print("\n")
                tabS[1] = tabB.pop()
                lastB = tabS[1]
    if uzytkownik == 2:
        print("System: Prosba do uzytkownika C o identyfikator")
        print("Otrzymano identyfikator od uzytkownika C = ",lastC)
        test = (lastC == tabS[2])
        print("Czy identyfikator istnieje: ",test)
        if test == True:
            print("Wysłano prośbę o hasło użytkownika C")
            print("Otrzymano hasło użytkownika C: ",tabC[-1])
            skrotUzytkownik = hashlib.new('sha3_512')
            skrotUzytkownik.update(tabC[-1].encode())
            hashC = skrotUzytkownik.hexdigest()
            print("Oczekiwany identyfikator C obliczony na podstawie hasła: ",hashC)
            test2 = (tabS[2] == hashC)
            if test2 == True:
                print("Poprawnie zweryfikowano uzytkownika C, zaktualizowano tablice systemową")
                print("\n")
                tabS[2] = tabC.pop() #stare hasło staje sie nowym loginem
                lastC = tabS[2] #stare hasło staje sie nowym loginem

            
