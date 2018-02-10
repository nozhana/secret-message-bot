# IMPORT

from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, MessageHandler, Filters

# INITIALIZATION

updater = Updater(token='501645217:AAGQ_sX_zD4IKwj-kOLnBQSdTXV2uPOGOuY')
dispatcher = updater.dispatcher

# FUNCTIONS

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Write your message to Nozhan.')

def send(bot, update):
    fullname = update.message.from_user.first_name+' '+update.message.from_user.last_name
    username = '@'+update.message.from_user.username
    bot.send_message(chat_id = 266661234,
        text='Message from {} ({}):\n\n'.format(fullname, username) + update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text='Message sent.')

# def id(bot, update):
#     bot.send_message(chat_id=update.message.chat_id,
#         text='```'+str(update.message.chat_id)+'```', parse_mode='Markdown')

# HANDLERS

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, send))
# dispatcher.add_handler(CommandHandler('id', id))

# DEPLOY

updater.start_polling(poll_interval=0.5)
