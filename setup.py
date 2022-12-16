import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

build_exe_options = {"packages": [] , "include_files":["driverfile","creds.txt"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "DYP autologin",
    version = "0.1",
    description = "DYP college firewall credentials auto login application",
    options = {"build_exe": build_exe_options},
    executables = [Executable("dyp_autologin.py", base=base)]
)