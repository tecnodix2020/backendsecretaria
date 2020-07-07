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

reasons_meeting = ['reunião', 'entrevista']
reasons_order = ['entrega', 'encomenda']

#Performs the reason for the visit
def treats_reason_for_visit(reason):
  result = None
  if reason in reasons_meeting:
    id = input('Por favor, me informe o seu CPF para verificar as informações.\n')
    result = get_metting_data(id)
  elif reason in reasons_order:
    recipient = input('Qual o nome do destinatário?\n')
    result = get_order_data(recipient)
  return result

def get_metting_data(id):
  return 'O seu id é ' + str(id)
    
def get_order_data(recipient):
  return 'A sua entrega é para ' + str(recipient)

#Returns compliance according the hour
def period():
  now = datetime.now()
  print(now)
  if now.hour >= 6 and now.hour < 12:
    return 'Bom dia! '
  elif now.hour >= 12 and now.hour < 18:
    return 'Boa tarde! '
  elif now.hour >= 18 and now.hour <= 23:
    return 'Boa noite! '
  else:
    return ''

load_cmds()
trainer = ListTrainer(bot)

for file in os.listdir('chats'):
  chats = open('chats/' + file, 'r').readlines()
  trainer.train(chats)

for k, v in dict_cmds.items():
  print(k, ' ===> ', v)

print(period(), 'Você está na Landix Sistemas.')
while True:
  try:
    reason = input('Por favor me informe o motivo de sua visita para que possa auxiliá-lo.\n')

    request = treats_reason_for_visit(reason)

    if request == None:
      response = bot.get_response(request)
      print(response)
    else:
      print(request)
  except(KeyboardInterrupt, EOFError, SystemExit):
    print('Não consigo te entender, poderia repetir por favor?')
    break
