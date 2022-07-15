# coding=utf-8
from core import HackingTool
from core import HackingToolsCollection

#It is highly recommended to use the tools inside root
#sudo su, this to improve efficiency, which is the goal of this tool

#Avoid running tools while another python process is running 
#since it can interfere or cause performance problems when we use the tools 

class TerminalMultiplexer(HackingTool):
    TITLE = "Terminal Multiplexer"
    DESCRIPTION = "Terminal Multiplexer is a tiling terminal emulator that " \
                  "allows us to open \n several terminal sessions inside one " \
                  "single window."
    INSTALL_COMMANDS = ["sudo apt-get install tilix"]

    def __init__(self):
        super(TerminalMultiplexer, self).__init__(runnable = False)


class MixTools(HackingToolsCollection):
    TITLE = "Mix tools"
    TOOLS = [TerminalMultiplexer()]
