from flask import Flask, request, render_template, jsonify
from bs4 import BeautifulSoup
import requests
from gigachat import GigaChat

app = Flask(__name__)


# Функция для парсинга информации об отеле
def parse_hotel_info(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    description_tag = soup.find('h2', text='Про отель')
    description = ''
    if description_tag:
        description_container = description_tag.find_next_sibling('div')
        if description_container:
            description_paragraphs = description_container.find_all('p')
            description = ' '.join(p.get_text(strip=True) for p in description_paragraphs)

    services = []
    if description:
        services_tags = description_container.find_all('p')
        for service_tag in services_tags:
            text = service_tag.get_text(strip=True)
            if 'к вашим услугам' in text.lower():
                services_list = text.split(':')[-1]
                services = [s.strip() for s in services_list.split(',')]
                break

    return {
        'description': description,
        'services': services
    }


# Функция для создания описания и вывода услуг
def create_description(url: str, hotel_name: str, hotel_address: str, message: str) -> str:
    api_key = 'ZDIxNzE5YTgtNGE3My00Y2RmLTg2MDAtYTg0NDEwZWY0YWFiOmFmMWQxNTBjLTIxMzQtNDAxOC1hM2YwLWJkZWUzYjQ5OWI5Ng=='
    hotel_info = parse_hotel_info(url)

    prev_description = hotel_info['description']
    hotel_tools = hotel_info['services']

    # Генерация описания отеля
    prompt_description = f'''
    Сгенерируй красивое описание отеля на основе этих данных:
    пожелания отельера: {message},
    hotel_name: {hotel_name},
    hotel_address: {hotel_address},
    prev_description: {prev_description} (Можно на него опираться не нельзя полностью копировать),
    hotel_tools: {hotel_tools} (Услуги отеля, возьми самые важные и красиво перечисли их)
    Не нужно додумывать факты об отеле, сформеруй на основе данных лаконичное и красивое описание
    '''

    # Генерация списка услуг
    prompt_tools = f'''
    Красиво оформи услуги исходя из основного описания
    hotel_tools: {prev_description} (Услуги отеля)
    Не нужно додумывать факты об отеле
    Напиши короткое, красивое и лаконичное название каждой услуги
    В выводе должны быть лишь услуги, не пиши лишних слов приветствия
    '''

    with GigaChat(credentials=api_key, verify_ssl_certs=False) as giga:
        # Получение описания
        response = giga.chat(prompt_description)
        description = response.choices[0].message.content

        # Получение списка услуг
        response = giga.chat(prompt_tools)
        tools = response.choices[0].message.content

    return description, tools


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        url = request.form['url']
        hotel_name = request.form['hotel_name']
        hotel_address = request.form['hotel_address']
        message = request.form['message']

        # Получаем описание отеля и список услуг
        description, tools = create_description(url, hotel_name, hotel_address, message)

        # Отправляем данные в шаблон
        return render_template('index.html', description=description, tools=tools)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
