from dotenv import load_dotenv
from peewee import *

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

# Create User Model
class UserModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"


# Create Car Model
class CarModel(Model):
    id = AutoField(primary_key=True)
    brand = CharField(max_length=50)
    model = CharField(max_length=50)
    year = IntegerField()
    color = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "cars"


# Create Phone Model
class PhoneModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    color = CharField(max_length=50)
    year = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "phones"


# Create Bike Model
class BikeModel(Model):
    id = AutoField(primary_key=True)
    brand = CharField(max_length=50)
    model = CharField(max_length=50)
    year = IntegerField()
    color = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "bikes"


#Create Computer Model
class ComputerModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)
    ram = IntegerField()
    cpu = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "computers"