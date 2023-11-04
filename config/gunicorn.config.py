# gunicorn.config.py
import multiprocessing

bind = "0.0.0.0:8080"
chdir = "config"
workers = multiprocessing.cpu_count() * 2 + 1
