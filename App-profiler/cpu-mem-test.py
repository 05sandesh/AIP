#!/usr/bin/env python3 
import argparse
from distutils.log import debug
import math
import threading

from skywalking import agent, config
from flask import Flask

# app = Flask(__name__)

def tester(load):
  try:
    load = int(load)
  except:
    load = 10
  while(load):
    x = 0 
    for i in range(0, 1000000) :
          x += math.sqrt(x)
    load = load - 1
  return str(load) 

def collectMetrics():
  config.init(collector_address='127.0.0.1:12800', service_name='your awesome service')
  agent.start()

# @app.route('/')
def main() -> int:
    parser = argparse.ArgumentParser(description = 'Input load for test application  ')
    # group = parser.add_mutually_exclusive_group()
    
    parser.add_argument('-l',  help= "load ")
    args = parser.parse_args()
    # print(args)
    retVal = 'hello World'
    if args.l:
        print(args.l)
        # new_thread = threading.Thread(target=tester, args=args.l)
        # threading.Thread(target=tester).start()
        # new_thread.start()
        retVal = tester(args.l)
        # new_thread1 = threading.Thread(target=collectMetrics)
        # new_thread1.start()
        # collectMetrics()
    return retVal

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=12800)

if __name__ == '__main__':
    main()






