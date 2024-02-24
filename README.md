# OpenAI 文本转语音

这是一个使用 OpenAI 进行文本转语音的简单 Web 应用程序。您可以输入文本并选择语音模型以及音色，然后生成对应的语音输出。
 - 你可访问原作者的主页[huggingface](https://huggingface.co/ysharma)
我对其进行了修改，添加了Flask版本。

## 使用方法

1. 在输入框中输入您要转换的文本。
2. 输入您的 OpenAI API Key。
3. 选择语音模型和音色。
4. 点击 "文本转音频" 按钮生成语音。
5. 播放生成的语音输出。

## UI展示：

![Preview](https://raw.githubusercontent.com/Ccj0221/OpenAI_TTS/UI/gradio_ui.png?sanitize=true)

您也可以在以下链接创建实例：[codewithgpu](https://www.codewithgpu.com/u/J_0221)

## 在线体验

您可以直接访问在线演示，体验 OpenAI 文本转语音功能：
[OpenAI TTS Demo](https://huggingface.co/spaces/ysharma/OpenAI_TTS_New)

## 配置说明

1. 确保您拥有有效的 OpenAI API Key。
2. 如果你需要使用Flask，请访问 https://dashboard.ngrok.com/signup 创建一个 ngrok 账户，如果您已经有了账户，请登录。
- 登录后，您将看到您的 authtoken，它类似于 authtoken: YOUR_AUTH_TOKEN -
  -将这个 authtoken 复制下来，并在终端中运行以下命令，将 authtoken 添加到 pyngrok 中：
   -  ngrok authtoken YOUR_AUTH_TOKEN #“YOUR_AUTH_TOKEN”替换为你的authtoken，复制代码到右侧终端中
