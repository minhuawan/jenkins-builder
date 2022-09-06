import subprocess as sp
from datetime import datetime as dt


def log(msg):
    print(f"{dt.now().strftime('%H:%M:%S')}: {msg}", flush=True)


def execute_command(command):
    log(f'start execute command {command}')
    code = sp.call(command)
    if code != 0:
        log(f'exit build because execute command failed with code: {code}, command: {command}')
        exit(code)
