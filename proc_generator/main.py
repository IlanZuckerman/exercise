#!/usr/bin/env python3

import os
import signal
import subprocess
import time

import yaml


def parse_args():
    with open('./config.yml', 'rb') as f:
        conf = yaml.safe_load(f.read())

    return conf['num_procs'], conf['proc_duration'], conf['wget_url'], conf['file_path'], conf['actions']


def main():
    procs = []
    num_procs, proc_duration, wget_url, file_path, actions = parse_args()
    print(
        f"num_procs: {num_procs}, proc_duration: {proc_duration}, wget_url: {wget_url}, file_path: {file_path},"
        f" actions: {actions}"
    )
    for action in actions:
        if action == "fork":
            signal_forks(procs)
            print("forking")
        elif action == "wget":
            pid = run_wget(proc_duration, wget_url)
            procs.append(pid)
            print("wget")
        elif action == "write":
            pid = run_write(proc_duration, file_path)
            procs.append(pid)
            print("writing")
    time.sleep(10)


def run_wget(duration, url):
    """
    call wget script and return its pid
    :param duration: (str) In seconds. for how long the proc should live
    :param url: (str) Url for wget. for example 'google.com'
    :return: (int) generated process pid
    """
    process = subprocess.Popen(["./wget.sh", duration, url])
    return process.pid


def run_write(duration, file_path):
    """
    call file write script and return its pid
    :param duration: (str) In seconds. for how long the proc should live
    :param file_path: (str) Path of the file to be written to
    :return: (int) generated process pid
    """
    process = subprocess.Popen(["./write.sh", duration, file_path])
    return process.pid


def signal_forks(pids):
    """
    If 'fork' action was defined in the config, then the process will be forked. Otherwise - killed.
    SIGUSR1 Is just a signal that if it is passed to the proc, it will then replicate it self (fork).

    :param pids: (list) list of generated processes
    """
    for pid in pids:
        time.sleep(1)
        try:
            os.kill(pid, signal.SIGUSR1)
        except OSError:
            print(pid, " is already gone")
            pids.remove(pid)
        else:
            print(pid, " is signaled to fork iself")


if __name__ == "__main__":
    main()
