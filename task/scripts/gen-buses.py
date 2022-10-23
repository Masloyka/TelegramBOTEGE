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
    parser.add_argument("-o", "--output", type=str, default = "../tests/", help="Output dirpath")
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

    # Read points.csv
    points_df = pd.read_csv(args.input + '/points.csv')
    point_ids = points_df['point_id'].tolist()
    
    # Generate 30 random buses with capacity 100 in random points
    buses = []
    for i in range(30):
        buses.append({
            'bus_id': i,
            'capacity': 100,
            'point_id': random.choice(point_ids)
        })
    
    for i in range(10):
        buses.append({
            'bus_id': i,
            'capacity': 50,
            'point_id': random.choice(point_ids)
        })

    buses_df = pd.DataFrame(buses)
    buses_df.to_csv(out_dirpath + '/buses.csv', index=False)
    
if __name__ == '__main__':
    main() 