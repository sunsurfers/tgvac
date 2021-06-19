import datetime

from telegraph import Telegraph

import database


def generate_telegraph_page_week_report():
	"""
	Составить отчет за неделю по вакансиям
	"""

	telegraph = Telegraph()
	telegraph.create_account(short_name='Pnzcoa Helper')

	now = datetime.datetime.now()
	last_week = now - datetime.timedelta(days=7)

	title = 'Вакансии для ИТ-аналитиков за период с {} по {}'.format(
		last_week.strftime('%d.%m.%Y'), now.strftime('%d.%m.%Y')
	)
	html_content = ''

	vacancies = database.Vacancy.select().where(database.Vacancy.date_time >= last_week)
	for vacancy in vacancies:
		short_text= '\n'.join(vacancy.text.split('\n')[:7])
		url = 'https://t.me/{}/{}'.format(vacancy.chat_username, vacancy.message_id)
		html_content += '<a href="{}"><p>{}</p></a><hr>'.format(
			url, short_text.replace('\n', '<br>')
		)

	if not len(html_content):
		html_content = 'Пока нет подходящий вакансий'

	response = telegraph.create_page(title, html_content=html_content)

	return 'https://telegra.ph/{}'.format(response['path'])


# print(generate_telegraph_page_week_report())
