import datetime

from pyrogram import Client
from pyrogram import filters

import database
import config
import util


app = Client(
	session_name=config.SESSION_NAME,
	api_id=config.API_ID,
	api_hash=config.API_HASH,
)


@app.on_message(filters.text)
def text_content_handler(client, message):

	# Получить отчет вручную
	if message.text == '/generate_report':
		url = util.generate_telegraph_page_week_report()
		message.reply_text(url)
		return

	# Проверка что сообщение из чата аналитиков
	if message.chat.id in config.ANALYST_JOB_CHAT_ID:
		# Проверка на ключевые слова в вакансии
		if 'пенз' in message.text.lower() or 'удален' in message.text.lower():
			# Добавить вакансию в базу
			vacancy = database.Vacancy(
				text=message.text,
				date_time=datetime.datetime.now(),
				message_id=message.message_id,
				chat_username=message.chat.username,
			)
			vacancy.save()
			return


if __name__ == '__main__':
	app.run()
