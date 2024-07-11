import datetime as dt
import pytz

mask = "%d/%m/%Y - %H:%M:%S"
d = dt.datetime.now(pytz.timezone("America/Manaus"))
print('Horário em Parintins:', d.strftime(mask))

# Que horas são em Tóquio?
d = dt.datetime.now(pytz.timezone("Asia/Tokyo"))
print('Horário em Tóquio:', d.strftime(mask))

# Boa prática: armazenar datas em UTC
d = dt.datetime.now(pytz.timezone('utc'))
print('Horário UTC:', d.strftime(mask))