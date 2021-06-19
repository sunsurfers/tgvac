from peewee import *

import config


db = SqliteDatabase(config.DATABASE_PATH, thread_safe=True)


class BaseModel(Model):

	class Meta:
		database = db


class Vacancy(BaseModel):
	"""
	Вакансии из чата аналитиков
	"""

	text = TextField()
	date_time = DateTimeField()
	message_id = IntegerField()
	chat_username = TextField()


db.connect()
db.create_tables([Vacancy,])


# ALTER TABLE Vacancy ADD COLUMN chat_username text;
# UPDATE Vacancy SET chat_username="analyst_job";
