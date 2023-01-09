from django.db import models as m

import datetime as dt

class datauser(m.Model):
    name = m.CharField(max_length=30)
    lastn = m.CharField(max_length=30)
    password = m.CharField(max_length=40)
    phone = m.CharField(max_length=60)
    date = m.DateTimeField()

class plan(m.Model):
    plan = m.CharField(max_length=20)
    price = m.DecimalField(max_digits=30,decimal_places=2)
    description = m.CharField(max_length=100)



