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
    parser.add_argument("-n", "--nodes", type=int, default = 10, help="Number of nodes (gates + stops)")
    parser.add_argument("-g", "--gates", type=int, default = 2, help="Number of gates")
    parser.add_argument("-e", "--edges", type=int, default = -1, help="Number of edges")
    parser.add_argument("-o", "--output", type=str, default = "./", help="Output dirpath")
    args = parser.parse_args()

    # Prepare args
    args.input = args.input.rstrip('/')
    args.output = args.output.rstrip('/')

    # Create output folder 
    out_dirpath = args.output + f'/test_{time_suffix}'
    if not os.path.isdir(out_dirpath):
        os.mkdir(out_dirpath)

    # Create logger
    logger = misc.get_logger(__name__, log_fpath=out_dirpath + f'/{script_name}.log')
    logger.info(f"Started {script_abspath=} with args: {args}")

    # Generate random graph 


if __name__ == '__main__':
    main() 