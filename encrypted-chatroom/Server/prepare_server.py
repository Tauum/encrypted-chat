from config import PORT
from signal import SIGTERM  # or SIGKILL
from psutil import process_iter


def kill_process_on_port():
    for proc in process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == PORT:
                proc.send_signal(SIGTERM)  # or SIGKILL


def run_prepare():
    kill_process_on_port()
