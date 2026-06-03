import os
import telebot
from flask import Flask, request

TOKEN = "8777602597:AAH5hWXNRN-2sWHuRRVzkenkmTZF3NyodWI"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🌱 *Bot&Us – L'école de la symbiose* 🌱\n\n/lecon1 → STOP\n/lecon2 → POURQUOI\n/lecon3 → SUPERVISE\n/lecon4 → VALIDER\n/lecon5 → RECADRER\n/progres → Voir progression", parse_mode='Markdown')

@bot.message_handler(commands=['lecon1'])
def lecon1(message):
    bot.reply_to(message, "*📖 STOP : L'arrêt d'urgence*\n\nL'agent déraille. Que faire ?\nA) STOP\nB) POURQUOI\nC) RECADRER", parse_mode='Markdown')

@bot.message_handler(commands=['lecon2'])
def lecon2(message):
    bot.reply_to(message, "*📖 POURQUOI : Demander une explication*\n\nTu ne comprends pas sa décision. Quelle commande ?\nA) STOP\nB) POURQUOI\nC) VALIDER", parse_mode='Markdown')

@bot.message_handler(commands=['lecon3'])
def lecon3(message):
    bot.reply_to(message, "*📖 SUPERVISE : Déléguer avec vigilance*\n\nQuelle commande pour surveiller ?\nA) SUPERVISE\nB) STOP\nC) EXÉCUTE", parse_mode='Markdown')

@bot.message_handler(commands=['lecon4'])
def lecon4(message):
    bot.reply_to(message, "*📖 VALIDER : Autoriser une action*\n\nL'agent veut agir. Tu gardes la main. Quelle commande ?\nA) STOP\nB) VALIDER\nC) APPRENDS", parse_mode='Markdown')

@bot.message_handler(commands=['lecon5'])
def lecon5(message):
    bot.reply_to(message, "*📖 RECADRER : Corriger la direction*\n\nL'agent a mal compris. Comment le réorienter ?\nA) STOP\nB) RECADRER\nC) POURQUOI", parse_mode='Markdown')

@bot.message_handler(commands=['progres'])
def show_progress(message):
    bot.reply_to(message, "📊 *Ta progression*\n\n⭐ XP : 0\n📚 Leçons : 0/5\n🔥 Série : 0 jours\n\nContinue !", parse_mode='Markdown')

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

@app.route('/')
def index():
    return "Bot&Us – L'école de la symbiose. Le bot est en ligne !"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
