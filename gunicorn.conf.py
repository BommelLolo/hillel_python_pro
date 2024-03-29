import multiprocessing

bind = "127.0.0.1:9000"
workers = multiprocessing.cpu_count() * 2 + 1
wsgi_app = "project.wsgi:application"
loglevel = "debug"
reload = True
