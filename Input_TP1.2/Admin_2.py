# Admin_2
import json
import time
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template


class Admin_2(Agent):
    # definition des variables essentielles au calcul de la moyenne génerale
    s = 0
    count = 0
    note = dict()
    class react(CyclicBehaviour):

        async def run(self):
            per = "inform"  # per représente la performative inform
            onto = "moyenne"  # onto représente l'ontologie des message recu de admin1
            print('Admin2 en attente d un message')
            message = await self.receive(timeout=10)  # wait for a message for 10 seconds
            if message:
                ## Question 7 : Recevoir les deux messages venant de Admin_1 ......
                if (message.get_metadata("performative")) == per and (message.get_metadata("ontology")) == onto:

                    print("Question 7.1 : recevoir les deux messages ")

                    print('Admin_2 !! : Message recu de : {}'.format(message.sender))
                    NMoy = float(message.body)  # notes du module1 (NM1 = Note Module1)
                    print("contenu du message : ", NMoy)
                    print("Ontology du message : ", message.get_metadata("ontology"))

                    # Compter le nombre de notes reçues
                    Admin_2.count += 1
                    if Admin_2.count == 1:
                        Admin_2.note.update({"Module1":NMoy})
                    # Ajouter la note à la somme des notes
                    Admin_2.s += NMoy

                    print("le nombre de moyenne est {0}".format(Admin_2.count))
                    if Admin_2.count == 2:
                        # calculer moyenne générale
                        Admin_2.note.update({"Module2":NMoy})
                        moygeneral = Admin_2.s / 2
                        print("Moyenne generale est : {} ".format(moygeneral))

                # Pour recevoir l'étudiant
                elif message.get_metadata("ontology") == "Note" and message.get_metadata("performative") == "query":
                    print('Admin_2 !! : Message recu de : {}'.format(message.sender))
                    print("Il a envoyé :{}".format(message.body))
                    message4 = Message(to='Admin_1@jabber.ig.umons.ac.be')
                    message4.set_metadata("performative", 'inform')
                    message4.set_metadata("ontology", "Note")
                    message4.body = "Puis-je envoyé les notes à l'etudiant"  # contenu du message
                    await self.send(message4)
                # Si Admin1 envoie l'accord
                elif message.get_metadata("ontology") == "Note" and message.get_metadata("performative") == "inform":
                    print('Admin_2 !! : Message recu de : {}'.format(message.sender))
                    print("Il a envoyé son accord pour l'étudiant!")
                    envoie_etudiant = Message(to='etudiant@jabber.ig.umons.ac.be')
                    envoie_etudiant.set_metadata("performative", 'inform')
                    envoie_etudiant.set_metadata("ontology", "Note")
                    Note_enc = json.dumps(Admin_2.note)
                    envoie_etudiant.body = Note_enc  # contenu du message
                    await self.send(envoie_etudiant)
                    time.sleep(2)
                    await self.agent.stop()

    async def setup(self):

        print("Bonjour je suis admin_2")
        b = self.react()
        self.add_behaviour(b)
