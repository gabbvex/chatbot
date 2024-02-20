from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
import openai

# Configure sua chave API da OpenAI (deve ser configurada como uma variável de ambiente)
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_gpt3_response(prompt_text):
    try:
        response = openai.Completion.create(
          engine="text-davinci-003", # ou "davinci" dependendo da disponibilidade
          prompt=prompt_text,
          temperature=0.7,
          max_tokens=150,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Erro ao chamar a API GPT-3: {e}")
        return "Desculpe, ocorreu um erro ao gerar uma resposta."

def chatbot_view(request):
    user_input = request.params.get('q', 'Olá')
    chat_response = get_gpt3_response(user_input)
    return Response(chat_response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    with Configurator() as config:
        config.add_route('chat', '/chat')
        config.add_view(chatbot_view, route_name='chat')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
