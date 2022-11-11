
#Admin_2
import time
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template

class Admin_2(Agent):
    #definition des variables essentielles au calcul de la moyenne génerale
    s=0
    count =0
    class react(CyclicBehaviour):
        async def run(self):
            per="inform"      #per représente la performative inform
            onto="moyenne" #onto représente l'ontologie des message recu de admin1
            print('Admin2 en attente d un message')
            message = await self.receive(timeout=10) # wait for a message for 10 seconds
            if message : 
            ## Question 7 : Recevoir les deux messages venant de Admin_1 ......
                if(message.get_metadata("performative"))==per and (message.get_metadata("ontology"))==onto:
                    
                        print ("Question 7.1 : recevoir les deux messages ")
              
                        print('Admin_2 !! : Message recu de : {}'.format(message.sender))
                        NMoy = float(message.body) #notes du module1 (NM1 = Note Module1)
                        print("contenu du message : ", NMoy)
                        print("Ontology du message : ",message.get_metadata("ontology"))

                        # Compter le nombre de notes reçues
                        Admin_2.count+=1
                        # Ajouter la note à la somme des notes
                        Admin_2.s += NMoy

                        print("le nombre de moyenne est {0}".format(Admin_2.count))
                        if Admin_2.count == 2:
                            #calculer moyenne générale 
                            moygeneral = Admin_2.s/2
                            print ("Moyenne generale est : {} ".format(moygeneral))

          
    async def setup(self):
    
        print("Bonjour je suis admin_2")
        b = self.react()
        self.add_behaviour(b)
        