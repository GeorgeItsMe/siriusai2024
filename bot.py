from bs4 import BeautifulSoup
import requests


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


url = 'https://travel.yandex.ru/hotels/moscow/otel-mandarin-moskva/'
hotel_info = parse_hotel_info(url)
print('Description:', hotel_info['description'])
print('Services:', hotel_info['services'])
