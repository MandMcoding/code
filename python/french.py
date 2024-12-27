import random
pronom = ["J", "Tu", "Il", "Elle", "On", "Nous", "Vous", "Ils", "Elles"]
avoir = {
	pronom[0]: "'ai ",
	pronom[1]: " as ",
	pronom[2]: " a ",
	pronom[3]: " a ",
	pronom[4]: " a ",
	pronom[5]: " avons ",
	pronom[6]: " avez ",
	pronom[7]: " ont ",
	pronom[8]: " ont "
}
verbes = ["faire", "avoir", "boire", "lire", "voir"]
participePasse = ["fait", "lu", "bu", "vu", "eu"]
verbConnection = {
	verbes[0]: participePasse[0],
	verbes[1]: participePasse[-1],
	verbes[2]: participePasse[2],
	verbes[3]: participePasse[1],
	verbes[4]: participePasse[3],
}

print("French practice for Participe Passe.\nTo stop the program type 1.")
while True:
	choice = ""
	if choice == "":
		print("")
	qPronom = random.choice(pronom)
	qVerb = random.choice(verbes)
	if qPronom == pronom[0]:
		print(qPronom + "e " + qVerb + "\n")
	else:
		print(qPronom + " " + qVerb + "\n")
	answer = input("")
	correctAnswer =  qPronom + avoir[qPronom] + verbConnection[qVerb]
	try:
		if int(answer) == 1:
			break
		
	except:
		if answer == correctAnswer:
			print("Correct!\n")
		elif awnser == "change":
			choice = ""
		else:
			print("Nice try!\nCorrection: " + correctAnswer +"\n")
