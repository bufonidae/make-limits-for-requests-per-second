#Python 3

from time import time,sleep

#разрешено делать number_of_requests запросов в time_for_those_requests секунд
number_of_requests = 2#items
time_for_those_requests = 5#секунд

chat_id = 0#or IP or any unique useridentification
checklimit = {}#у каждого chat_id своя закладка в Жсоне, чтоб не путались.
stopreq = False#флаг остановки операции, если уперлись в лимит запросов
getrequest_For_User_chatid = True#для разового запуска в случае получения запроса

if getrequest_For_User_chatid:
	getrequest_For_User_chatid = False#для разового запуска в случае получения запроса

	while True:
		#счетчик запросов по аккаунту chat_id
		checklimit.setdefault(chat_id,[])
		checklimit[chat_id].append(time())#ставит время запроса. По каждому запросу по одной строке в конце спсика
		if len(checklimit[chat_id]) > number_of_requests:#если в памяти запросов больше чем дохволено, то и проверяем время первого из них
			firstreq = checklimit[chat_id][0]
			if time()-firstreq > time_for_those_requests:#лимит не превышен
				checklimit[chat_id].pop(0)#то удаляем время первого запроса из списка
			else:#лимит превышен
				checklimit[chat_id].pop()#то удаляем время последнего (текущего) запроса из списка
				print(chat_id,"Пожалуйста не более " + str(number_of_requests) + " запросов в " + str(time_for_those_requests) + " секунд")
				print(chat_id,"Уперся в лимит запросов")
				stopreq = True
		if stopreq:
			stopreq = False
			continue
		print("Выполняем стандартную операцицю, лимиты в норме")

	  	#make anu you code....
