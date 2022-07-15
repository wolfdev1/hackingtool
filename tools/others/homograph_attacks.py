# coding=utf-8
from core import HackingTool
from core import HackingToolsCollection

#It is highly recommended to use the tools inside root
#sudo su, this to improve efficiency, which is the goal of this tool

#Avoid running tools while another python process is running 
#since it can interfere or cause performance problems when we use the tools 

class EvilURL(HackingTool):
    TITLE = "EvilURL"
    DESCRIPTION = "Generate unicode evil domains for IDN Homograph Attack " \
                  "and detect them."
    INSTALL_COMMANDS = ["git clone https://github.com/UndeadSec/EvilURL.git"]
    RUN_COMMANDS = ["cd EvilURL;python3 evilurl.py"]
    PROJECT_URL = "https://github.com/UndeadSec/EvilURL"


class IDNHomographAttackTools(HackingToolsCollection):
    TITLE = "IDN Homograph Attack"
    TOOLS = [EvilURL()]
