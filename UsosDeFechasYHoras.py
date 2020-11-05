import datetime

#30 de Abril del 2019
date = datetime.date(2019,4,30)

#Atributo año de la fecha
date.year

#Atributo mes de la fecha
date.month

#Atributo dia de la fecha
date.day

#Devuelve el día de la semana. El lunes es el cero y el domingo es el 6
date.weekday()
#Devuelve el día de la semana. El lunes es el uno y el domingo es el 7
date.isoweekday()
#Devuelve la fecha como un string con el formato 'YYYY-MM-DD'
date.isoformat()

#Fecha máxima
date_max = datetime.date.max

#Datetime objects
#El día 10 de Octubre de 2019 a las 9:15:30
date_and_time = datetime.datetime(2019,10,10,9,15,30)

#Atributo año de la fecha y hora
date_and_time.year
#Atributo mes de la fecha y hora
date_and_time.month
#Atributo dia de la fecha y hora
date_and_time.day
#Atributo hora de la fecha y hora
date_and_time.hour
#Atributo minuto de la fecha y hora
date_and_time.minute
#Atributo segundo de la fecha y hora
date_and_time.second
#Atributo microsegundo de la fecha y hora
date_and_time.microsecond

#Obtengo un objeto date a partir del objeto datetime
date_and_time.date()

#La fecha y hora actual (local)
now = datetime.datetime.now()

#La fecha y hora actual en UTC (Coordinated Universal Time)
now = datetime.datetime.utcnow()

#Time Objects
#La hora 10:20:35
time = datetime.time(10,20,35)
#Atributo hora de la hora
time.hour
#Atributo minuto de la hora
time.minute
#Atributo segundo de la hora
time.second
#Atributo microsegundo de la hora
time.microsecond
