#!/usr/bin/env

import time
import string
import sys
import commands
import matplotlib.pyplot as plt
time1=0
def get_cpumem(pid):
    d = [i for i in commands.getoutput("ps aux").split("\n")
        if i.split()[1] == str(pid)]
    return (float(d[0].split()[2]), float(d[0].split()[3])) if d else None

if __name__ == '__main__':
    if not len(sys.argv) == 4 or not all(i in string.digits for i in sys.argv[1]):
        print("usage: %s PID" % sys.argv[0])
        exit(2)
    plt.ion()
    try:
        while True:
            x0,y0 = get_cpumem(sys.argv[1])
            x1,y1 = get_cpumem(sys.argv[1])
            x2,y2 = get_cpumem(sys.argv[1])
            x3,y3 = get_cpumem(sys.argv[1])
            x = x0+x1+x2+x3
            if not x0:
                print("no such process")
                exit(1)
            print("%.2f\t%.2f" % (x0,y0))
            time.sleep(1)
            plt.scatter(time1, x)
            plt.draw()
            plt.title(str("neo_relayboard_joystick"))
            plt.xlabel('time')
            plt.ylabel('CPU usage')
            time1 = time1+1
            plt.pause(1)
        plt.show()

    except KeyboardInterrupt:
        print
        exit(0)