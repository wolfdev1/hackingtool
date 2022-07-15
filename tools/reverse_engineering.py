# coding=utf-8
import subprocess

from core import HackingTool
from core import HackingToolsCollection

#It is highly recommended to use the tools inside roo
#sudo su, this to improve efficiency, which is the goal of this tool

#Avoid running tools while another python process is running 

#since it can interfere or cause performance problems when we use the tools 

class AndroGuard(HackingTool):
    TITLE = "Androguard"
    DESCRIPTION = "Androguard is a Reverse engineering, Malware and goodware " \
                  "analysis of Android applications and more"
    INSTALL_COMMANDS = ["sudo pip3 install -U androguard"]
    PROJECT_URL = "https://github.com/androguard/androguard "

    def __init__(self):
        super(AndroGuard, self).__init__(runnable = False)


class Apk2Gold(HackingTool):
    TITLE = "Apk2Gold"
    DESCRIPTION = "Apk2Gold is a CLI tool for decompiling Android apps to Java"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/lxdvs/apk2gold.git",
        "cd apk2gold;sudo bash make.sh"
    ]
    PROJECT_URL = "https://github.com/lxdvs/apk2gold "

    def run(self):
        uinput = input("Enter (.apk) File >> ")
        subprocess.run(["sudo", "apk2gold", uinput])


class Jadx(HackingTool):
    TITLE = "JadX"
    DESCRIPTION = "Jadx is Dex to Java decompiler.\n" \
                  "[*] decompile Dalvik bytecode to java classes from APK, dex," \
                  " aar and zip files\n" \
                  "[*] decode AndroidManifest.xml and other resources from " \
                  "resources.arsc"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/skylot/jadx.git",
        "cd jadx;./gradlew dist"
    ]
    PROJECT_URL = "https://github.com/skylot/jadx"

    def __init__(self):
        super(Jadx, self).__init__(runnable = False)


class ReverseEngineeringTools(HackingToolsCollection):
    TITLE = "Reverse engineering tools"
    TOOLS = [
        AndroGuard(),
        Apk2Gold(),
        Jadx()
    ]
