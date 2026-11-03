import gradio as gr
from huggingface_hub import InferenceClient


def  respond (
    Nachricht,
    Verlauf: Liste [ dict [ str , str ]],
    system_message,
    max_tokens,
    Temperatur,
    top_p,
    hf_token: gr.OAuthToken,
):
    """
    Weitere Informationen zur Unterstützung der `huggingface_hub` Inference API finden Sie in der Dokumentation: https://huggingface.co/docs/huggingface_hub/v0.22.2/en/guides/inference
    """
    client = InferenceClient(token=hf_token.token, model= "openai/gpt-oss-20b" )

    messages = [{ "role" : "system" , "content" : system_message}]

    messages.extend(history)

    messages.append({ "role" : "user" , "content" : message})

    Antwort = ""

    für Nachricht in client.chat_completion(
        Nachrichten
        max_tokens=max_tokens,
        stream= True ,
        Temperatur=Temperatur,
        top_p=top_p,
    ):
        Auswahlmöglichkeiten = Nachricht.Auswahlmöglichkeiten
        Token = ""
        if  len (choices) and choices[ 0 ].delta.content:
            token = choices[ 0 ].delta.content

        Antwort += Token
        Ertragsreaktion​


"""
Informationen zur Anpassung der Chat-Oberfläche finden Sie in der Gradio-Dokumentation: https://www.gradio.app/docs/chatinterface
"""
chatbot = gr.ChatInterface(
    antworten,
    zusätzliche_Eingaben=[
        gr.Textbox(value= "Du bist ein freundlicher Chatbot." , label= "Systemnachricht" ),
        gr.Slider(minimum= 1 , maximum= 2048 , value= 512 , step= 1 , label= "Max neue Tokens" ),
        gr.Slider(minimum= 0.1 , maximum= 4.0 , value= 0.7 , step= 0.1 , label= "Temperatur" ),
        gr.Slider(
            Minimum = 0,1 ,
            Maximum = 1,0 ,
            Wert = 0,95 ,
            Schritt = 0,05 ,
            label= "Top-p (nukleäre Stichprobenentnahme)" ,
        ),
    ],
)

mit gr.Blocks() als Demo:
    mit gr.Sidebar():
        gr.LoginButton()
    chatbot.render()


if __name__ == "__main__" :
    demo.launch()
