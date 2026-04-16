culinary_assistant-

AI Кулинарен Асистент: Какво има в хладилника?

Автор: Денис Неделчев

Обзор

Това е интелигентно уеб приложение, създадено с Flask и Google Gemini AI. Проектът анализира снимка на продукти и автоматично генерира персонализирани рецепти с хранителна стойност.

Основни функционалности

Автоматично разпознаване: Идентифицира продуктите от качена снимка чрез Gemini AI.

Генериране на рецепти: Създава инструкции за готвене на база наличните продукти.

Хранителна стойност: Изчислява приблизителни калории и макронутриенти.

Технологичен стек

Python 3.11+

Flask (Web Framework)

Google Generative AI SDK (google-genai)

Библиотеки: Pillow, python-dotenv

Структура на проекта

/static/uploads/ — съхранение на качените изображения.

/templates/index.html — потребителски интерфейс.

app.py — основна логика.

.env — за сигурно съхранение на API ключа (не се качва в GitHub).

Инсталиране и стартиране

Клониране:

git clone [https://github.com/DNedelchew/culinary_assistant.git](https://github.com/DNedelchew/culinary_assistant.git)
cd culinary_assistant


Виртуална среда:

python -m venv .venv
source .venv/bin/activate  # За Mac/Linux
# .venv\Scripts\activate   # За Windows


Инсталиране на пакети:

pip install flask google-genai pillow python-dotenv


Конфигурация на API

Създайте файл .env в главната папка и поставете ключа си вътре:

GEMINI_API_KEY=вашият_ключ_тук


Справяне с проблеми (Troubleshooting)

Грешка 429: Безплатният план на Google има лимити. Изчакайте 1 минута и опитайте отново.

Моделът не е намерен (404): Проектът ползва gemini-3-flash. Ако вашият ключ не го поддържа, сменете модела в app.py на gemini-1.5-flash.