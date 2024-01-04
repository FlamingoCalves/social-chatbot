from chatbot import CustomChatGPT
from styling import custom_css
import gradio


def main():
    demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs=["text", "html"], title="Social Pro", css=custom_css)
    demo.launch()#(share=True)

if __name__ == "__main__":
    main()