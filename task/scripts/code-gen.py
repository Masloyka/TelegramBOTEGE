import functools as ft
from scipy import stats
import random
import math
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import time
import subprocess
import os
import sys
import argparse 
from datetime import datetime
import tqdm
import pylab as plb
import misc
import multiprocessing as mp
import shutil

time_suffix = datetime.today().strftime("%d-%m-%Y_%H-%M-%S")
script_abspath, script_name_w_ext = misc.get_script_abspath_n_name(__file__)
script_name = script_name_w_ext.split('.')[0]

def main():
    # Parse console arguments
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", type=str, default = "./", help="Input dirpath")
    parser.add_argument("-o", "--output", type=str, default = "./", help="Output dirpath")
    args = parser.parse_args()
    args.input = args.input.rstrip('/')
    args.output = args.output.rstrip('/')

    # Create output folder 
    out_dirpath = args.output + f'/codegen_{time_suffix}'
    if not os.path.isdir(out_dirpath):
        os.mkdir(out_dirpath)

    # Create logger
    logger = misc.get_logger(__name__, log_fpath=out_dirpath + f'/{script_name}.log')
    logger.info(f"Started {script_abspath=} with args: {args}")

    # # Read buses.csv
    # buses_df = pd.read_csv(args.input + '/buses.csv')
    # buses = buses_df.to_dict('records')

    # # Read roads.csv
    # roads_df = pd.read_csv(args.input + '/roads.csv')
    # roads = roads_df.to_dict('records')

    # Read flights.csv
    flights_df = pd.read_csv(args.input + '/flights-new.csv')
    flights = flights_df.to_dict('records')

    # Read solution.csv
    solution_df = pd.read_csv(args.input + '/solution.csv')
    solution = solution_df.to_dict('records')

    """
    Transform solution.csv and fligts.csv to json structures as follows:
    start1 = {
      'isStart': True,
      'id': 1,
      'buses': [5, 6, 10],
      'src': '1',
      'trg': '2',
      'passengers': 100,
    }
    stop1 = {
      'isStart': False,
      'id': 1,
      'buses': [5, 6, 10],
      'src': '1',
      'trg': '2',
      'passengers': 100,
    }
    ...
    timeDict = {
      '123': [start1, stop1, ...],
      '456': [start2, stop2, ...],
    }
    """

    # Create timeDict
    timeDict = {}
    starts = {}
    stops = {}
    for flight in flights:
      id = flight['id']
      src, trg = flight['gate_id'], flight['point_id']
      if flight['type'] == 'A':
        src, trg = trg, src
      starts[id] = {
          'isStart': True,
          'id': id,
          'buses': [],
          'src': src,
          'trg': trg,
          'passengers': flight['passengers'],
      }
      stops[id] = {
          'isStart': False,
          'id': id,
          'buses': [],
          'src': src,
          'trg': trg,
          'passengers': flight['passengers'],
      }

    for i, row in enumerate(solution):
      type = row['task_type']
      bus_id = row['bus_id']
      id = row['flight_id']
      passengers = row['passengers']
      src = row['src']
      trg = row['trg']
      start_time = row['start_time']
      end_time = row['end_time']
        
      if type in ['loading', 'unloading']:
        continue  
      
      # isStart == True if type starts with "to_load"
      isStart = type.startswith('to_load')

      if isStart:
        starts[id]['buses'].append(bus_id)
      else:
        stops[id]['buses'].append(bus_id)
    
    for k, v in starts.items():
      if v['src'] not in timeDict:
        timeDict[v['src']] = []
      timeDict[v['src']].append(v)

    for k, v in stops.items():
      if v['trg'] not in timeDict:
        timeDict[v['trg']] = []
      timeDict[v['trg']].append(v)

    # Save start, stop and time dicts as python code to 'code.py'
    with open(out_dirpath + '/code.py', 'w') as f:
      f.write(f'starts = {starts}' + '\n\n\n')
      print(f'starts = {starts}')
      f.write(f'stops = {stops}' + '\n\n\n')
      print(f'stops = {stops}')
      f.write(f'timeDict = {timeDict}' + '\n\n\n')
      print(f'timeDict = {timeDict}')


if __name__ == '__main__':
    main() 