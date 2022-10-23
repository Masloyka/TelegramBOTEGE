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
    parser.add_argument("-i", "--input", type=str, default = "/home/leo/GitHub/aviahack-22/task/tests/jopka", help="Input dirpath")
    parser.add_argument("-o", "--output", type=str, default = "/home/leo/GitHub/aviahack-22/task/tests/jopka", help="Output dirpath")
    args = parser.parse_args()
    args.input = args.input.rstrip('/')
    args.output = args.output.rstrip('/')

    # Create output folder 
    out_dirpath = args.output + f'/solution_{time_suffix}'
    if not os.path.isdir(out_dirpath):
        os.mkdir(out_dirpath)

    # Create logger
    logger = misc.get_logger(__name__, log_fpath=out_dirpath + f'/{script_name}.log')
    logger.info(f"Started {script_abspath=} with args: {args}")

    # Read buses.csv
    buses_df = pd.read_csv(args.input + '/buses.csv')
    buses = buses_df.to_dict('records')

    # Read roads.csv
    roads_df = pd.read_csv(args.input + '/roads.csv')
    roads = roads_df.to_dict('records')

    # Read flights.csv
    flights_df = pd.read_csv(args.input + '/flights.csv')
    flights = flights_df.to_dict('records')

    # Create graph from roads
    G = nx.DiGraph()
    for road in roads:
      G.add_edge(road['src'], road['trg'], weight=road['dist'])

    # Calculate all pairs shortest paths
    all_pairs_shortest_paths_length = dict(nx.all_pairs_dijkstra_path_length(G))

    # Assign one or several buses to flights
    for flight in flights:
      flight_cap = flight['passengers']
      flight_buses = []

      i = 0
      while flight_cap > 0 and i < 1000:
        bus = random.choice(buses)
        flight_cap -= bus['capacity']
        flight_buses.append(bus['bus_id'])
        i += 1

      flight['buses'] = flight_buses

      for b in flight_buses:
        if 'flights' not in buses[b]:
          buses[b]['flights'] = []
        buses[b]['flights'].append(flight['id'])

    # Remove unused buses
    buses = [b for b in buses if 'flights' in b]

    solution = []

    # Simulate bus movement
    for bus in tqdm.tqdm(buses):
      logger.info(f'Bus {bus["bus_id"]}')
      bus_start_time = 0
      for flight_id in bus['flights']:
        flight = flights[flight_id]
        src, trg = flight['point_id'], flight['gate_id']
        if flight['type'] == 'D':
          src, trg = trg, src

        bus_cur_point = bus['point_id']
        logger.info(f'Flight {flight_id} {src} -> {trg}')
        logger.info(f'bus_cur_point, src, trg: {bus_cur_point}, {src}, {trg}')

        task_time_1 = all_pairs_shortest_paths_length[bus_cur_point][src]
        task_type_1 = 'to_load_from_aircraft' if flight['type'] == 'A' else 'to_load_from_gate'

        task_time_11 = 5
        task_type_11 = 'loading'

        task_time_2 = all_pairs_shortest_paths_length[src][trg]
        task_type_2 = 'to_unload_to_aircraft' if flight['type'] == 'D' else 'to_unload_to_gate'

        task_time_21 = 10
        task_type_21 = 'unloading'

        solution.append({
          'bus_id': bus['bus_id'],
          'flight_id': flight_id,
          'passengers': flight['passengers'],
          'task_type': task_type_1,
          'src': bus_cur_point,
          'trg': src,
          'start_time': bus_start_time,
          'end_time': bus_start_time + task_time_1,
        })

        solution.append({
          'bus_id': bus['bus_id'],
          'flight_id': flight_id,
          'passengers': flight['passengers'],
          'task_type': task_type_11,
          'src': src,
          'trg': src,
          'start_time': bus_start_time + task_time_1,
          'end_time': bus_start_time + task_time_1 + task_time_11,
        })

        solution.append({
          'bus_id': bus['bus_id'],
          'flight_id': flight_id,
          'passengers': flight['passengers'],
          'task_type': task_type_2,
          'src': src,
          'trg': trg,
          'start_time': bus_start_time + task_time_1 + task_time_11,
          'end_time': bus_start_time + task_time_1 + task_time_11 + task_time_2,
        })

        solution.append({
          'bus_id': bus['bus_id'],
          'flight_id': flight_id,
          'passengers': flight['passengers'],
          'task_type': task_type_21,
          'src': trg,
          'trg': trg,
          'start_time': bus_start_time + task_time_1 + task_time_11 + task_time_2,
          'end_time': bus_start_time + task_time_1 + task_time_11 + task_time_2 + task_time_21,
        })

        bus_start_time += task_time_1 + task_time_11 + task_time_2 + task_time_21
        bus['point_id'] = trg

        flight_complete_time = bus_start_time + task_time_1 + task_time_2 if flight['type'] == 'D' else bus_start_time + task_time_1
        flight['complete_time'] = flight_complete_time

    # Write solution.csv
    header = ['bus_id', 'flight_id', 'passengers', 'task_type', 'src', 'trg', 'start_time', 'end_time']
    solution_df = pd.DataFrame(solution, columns=header)
    solution_df.to_csv(out_dirpath + '/solution.csv', index=False)

    # Write flights-new.csv
    header = 'id,type,date,time,point_id,gate_id,passengers,buses,complete_time'.split(',')
    flights_df = pd.DataFrame(flights, columns=header)
    flights_df.to_csv(out_dirpath + '/flights-new.csv', index=False)

if __name__ == '__main__':
    main() 