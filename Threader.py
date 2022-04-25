import sys
import subprocess

def threader():
    procs = []
    for i in range(2):
        proc = subprocess.Popen([sys.executable, 'TrendBot.py', '{}in.csv'.format(i), '{}out.csv'.format(i)])
        procs.append(proc)

    for proc in procs:
        proc.wait()

for i in range(100):
    threader()

