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
    parser.add_argument("-i", "--input", type=str, default = "../tests/sample", help="Input dirpath")
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

    # Read roads.xlxs
    roads_df = pd.read_excel(args.input + '/roads.xlsx')
    src_ids = roads_df['src'].tolist()
    trg_ids = roads_df['trg'].tolist()

    # Create graph from roads
    G = nx.from_pandas_edgelist(roads_df, 'src', 'trg', ['dist'], create_using=nx.MultiDiGraph())

    # Color nodes red if they are in point_ids, blue otherwise
    node_colors = ['red' if node in point_ids else 'blue' for node in G.nodes()]

    # Extend point_ids with src_ids and trg_ids
    point_ids.extend(src_ids)

    # Remove duplicates
    point_ids = list(set(point_ids))

    # Plot graph
    plt.figure(figsize=(10,10))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_color=node_colors, with_labels=True)
    plt.show()

    # Save graph
    plt.savefig(out_dirpath + '/graph-orig.png')

if __name__ == '__main__':
    main() 