import time
import datetime

from pyrogram import Client

import config
import util


app = Client(
	session_name=config.SESSION_NAME,
	api_id=config.API_ID,
	api_hash=config.API_HASH,
)


def main():
	while True:
		now = datetime.datetime.now()

		# Каждый ПН в 00:10
		if now.weekday == 0 and now.hour == 0 and now.minute == 10:
			url = util.generate_telegraph_page_week_report()
			
			with app:
				app.send_message(config.PNZA_COA_CHAT_ID, url)

		time.sleep(1 * 60)


if __name__ == '__main__':
	main()
