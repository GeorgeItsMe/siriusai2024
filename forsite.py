from flask import Flask, request, render_template, jsonify
from bs4 import BeautifulSoup
import requests
from gigachat import GigaChat


app = Flask(__name__)

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

api_key = 'ZDIxNzE5YTgtNGE3My00Y2RmLTg2MDAtYTg0NDEwZWY0YWFiOmFmMWQxNTBjLTIxMzQtNDAxOC1hM2YwLWJkZWUzYjQ5OWI5Ng=='

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-description', methods=['POST'])
def generate_description():
    # Получаем данные из формы
    url = request.form['url']
    hotel_name = request.form['hotel_name']
    hotel_address = request.form['hotel_address']
    message = request.form['message']

    # Получаем информацию о отеле
    hotel_info = parse_hotel_info(url)
    prev_description = hotel_info['description']
    hotel_tools = hotel_info['services']

    # Генерация подсказки для GigaChat
    prompt = f'''
    Сгенерируй красивое описание отеля на основе этих данных:
    пожелания отельера: {message},
    hotel_name: {hotel_name},
    hotel_address: {hotel_address},
    prev_description: {prev_description} (Можно на него опираться не нельзя полностью копировать),
    hotel_tools: {hotel_tools} (Услуги отеля, возми самые важные и красиво перечисли их)
    Не нужно додумывать факты об отеле, сформеруй на основе данных лакончиное и красивое описание 
    '''

    # Обращение к GigaChat API
    with GigaChat(credentials=api_key, verify_ssl_certs=False) as giga:
        response = giga.chat(prompt)
        out = response.choices[0].message.content

    # Формируем список услуг
    formatted_services = "<ul>"
    for service in hotel_tools:
        formatted_services += f"<li>{service}</li>"
    formatted_services += "</ul>"

    # Отправляем результат обратно на страницу
    return render_template('index.html', description=out, services=formatted_services)

if __name__ == '__main__':
    app.run(debug=True)
