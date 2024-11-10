# Дополнительная задача и MVP основного продукта для программы Сириус ИИ

**Проект: Классификатор рейтинга отеля на основе отзывов (МТС x ФКН ВШЭ)**  
Этот проект разработан с целью автоматической классификации рейтингов отелей на основе текстовых отзывов пользователей. С помощью моделей машинного обучения и современных техник обработки естественного языка (NLP), мы можем предсказать оценку отеля, основываясь на тексте отзывов, что позволяет улучшить процесс анализа и рекомендаций для пользователей.

## Структура проекта классификатора рейтинга отеля:

- **MTC_reviews_parser.py**  
  Скрипт для парсинга данных из отзывов, которые используются для обучения моделей. Он извлекает и обрабатывает отзывы с различных онлайн-ресурсов, создавая файл с данными для дальнейшего анализа.

- **mtc_reviews_EDA.ipynb**  
  Ноутбук для начального анализа данных (EDA), в котором исследуются отзывы и их структура. Здесь мы анализируем и визуализируем распределение рейтингов, длину отзывов и другие важные метрики.

- **mtc_reviews_embs.ipynb**  
  Ноутбук, в котором создаются эмбеддинги для отзывов с использованием моделей для обработки текста. Эмбеддинги позволяют преобразовать текст в числовые представления, что облегчает работу с текстовыми данными в задачах классификации.

- **feedback_classification.ipynb**  
  Основной ноутбук с эксперементами над моделями машинного обучения для классификации отзывов и предсказания рейтинга отеля. Включает выбор и оценку различных моделей, таких как логистическая регрессия, случайный лес и градиентный бустинг.

- **all_reviews.csv**  
  Данные, полученные из парсера, содержащие все отзывы и связанные с ними метаданные. Этот файл является основным источником данных для обучения моделей.

- **df_embs.csv**  
  Данные с эмбеддингами отзывов. Этот файл содержит числовые представления текстов отзывов, полученные после обработки с использованием техники эмбеддинга.

- **tfidf_try.py**  
  Дополнительный скрипт, который использует метод TF-IDF (Term Frequency-Inverse Document Frequency) для классификации текстов. Этот подход помогает оценить важность каждого слова в тексте и может быть использован в качестве основы для машинного обучения.

## Основные возможности:

1. **Анализ и классификация отзывов**: Система анализирует текстовые отзывы пользователей и классифицирует их, предсказывая рейтинг отеля (например, от 1 до 5).
2. **Обработка отзывов с помощью NLP**: Используются различные методы, включая эмбеддинги и TF-IDF, для преобразования текстов в числовые данные, что помогает улучшить точность классификации.
3. **Интерфейс для генерации описания отелей**: Веб-приложение позволяет владельцам отелей генерировать красивые и информативные описания на основе отзывов и дополнительных пожеланий.
4. **Отчеты и визуализация**: В рамках анализа данных создаются подробные отчеты и визуализации, помогающие понять, как отзывы влияют на общий рейтинг отелей.


**Проект: Генератор описания отеля на основе данных заполненых отельером (МТС x ФКН ВШЭ)**  
Этот проект разработан с целью помочь отельеру в заполнении описания отеля. Описание отеля генерируется на основе спаршенных и заполненных отельером данных. В качестве LLM для генерации итогового описания используется
vikhr

**Данные об отеле с которыми работает pipline:**
* Фотографии отеля
* Геоданные
* Отзывы об отеле (при наличии)
* Информация с сайтов на которых отель уже размещался (при наличии)
* Информация с сайта заполняемая отельером (Название, адрес, и т.д)

## Структура проекта генерации описания отеля:
- **parsing.py**  
  Парсер, который извлекает описания отелей для основного приложения. Он помогает собрать дополнительные данные, которые могут быть полезны для создания более точных рекомендаций.

- **forsite.py**  
  Основной сайт, написанный на Flask (Minimal Viable Product - MVP). Это веб-приложение позволяет пользователям загружать данные о отеле, генерировать описание и получать рейтинг отеля на основе отзывов.

- **index.html**  
  HTML и CSS для сайта, обеспечивающие пользовательский интерфейс. Этот файл отвечает за внешний вид и функциональность страницы, где пользователи могут взаимодействовать с веб-приложением.

> Проект находится на стадии MVP, в коде проекта могут быть использованы другие модели, нежели заявленные в итоговом решении. С идеей итогового решения можете ознакомиться в презентации

## Установка и использование проекта для генерации описания отеля

### Требования:
- Python 3.7+
- Flask для веб-приложения
- Библиотеки для работы с данными и моделями (pandas, scikit-learn, numpy, etc.)
  
### Установка:

1. Перейдите в директорию проекта:
   ```bash
   git clone https://github.com/GeorgeItsMe/siriusai2024.git
2. Клонируйте репозиторий:
   ```
   cd siriusai2024

3. Установите зависимости:
   ```
   pip install -r requirements.txt

4. Запустите веб-приложение:
   ```
   python forsite.py

Этот проект лицензирован под MIT License.
