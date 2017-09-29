#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/python-telegram-bot/

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from functools import wraps

LIST_OF_ADMINS = [] # List of admins who can start/stop the bot
TOKEN = '' # Your bot's token
updater = Updater(token = TOKEN)
j = updater.job_queue
dispatcher = updater.dispatcher

# Start
def start(bot, update):
    if update.effective_user.id in LIST_OF_ADMINS:
        bot.send_message(chat_id=update.message.chat_id, text='Os voy a rayar hasta que me pagueis.') # Message to send
        job = j.run_repeating(callback_minute, interval=3600, first=3600, context=update.message.chat_id) # Interval of time, first message 3600 seconds after the command
    else:
        bot.send_message(chat_id=update.message.chat_id, text='No tienes acceso mindundi.') # Message to send if a non admin tries to start the bot

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Stop
def stop(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Ya paro coño.')
    j.stop()

stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)

# Message to send when scheduled
def callback_minute(bot, job):
    bot.send_message(chat_id=job.context, text='Pagadme ya putos morosos.')

# To keep the bot running
updater.start_polling()