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
import multiprocessing as mp
import shutil

def main():
    # read flights.csv
    flights_df = pd.read_csv('/home/leo/GitHub/aviahack-22/task/tests/good/flights.csv')

    # make id enumeration from 0
    cnt = 0
    for i, flight in enumerate(flights_df['id']):
        flights_df.at[i, 'id'] = cnt
        cnt += 1
        # print (i, flight)
    
    # save flights.csv
    flights_df.to_csv('/home/leo/GitHub/aviahack-22/task/tests/good/flights.csv', index=False)

if __name__ == '__main__':
    main() 