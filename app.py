from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging
from datetime import datetime
from chatbot import TuristickiChatbot
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from hrvatski_turistickiLexer import hrvatski_turistickiLexer
from hrvatski_turistickiParser import hrvatski_turistickiParser

logging.basicConfig(
    filename=f'chatbot_{datetime.now().strftime("%Y%m%d")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Jedna globalna instanca ili više, ovisno o potrebama:
chatbot_instance = TuristickiChatbot()

def pokreni_chatbot(query, chatbot):
    input_stream = InputStream(query.lower())
    lexer = hrvatski_turistickiLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = hrvatski_turistickiParser(token_stream)
    tree = parser.razgovor()
    chatbot.trenutni_odgovor = None
    walker = ParseTreeWalker()
    walker.walk(chatbot, tree)
    return chatbot.trenutni_odgovor or "Oprostite, nisam razumio pitanje. Možete li preformulirati?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def process_query():
    data = request.json
    query = data.get('query', '').strip()

    if not query:
        return jsonify({'response': 'Molim vas unesite pitanje.'})

    if query.lower() == 'dovidenja':
        return jsonify({'response': 'Doviđenja! Hvala na razgovoru!'})

    try:
        odgovor = pokreni_chatbot(query, chatbot_instance)
        return jsonify({'response': odgovor})
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({'response': 'Došlo je do greške u obradi vašeg upita.'})

if __name__ == '__main__':
    app.run(debug=True)