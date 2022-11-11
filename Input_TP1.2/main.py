import time
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour, CyclicBehaviour
from spade.message import Message
from spade.template import Template

from typing import Optional, Dict, Type
import json
from Prof_1 import Prof_1
from Prof_2 import Prof_2
from Admin_1 import Admin_1
from Admin_2 import Admin_2
from Etudiant import Etudiant



if __name__ == "__main__":
    Admin2 = Admin_2("Admin_2@jabber.ig.umons.ac.be", "VPTJL0GkOp7ZY9v")
    # démarrer l'agent et voir ce qu'il affiche 
    Admin2.start()
    Admin2.web.start(hostname="127.0.0.1",port="10000")
    time.sleep(1)
    Admin1 = Admin_1("Admin_1@jabber.ig.umons.ac.be", "JCqnbzJ5DxegAYC")
    # démarrer l'agent 
    Admin1.start()
    Admin1.web.start(hostname="127.0.0.2",port="10001")
    time.sleep(1)
    Prof1 = Prof_1("Prof_1@jabber.ig.umons.ac.be", "a0ZGkWVwvxeW1gt")
    # démarrer l'agent 
    Prof1.start()

    Prof2 = Prof_2("Prof_2@jabber.ig.umons.ac.be", "my2DvoknCf6kBA7")
    time.sleep(1)
    # démarrer l'agent 
    Prof2.start()

    Etudiant1 = Etudiant("etudiant@jabber.ig.umons.ac.be", "nGuFNpShG8XW7d4")
    time.sleep(1)
    # démarrer l'agent
    Etudiant1.start()
    time.sleep(1)
     
    while Admin2.is_alive() and Admin1.is_alive():
        try:
            time.sleep(10)
        except KeyboardInterrupt:
            Admin1.stop()
            Admin2.stop()
            Prof2.stop()
            Prof1.stop()
            Etudiant1.stop()
            break
    print("Agents finished")