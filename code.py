from time import time,sleep

#разрешено делать number_of_requests запросов в time_for_those_requests секунд
number_of_requests = 2#items
time_for_those_requests = 5#секунд

chat_id = 0#or IP or any unique useridentification
checklimit = {}#у каждого chat_id своя закладка в Жсоне, чтоб не путались.
stopreq = False#флаг остановки операции, если уперлись в лимит запросов
		
while True:
  #счетчик запросов по аккаунту
  checklimit.setdefault(chat_id,[])
  checklimit[chat_id].append(time())
  if len(checklimit[chat_id]) > number_of_requests:
    firstreq = checklimit[chat_id][0]
    if time()-firstreq > time_for_those_requests:#лимит не превышен
      checklimit[chat_id].pop(0)
    else:#лимит превышен
      checklimit[chat_id].pop()
      print(chat_id,"Пожалуйста не более " + str(number_of_requests) + " запросов в " + str(time_for_those_requests) + " секунд")
      print(chat_id,"Уперся в лимит запросов")
      stopreq = True
  if stopreq:
    stopreq = False
    continue
    
  #make anu you code....
