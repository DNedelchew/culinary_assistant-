import os
import time
from flask import Flask, render_template, request
from google import genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    image_path = None

    if request.method == 'POST':
        file = request.files.get('image')

        user_prompt = request.form.get("prompt")

        base_prompt = """Разпознай продуктите и предложи рецепта."""

        if user_prompt:
            prompt = base_prompt + "\nДопълнително: " + user_prompt
        else:
            prompt = base_prompt

        if file and file.filename != "":
            image_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(image_path)

            img = Image.open(image_path)

           
            try:
                response = client.models.generate_content(
                    model="models/gemini-3-flash",
                    contents=[prompt, img]
                )
                result = response.text

            except Exception as e:
                print("Първи опит грешка:", e)
                time.sleep(2)

                try:
                    response = client.models.generate_content(
                       model="models/gemini-2.5-flash",
                        contents=[prompt, img]
                    )
                    result = response.text
                except Exception as e:
                    print("Втори опит грешка:", e)
                    result = "⚠️ Сървърът е натоварен. Опитай пак след малко."

        else:
            result = "Моля качи снимка!"

    return render_template('index.html', result=result, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)