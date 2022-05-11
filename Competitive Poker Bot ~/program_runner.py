import re
import os
import sys
import subprocess
from multiprocessing import Process
import platform


class SysRunner:
    def __init__(self):
        self.cc_bot = os.path.join(os.path.abspath(os.path.dirname(__file__)), "cc-bot/cc.py")
        self.cc_log = os.path.join(os.path.abspath(os.path.dirname(__file__)), "output-log/cc.out")

        self.rourou_bot = os.path.join(os.path.abspath(os.path.dirname(__file__)), "cc-bot/rourou.py")
        self.rourou_log = os.path.join(os.path.abspath(os.path.dirname(__file__)), "output-log/rourou.out")


    def run_rourou(self):
        print(f'[CPID {os.getpid()}] Running rourou...')

        py_ver = re.match("^[0-9][.][0-9]", platform.python_version()).group(0)
        with open(self.rourou_log, 'wb') as rourou_fp:
            rourou_proc = subprocess.Popen([f'python{py_ver}', self.rourou_bot], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def run_rourou(self):
        print(f'[CPID {os.getpid()}] Running rourou...')

        py_ver = re.match("^[0-9][.][0-9]", platform.python_version()).group(0)
        with open(self.rourou_log, 'wb') as rourou_fp:
            rourou_proc = subprocess.Popen([f'python{py_ver}', self.rourou_bot], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def run_cc(self):
        print(f'[CPID {os.getpid()}] Running CC...')

        py_ver = re.match("^[0-9][.][0-9]", platform.python_version()).group(0)
        with open(self.cc_log, 'wb') as cc_fp:
            cc_proc = subprocess.Popen([f'python{py_ver}', self.cc_bot], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def run_program(self):
        print(f'[PPID {os.getpid()}] Program Started...')

        rourou_proc = Process(target=self.run_rourou)
        rourou_proc.start()

        cc_proc = Process(target=self.run_cc)
        cc_proc.start()

        rourou_proc.join()
        cc_proc.join()


if __name__ == "__main__":
    runner = SysRunner()
    runner.run_program()