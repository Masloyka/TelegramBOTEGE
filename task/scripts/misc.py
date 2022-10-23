import logging
import configparser as cfg
import os
import shutil

def get_logger(
    logger_name, logger_level = logging.DEBUG,
    log_stream_level=logging.INFO,  # if log_stream_level == None, stream handler won't be created
    log_fpath=None, log_file_level=logging.DEBUG, # if log_fpath == None, file handler won't be created
    string_format='[%(asctime)s| %(levelname)s] %(message)s'
):

    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)

    formatter = logging.Formatter(string_format)

    if log_stream_level != None:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_stream_level)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    if log_fpath != None:
        file_handler = logging.FileHandler(log_fpath)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


    return logger

def get_config(
    config_fpath
):
    script_dirpath = os.path.dirname(__file__)
    shutil.copyfile(script_dirpath + '/config.ini', config_fpath)
    
    config = cfg.ConfigParser()
    config.optionxform = str
    config.read(config_fpath)

    return config

def get_script_abspath_n_name(file):
    file = file.strip('\\')
    abspath = os.path.realpath(file)
    name = os.path.basename(abspath)
    return abspath, name

def path_exists(path):
    return os.path.exists(path)