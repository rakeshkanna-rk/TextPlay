'''
Helps to run commands in backend
'''

import os
import subprocess

def backend_subprocess(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except Exception as e:
        print(f"Error: {e}", flush=True)

def backend_suppress(command):
    with open(os.devnull, "w") as devnull:
        command = command.split(" ")
        subprocess.check_call(command, stdout=devnull, stderr=subprocess.STDOUT)

def backend_exec(command):
    os.system(command)
