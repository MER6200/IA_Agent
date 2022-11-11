
#Admin_1
import time
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template


class Admin_1(Agent):
    # Définition des variables à utiliser pour le calcul des sommes et moyennes des notes reçues
    compt1=0 #compter le nombre de notes reçues pour le module1
    compt2=0 #compter le nombre de notes reçues pour le module2
    s1=0
    s2=0

    
    class react(CyclicBehaviour):
       async def run(self):
            perform="inform" #perform représente tous les messages de type inform
            onto1="Module1"  #onto1 représente les notes envoyées pour le module1
            onto2="Module2"  #onto2 représente les notes envoyées pour le module2
            print("Admin1 en attente d'un message")
            message = await self.receive(timeout=10) # wait for a message for 10 seconds
            if message :

                #Si le message reçu concerne les notes du module1 :
                if message.get_metadata("ontology")==onto1 and message.get_metadata("performative")== perform:
                        print('Admin_1 !! : Message recu de : {}'.format(message.sender))
                        ## Question 6 : recevoir le premier message "module2"................
                        NM1 = float(message.body) #notes du module1 (NM1 = Note Module1)
                        
                        print("contenu du message : ", NM1)
                        
                        print("Ontology du message : ",message.get_metadata("ontology"))

                        Admin_1.compt1+=1  # Compter le nombre de notes reçues
                        
                        Admin_1.s1+=NM1    # Ajouter la note à la somme des notes

                        print("nombre de notes recu pour module 1 est {0}".format(Admin_1.compt1))
                        
                        if Admin_1.compt1 == 2:
                            ## Question 6 : Calculer la première moyenne ..................
                            moy1=Admin_1.s1/2
                            print ("Moyenne du module 1 est : {} ".format(moy1))
                            ## Question 6.3 : envoyer la première moyenne vers Admin_2.......

                            print ("envoie en cours a admin 2 ....")
                            print("envoie en cours a admin 2 ....")
                            message3 = Message(to='Admin_2@jabber.ig.umons.ac.be') 
                            message3.set_metadata("performative",'inform')
                            
                            #client nom de l’agent récepteur
                            message3.set_metadata("ontology", "moyenne")
                            message3.body = str(moy1) #contenu du message
                            await self.send(message3)

                if message.get_metadata("ontology")==onto2 and message.get_metadata("performative")== perform:
                    print('Admin_1 !! : Message recu de : {}'.format(message.sender))
                    ## Question 6 : recevoir le premier message "module2"................
                    NM2 = float(message.body) #notes du module2 (NM2 = Note Module2)

                    print("contenu du message : ", NM2)

                    print("Ontology du message : ",message.get_metadata("ontology"))

                    Admin_1.compt2+=1  # Compter le nombre de notes reçues

                    Admin_1.s2+=NM2    # Ajouter la note à la somme des notes

                    print("nombre de notes recu pour module 2 est {0}".format(Admin_1.compt2))

                    if Admin_1.compt2 == 2:
                        ## Question 6 : Calculer la 2éme moyenne ..................
                        moy2=Admin_1.s2/2
                        print ("Moyenne du module 2 est : {} ".format(moy2))
                        ## Question 6.3 : envoyer la 2éme moyenne vers Admin_2.......

                        print ("envoie en cours a admin 2 ....")
                        print("envoie en cours a admin 2 ....")
                        message4 = Message(to='Admin_2@jabber.ig.umons.ac.be')
                        message4.set_metadata("performative",'inform')

                        #client nom de l’agent récepteur
                        message4.set_metadata("ontology", "moyenne")
                        message4.body = str(moy2) #contenu du message
                        await self.send(message4)
                #Idem pour le module 2 
                #.....
                #.....
                #.....
                #.....


    async def setup(self):
        print("Demarrage de l'agent Admin_1")
        b = self.react()
        self.add_behaviour(b)
        
