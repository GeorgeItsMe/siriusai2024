from gigachat import GigaChat

message = 'Отель супер, только для випов, даже номера люкс есть 40кв метров' # сюда строку из поля ввода

with GigaChat(credentials='ZDIxNzE5YTgtNGE3My00Y2RmLTg2MDAtYTg0NDEwZWY0YWFiOmFmMWQxNTBjLTIxMzQtNDAxOC1hM2YwLWJkZWUzYjQ5OWI5Ng==', verify_ssl_certs=False) as giga:
    response = giga.chat(message + 'отредактируй описание которое тебе дали до, повысь читабельность')
    out = response.choices[0].message.content

print(out)