from flask import Flask, render_template, request, send_file
from openai import OpenAI
import tempfile
from pyngrok import ngrok

app = Flask(__name__)
ngrok_tunnel = ngrok.connect(6006)

def tts(text, model, voice, api_key):
    if api_key == '':
        raise ValueError('请输入你的 OpenAI API Key')
    else:
        try:
            client = OpenAI(api_key=api_key)

            response = client.audio.speech.create(
                model=model,
                voice=voice,
                input=text,
            )

        except Exception as error:
            raise ValueError("音频生成错误. 请检查你的 API key 以及网络配置 并再次尝试.")
            print(str(error))

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        temp_file.write(response.content)

    temp_file_path = temp_file.name

    return temp_file_path

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        model = request.form["model"]
        voice = request.form["voice"]
        api_key = request.form["api_key"]

        audio_file = tts(text, model, voice, api_key)

        return send_file(audio_file, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    print(" * Running on", ngrok_tunnel.public_url)
    app.run()
