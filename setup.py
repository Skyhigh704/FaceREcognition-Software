from ensurepip import version
import os
from pickletools import optimize
from xml.dom.xmlbuilder import Options
import cx_Freeze
import sys
import os
base = None

if sys.platform == "win32":
    base = "Win32GUI"


os.environ['TCL_LIBRARY'] = r"C:\python\tcl\tcl8.6"
os.environ['Tk_LIBRARY'] =r"C:\python\tcl\tk8.6"

executables=[cx_Freeze.Executable("main.py",base=base,icon="face_recognition_icon_154436.ico")]

cx_Freeze.setup(
    name="Facial Recognition Software",
    options={"build_exe":{"packages":["tkinter","os"],"include_files":["face_recognition_icon_154436.ico",'tcl86t.dll','tk86t.dll','images','data_sets','face_recognition_system']}},
    version="1.0",
    description="Face recogniton system||Devloped by ECE18 student as a project work2",
    executables=executables
)