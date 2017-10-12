# -*- coding: utf-8 -*-

import socket #on importe la bibliotheque socket

ip = "192.168.0.202" #l'adresse ip associé à la variable ip
port = 5005 #le port associé à port
msg = "cinema" #le message envoyé : cinema

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(1.0) #le delai d'expiration

sock.connect((ip, port)) #la commande sock.connect importé de socket a besoin de
#l'ip et du port qu'on a mit enregistrer dans les variables ip et port
sock.send(msg) #sock.send est importé de socket, il envoie le contenue de la variable msg

trameReponse, addr = sock.recvfrom(1024) #on recupere la reponse ans une variable trameReponse, et
# l'adresse du server dans addr, on peut recevoir un maximun de 1024octet

print "Réception de la trame de réponse", trameReponse.encode("hex") #on affiche le contenue de la trame
#de reponse qui est encode en hexadecimal

b0= ord(trameReponse[3])<<24
b1= ord(trameReponse[2])<<16
b2= ord(trameReponse[1])<<8
b3= ord(trameReponse[0])
# il s'agit d'un decalage de bit

code = b0|b1|b2|b3
# on assemble les octets, qu'on enregistre dans la variable code

print code
#on affiche le code
