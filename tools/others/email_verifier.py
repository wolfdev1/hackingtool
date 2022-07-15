# coding=utf-8
from core import HackingTool
from core import HackingToolsCollection

#It is highly recommended to use the tools inside root
#sudo su, this to improve efficiency, which is the goal of this tool

#Avoid running tools while another python process is running 
#since it can interfere or cause performance problems when we use the tools 

class KnockMail(HackingTool):
    TITLE = "Knockmail"
    DESCRIPTION = "KnockMail Tool Verify If Email Exists"
    INSTALL_COMMANDS = [
        "git clone https://github.com/heywoodlh/KnockMail.git",
        "cd KnockMail;sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd KnockMail;python3 knockmail.py"]
    PROJECT_URL = "https://github.com/heywoodlh/KnockMail"


class EmailVerifyTools(HackingToolsCollection):
    TITLE = "Email Verify tools"
    TOOLS = [KnockMail()]
    
