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
from leo import misc
import multiprocessing as mp
import shutil

time_suffix = datetime.today().strftime("%d-%m-%Y_%H-%M-%S")
script_abspath, script_name_w_ext = misc.get_script_abspath_n_name(__file__)
script_name = script_name_w_ext.split('.')[0]

def main():
    # Parse console arguments
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--input", type=str, default = "./sample", help="Input dirpath")
    parser.add_argument("-o", "--output", type=str, default = "./", help="Output dirpath")
    args = parser.parse_args()
    args.input = args.input.rstrip('/')
    args.output = args.output.rstrip('/')

    # Create output folder 
    out_dirpath = args.output + f'/format_{time_suffix}'
    if not os.path.isdir(out_dirpath):
        os.mkdir(out_dirpath)

    # Create logger
    logger = misc.get_logger(__name__, log_fpath=out_dirpath + f'/{script_name}.log')
    logger.info(f"Started {script_abspath=} with args: {args}")

    # Read points.xlxs
    points_df = pd.read_excel(args.input + '/points.xlsx')
    point_ids = points_df['point_id'].tolist()
    point_id_to_location_id_dict = dict(zip(points_df['point_id'], points_df['location_id']))
    location_id_to_point_id_dict = dict(zip(points_df['location_id'], points_df['point_id']))

    # Read roads.xlxs
    roads_df = pd.read_excel(args.input + '/roads.xlsx')
    src_ids = roads_df['src'].tolist()
    trg_ids = roads_df['trg'].tolist()

    # Create graph from roads
    G = nx.from_pandas_edgelist(roads_df, 'src', 'trg', ['dist'], create_using=nx.DiGraph())

    # Color nodes red if they are in point_ids, blue otherwise
    node_colors = ['red' if node in point_ids else 'blue' for node in G.nodes()]

    # Extend point_ids with src_ids and trg_ids
    point_ids.extend(src_ids)
    point_ids.extend(trg_ids)
    max_point_id = max(point_ids)
    next_point_id = max_point_id + 1

    # Remove duplicates
    point_ids = list(set(point_ids))
    
    # Transform location_id in flights.xlsx to point_id
    flights_df = pd.read_excel(args.input + '/flights.xlsx')

    # Rename column location_id to point_id
    flights_df.rename(columns={'location_id': 'point_id'}, inplace=True)
    
    for i, row in flights_df.iterrows():
      gate_id = row['gate']
      if row['point_id'] in location_id_to_point_id_dict:
          flights_df.at[i, 'point_id'] = location_id_to_point_id_dict[row['point_id']]
      else:
          location_id_to_point_id_dict[row['point_id']] = next_point_id
          flights_df.at[i, 'point_id'] = next_point_id
          next_point_id += 1
          
          # # add road to roads.xlsx
          # roads_df = roads_df.append({'src': gate_id, 'trg': flights_df.at[i, 'point_id'], 'dist': 1500}, ignore_index=True)
          
          # # add point to points.xlsx
          # points_df = points_df.append({'point_id': location_id_to_point_id_dict[row['point_id']], 
          #                               'point_id': row['point_id']}, 
          #                               ignore_index=True)

      # add edge from gate_id to location_id , dist = 1500
      G.add_edge(location_id_to_point_id_dict[gate_id], flights_df.at[i, 'point_id'], dist=1500)

    # Save flights_df as csv
    flights_df.to_csv(out_dirpath + '/flights.csv', index=False)

    # Save location_id_to_point_id_dict as points.csv
    pd.DataFrame.from_dict(location_id_to_point_id_dict, orient='index').to_csv(out_dirpath + '/points.csv', header=False)

    # Save edges from G as roads.csv with columns id, src, trg, dist
    header = 'id,src,trg,dist'
    with open(out_dirpath + '/roads.csv', 'w') as f:
      f.write(header + '\n')
      for i, (src, trg, dist) in enumerate(G.edges.data('dist')):
        f.write(f'{i},{src},{trg},{dist}' + '\n')

    # # Save points_df
    # points_df.to_excel(out_dirpath + '/points.xlsx', index=False)

    # # Save roads_df
    # roads_df.to_excel(out_dirpath + '/roads.xlsx', index=False)

if __name__ == '__main__':
    main() 