errorlog = '/var/log/gunicorn/gerror.log'
accesslog = '/var/log/gunicorn/gaccess.log'
# disable_redirect_access_to_syslog = True
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
capture_output = False
loglevel = 'debug'
bind = ['0.0.0.0:8000']
# log-file = /var/log/gunicorn//glog.log
# sudo journalctl -e -u  hello-world