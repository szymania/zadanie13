import pandas as pd
import aseegg as ag
import matplotlib.pyplot as plt
import numpy as np



t = np.linspace(0, 38.02, 200*38.02)
dane = pd.read_csv(r"C:\Users\ASUS\Desktop\kck\zadanie13\sub01_trial03.csv", delimiter=',', engine='python', header = None)
czestProbkowania = 200
sygnal = dane[1]
sygnal2 = dane[5]
przefiltrowanySygnal = ag.pasmowoprzepustowy(ag.pasmowozaporowy(sygnal, czestProbkowania, 49, 51), czestProbkowania, 1, 50)

plt.subplot(3, 1, 1)
plt.title("Sygnał przed filtracją")
plt.ylabel('Amplituda [µV]')
plt.xlabel('Czas [s]')
plt.plot(t, sygnal)

plt.subplot(3, 1, 2)
plt.title("Przefiltrowany sygnał")
plt.ylabel('Amplituda [µV]')
plt.xlabel('Czas [s]')
plt.plot(t, przefiltrowanySygnal)

plt.subplot(3, 1, 3)
plt.title("Wyświetlenia liczb")
plt.ylabel('Liczba')
plt.xlabel('Czas [s]')
plt.plot(t, sygnal2)

plt.show()

kod = []
poprzednia=0
p = 0
for i in range(len(przefiltrowanySygnal)):
    p+=1 ###przerwa pomiędzy powtarzającymi się liczbami
    if przefiltrowanySygnal[i] > 0.05 :
        liczba = sygnal2[i]
        if poprzednia != liczba:   ###czy znaleziona cyfra jest różna od poprzedniej
            kod.append(liczba)
            poprzednia = liczba
        elif p > 10:
            kod.append(liczba)
        p = 0
print(kod)
