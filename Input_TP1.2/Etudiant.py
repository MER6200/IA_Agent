
# Prof_1
import time
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template
import json


class Etudiant(Agent):


    class on_start(CyclicBehaviour):
        async def run(self):


            reception = await self.receive(timeout=10)
            if reception:
                if reception.get_metadata("ontology") == "Note" and reception.get_metadata("performative") == "inform":
                    print("Je suis l'etudiant et j'ai recu mes notes.")
                    print("Voici mes notes  : {}".format(reception.body) + ".\nMerci!")
                    await self.agent.stop()

            #ajouter le destinataire du message 1
            msg = Message(to="Admin_2@jabber.ig.umons.ac.be")
            #ajouter l'ontologie du message 1
            msg.set_metadata("ontology", "Note")
            #ajouter le performative du message 1
            msg.set_metadata("performative", "query")
            #ajouter le contenu du message 1
            msg.body = "Demande note"
            time.sleep(5)
            await self.send(msg)





    async def setup(self):
        print("Demarrage de l'agent Etudiant et je demande ma note")
        b = self.on_start()
        self.add_behaviour(b)



