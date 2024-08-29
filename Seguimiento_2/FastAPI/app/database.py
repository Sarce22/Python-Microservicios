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


class UserModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"


class BookModel(Model):
    id = AutoField(primary_key=True)
    isbn = IntegerField()
    title = CharField(max_length=50)
    author = CharField(max_length=50)
    genre = CharField(max_length=50)
    year_published = IntegerField()

    class Meta:
        database = database
        table_name = "books"


class CompanyModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    address = CharField(max_length=50)
    city = CharField(max_length=50)
    state = CharField(max_length=50)
    phone_number = CharField(max_length=50)
    email = CharField(max_length=50)
    website = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "companies"


class OrderModel(Model):
    id = AutoField(primary_key=True)
    user_id = IntegerField()
    product_id = IntegerField()
    quantity = IntegerField()
    total_price = FloatField()

    class Meta:
        database = database
        table_name = "orders"


class VideoGameModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    release_date = CharField(max_length=50)
    platform = CharField(max_length=50)
    genre = CharField(max_length=50)
    publisher = CharField(max_length=50)
    developer = CharField(max_length=50)
    user_score = FloatField()
    total_sales = FloatField()
    critic_count = IntegerField()
    

    class Meta:
        database = database
        table_name = "video_games"