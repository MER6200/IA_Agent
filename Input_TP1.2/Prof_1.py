
# Prof_1
import time
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template
import json 


class Prof_1(Agent):


    class on_start(OneShotBehaviour):
        async def run(self):
            print("Envoie de la note 1 - Module 1")

            #ajouter le destinataire du message 1
            msg = Message(to="Admin_1@jabber.ig.umons.ac.be")
            #ajouter l'ontologie du message 1
            msg.set_metadata("ontology", "Module1")
            #ajouter le performative du message 1
            msg.set_metadata("performative", "inform")
            #ajouter le contenu du message 1
            msg.body = "18"


            await self.send(msg)
            time.sleep(5)
            print("Envoie de la note 2 - Module 1")

            #ajouter le destinataire du message 2
            message2 = Message(to="Admin_1@jabber.ig.umons.ac.be")
            #ajouter l'ontologie du message 2
            message2.set_metadata("ontology", "Module1")
            #ajouter le performative du message 2
            message2.set_metadata("performative", "inform")
            #ajouter le contenu du message 1 
            message2.body = "17"
            await self.send(message2)
            await self.agent.stop()

    

    async def setup(self):
        print("Demarrage de l'agent Prof_1")
        b = self.on_start()
        self.add_behaviour(b)
        
      

