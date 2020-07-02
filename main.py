#Chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import os

bot = ChatBot(
  'Lisa',
  storage_adapter='chatterbot.storage.SQLStorageAdapter'
)

trainer = ListTrainer(bot)

for file in os.listdir('chats'):
  chats = open('chats/' + file, 'r').readlines()
  trainer.train(chats)

while True:
  request = input('Digite um texto: ')
  print('Bot: ' + str(bot.get_response(request)))