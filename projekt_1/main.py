import pandas
import pandas_ta as pta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import (MultipleLocator)


def ema(N, arr):
    ema = []
    alfa = 2 / (N + 1)
    for i in range(len(arr)):
        nom = 0
        denom = 0
        for j in range(i, max(-1, i - (N + 1)), -1):
            if pandas.notnull(arr[j]):
                nom += arr[j] * ((1 - alfa)**(i - j))
                denom += (1 - alfa)**(i - j)
        ema.append(nom / denom)
    return ema


def isBuyingPoint(macd_0, signal_0, macd_1, signal_1):
    if macd_0 < signal_0 and macd_1 > signal_1:
        return True
    else:
        return False


def isSellingPoint(macd_0, signal_0, macd_1, signal_1):
    if macd_0 > signal_0 and macd_1 < signal_1:
        return True
    else:
        return False

data = pandas.read_csv("PKN.WA.csv")

on_close = data["Close"]

N_1 = 26
N_2 = 12
N_3 = 9

# ema_26_t = on_close.ewm(span=N_1).mean()
# ema_12_t = on_close.ewm(span=N_2).mean()

# macd_t = ema_12_t - ema_26_t
# signal_t = macd_t.ewm(span=N_3).mean()

ema_26 = pandas.Series(ema(N_1, on_close))
ema_12 = pandas.Series(ema(N_2, on_close))

macd = ema_12 - ema_26
signal = ema(N_3, macd)

# plt.plot(macd_t)
# plt.plot(macd)
# plt.plot(signal_t, color='purple')
# plt.plot(signal, color='red')
# plt.show()

# Algorytm kupujacy/sprzedajacy z samego MACD

capital = 1000
stocks = 0

for i in range(1, len(on_close)):
    if isBuyingPoint(macd[i - 1], signal[i - 1], macd[i], signal[i]):
        price = on_close[i]
        howMany = capital // on_close[i]
        capital -= howMany * price
        stocks += howMany
    elif isSellingPoint(macd[i - 1], signal[i - 1], macd[i], signal[i]):
        price = on_close[i]
        capital += stocks * on_close[i]
        stocks = 0

print('ORLEN:')
print('Pure MACD:')
print(f'Capital and stocks without selling, on the last day: capital - {capital}, stocks - {stocks}')
capital += stocks * on_close[len(on_close) - 1]
print(f'Capital after selling everything on the last day: {capital}')

# Algorytm korzystajacy rowniez z RSI

rsi = pta.rsi(on_close, length = 14)

capital = 1000
stocks = 0

for i in range(1, len(on_close)):
    if isBuyingPoint(macd[i - 1], signal[i - 1], macd[i], signal[i]):
        if rsi[i] >= 30:
            price = on_close[i]
            howMany = capital // on_close[i]
            capital -= howMany * price
            stocks += howMany
    elif isSellingPoint(macd[i - 1], signal[i - 1], macd[i], signal[i]):
        if rsi[i] <= 70:
            price = on_close[i]
            capital += stocks * on_close[i]
            stocks = 0

print('MACD with RSI:')
print(f'Capital and stocks without selling, on the last day, using RSI: capital - {capital}, stocks - {stocks}')
capital += stocks * on_close[len(on_close) - 1]
print(f'Capital after selling everything on the last day, using RSI: {capital}')

# Wykres 1. - same akcje

fig1, ax_1 = plt.subplots()
ax_1.plot(data['Date'], on_close)

ax_1.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
ax_1.xaxis.set_minor_locator(mdates.MonthLocator())
ax_1.yaxis.set_minor_locator(MultipleLocator(25))
ax_1.grid(which='both')

ax_1.set_ylabel('Wartość akcji [PLN]')
ax_1.set_xlabel('Data')
ax_1.set_title('Wykres akcji CDP Red')

fig1.set_figheight(8)
fig1.set_figwidth(16)
fig1.savefig('wykresy\\1_akcje', bbox_inches='tight')

# Wykres 2. - sam wskaźnik

fig2, ax_2 = plt.subplots()
ax_2.plot(data['Date'], macd, color='purple', label='MACD')
ax_2.plot(data['Date'], signal, color='orange', label='Signal')

ax_2.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
ax_2.xaxis.set_minor_locator(mdates.MonthLocator())
ax_2.yaxis.set_minor_locator(MultipleLocator(5))
ax_2.grid(which='both')

ax_2.set_xlabel('Data')
ax_2.set_ylabel('Wartość wskaźnika')
ax_2.set_title('Wykres wskaźnika MACD i Signal')
ax_2.legend()

fig2.set_figheight(8)
fig2.set_figwidth(16)
fig2.savefig('wykresy\\2_wskaznik', bbox_inches='tight')

# Wykres 3. - oddzielnie akcje i wskaźnik

fig3, ax_3 = plt.subplots(2, 1)

ax_3[0].plot(data['Date'], on_close)
ax_3[1].plot(data['Date'], macd, color='purple', label='MACD')
ax_3[1].plot(data['Date'], signal, color='orange', label='Signal')

ax_3[1].yaxis.set_minor_locator(MultipleLocator(5))

for ax in ax_3:
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.grid(which='both')
    ax.set_xlabel('Data')

ax_3[0].set_ylabel('Wartość akcji [PLN]')
ax_3[1].set_ylabel('Wartość wskaźnika')
ax_3[1].legend()

ax_3[0].set_title('Akcje i wskaźnik')

fig3.set_figheight(8)
fig3.set_figwidth(16)
fig3.savefig('wykresy\\3_akcje_wskaznik', bbox_inches='tight')

# Wykres 4. - akcje i wskaźnik nałożone

fig, ax1 = plt.subplots()
y1, = ax1.plot(data['Date'], on_close, linewidth=2, label='Akcje')

ax1.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
ax1.xaxis.set_minor_locator(mdates.MonthLocator())
ax1.yaxis.set_minor_locator(MultipleLocator(25))
ax1.grid(which='both')

ax1.set_ylabel('Wartość akcji [PLN]')
ax1.set_xlabel('Data')

ax2 = ax1.twinx()

y2, = ax2.plot(data['Date'], macd, color='purple', alpha=0.6, label='MACD')
y3, = ax2.plot(data['Date'], signal, color='orange', alpha=0.7, label='Signal')

ax2.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
ax2.xaxis.set_minor_locator(mdates.MonthLocator())

ax2.set_ylabel('Wartość wskaźnika')
ax1.set_title('Porównanie akcji i wskaźnika')
plt.legend(handles=[y1, y2, y3])

fig.set_figheight(8)
fig.set_figwidth(16)
fig.savefig('wykresy\\4_akcje_wskaznik_nal', bbox_inches='tight')

plt.show()