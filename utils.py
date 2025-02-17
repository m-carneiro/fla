import logging
import datetime
import os


def create_html_file(file_name, value):
    with open(file_name + '.html', "w", encoding="utf-8") as f:
        f.write(value)


def date_handler(date: str) -> str | None:
    date = date.replace(' ', '')

    try:
        if date == 'hoje' or date == 'ontem' or date == 'amanhã':
            return date
        trimmed = date.split(',')
        current_year = datetime.date.today().year

        date = f"{trimmed[1]}/{current_year}"
        return date
    except Exception as e:
        logging.log(1, f'{e} - date_handler')


def create_txt_file(file_name: str, value: any):
    file = open(file_name + '.json', '+a')
    file.write(value)
    file.close()


def delete_all_files():
    home_path = os.getcwd()
    files = os.listdir(home_path)

    for item in files:
        if item == 'matches.json' or item.endswith('.html'):
            os.remove(home_path + '/' + item)
