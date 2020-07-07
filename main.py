#Chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import os
from datetime import datetime

bot = ChatBot(
  'Lisa',
  storage_adapter='chatterbot.storage.SQLStorageAdapter'
)

#Dictionary of commands
dict_cmds = {}

#Load the dictionary of commands
def load_cmds():
  lines = open('chats/commands.txt', 'r').readlines()

  for line in lines:
    line = line.replace('\n', '')
    parts = line.split('|')
    dict_cmds.update({ parts[0] : parts[1] })

#Evaluate the command
def evaluate(command):
  result = None
  try:
    result = dict_cmds[command]
  except:
    result = None
  return result

#Running the command ===> Reunir com André para melhor definição de como deverá ser feito isso
def run_command(command_type):
  result = None
  now = datetime.now()
  if command_type == 'askid':
    result = str(now.hour) + ' hrs e ' + str(now.minute) + ' min'
  elif command_type == 'askname':
    result = 'Hoje é ' + str(now.day)
  return result

load_cmds()
trainer = ListTrainer(bot)

for file in os.listdir('chats'):
  chats = open('chats/' + file, 'r').readlines()
  trainer.train(chats)

for k, v in dict_cmds.items():
  print(k, ' ===> ', v)

while True:
  try:
    request = input('Digite um texto: ')
    # print('Bot: ' + str(bot.get_response(request)))

    print('Tipo de comandos: ', evaluate(request))
    response = run_command(evaluate(request))

    if response == None:
      response = bot.get_response(request)

    print(response)
  except(KeyboardInterrupt, EOFError, SystemExit):
    print('Não consigo te entender, poderia repetir por favor?')
    break
