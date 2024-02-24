import gradio as gr
import os
import tempfile
from openai import OpenAI


def tts(text, model, voice, api_key):
    if api_key == '':
        raise gr.Error('请输入你的 OpenAI API Key')
    else:
        try:
            client = OpenAI(api_key=api_key)

            response = client.audio.speech.create(
                model=model, # "tts-1","tts-1-hd"
                voice=voice, # 'alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'
                input=text,
            )

        except Exception as error:
            raise gr.Error("音频生成错误. 请检查你的 API key 并再次尝试.")
            print(str(error))

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        temp_file.write(response.content)

    temp_file_path = temp_file.name

    return temp_file_path


with gr.Blocks() as demo:
    gr.Markdown("# <center> OpenAI 文本转语音 接口  </center>")
    with gr.Row(variant='panel'):
      api_key = gr.Textbox(type='password', label='OpenAI API Key', placeholder='请输入你的API Key')
      model = gr.Dropdown(choices=['tts-1','tts-1-hd'], label='Model', value='tts-1')
      voice = gr.Dropdown(choices=['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'], label='音色', value='alloy')

    text = gr.Textbox(label="输入文本", placeholder="请输入你要转换的文本，如果转换失败，请检查你的 API key)
    btn = gr.Button("文本转音频")
    output_audio = gr.Audio(label="输出结果")
    
    text.submit(fn=tts, inputs=[text, model, voice, api_key], outputs=output_audio, api_name="tts_enter_key", concurrency_limit=None)
    btn.click(fn=tts, inputs=[text, model, voice, api_key], outputs=output_audio, api_name="tts_button", concurrency_limit=None)

demo.launch(share=True)
