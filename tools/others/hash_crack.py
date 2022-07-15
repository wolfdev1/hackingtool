# coding=utf-8
from core import HackingTool
from core import HackingToolsCollection

#It is highly recommended to use the tools inside root
#sudo su, this to improve efficiency, which is the goal of this tool

#Avoid running tools while another python process is running 
#since it can interfere or cause performance problems when we use the tools 

class HashBuster(HackingTool):
    TITLE = "Hash Buster"
    DESCRIPTION = "Features: \n " \
                  "Automatic hash type identification \n " \
                  "Supports MD5, SHA1, SHA256, SHA384, SHA512"
    INSTALL_COMMANDS = [
        "git clone https://github.com/s0md3v/Hash-Buster.git",
        "cd Hash-Buster;make install"
    ]
    RUN_COMMANDS = ["buster -h"]
    PROJECT_URL = "https://github.com/s0md3v/Hash-Buster"


class HashCrackingTools(HackingToolsCollection):
    TITLE = "Hash cracking tools"
    TOOLS = [HashBuster()]
