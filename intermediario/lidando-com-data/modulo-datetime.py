import datetime as dt

# Introdução
data1 = dt.date(2024, 7, 11)
print('Dia', data1)
print('Hora atual:', dt.datetime.now())

data2 = dt.datetime(2024, 7, 11, 9, 10)
print('Dia com hora:', data2)

# timedelta
print('Daqui uma semana:', data2 + dt.timedelta(weeks=1))
print('Daqui 3 horas e 45 minutos:', data2 + dt.timedelta(hours=3, minutes=45))
print('Daqui 3 horas e 45 minutos:', data2 + dt.timedelta(minutes=225))
print('25 dias atrás:', data1 - dt.timedelta(days=25))