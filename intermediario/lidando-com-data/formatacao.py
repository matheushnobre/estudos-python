import datetime as dt
import locale

d = dt.datetime.now()

# Formatandodata e hora
mask = "%d/%m/%Y %H:%M"
str_data = d.strftime(mask)
print(str_data) 

# Imprimindo com textinho
locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
print(d.strftime("%d de %B de %Y, às %H horas e %M minutos")) 

# Convertendo uma string para data
dt_data = dt.datetime.strptime(str_data, mask)
print(dt_data)