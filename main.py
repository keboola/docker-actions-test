import sys
import time
from keboola import docker

cfg = docker.Config()

if (cfg.get_action() == 'test'):
    sys.stdout.write('test')
elif (cfg.get_action() == 'timeout'):
    time.sleep(60)
elif (cfg.get_action() == 'json'):
    sys.stdout.write('{"tables": ["a", "b", "c"]}')
elif (cfg.get_action() == 'invalidjson'):
    sys.stdout.write('{"tables": ["a", "b", "c"]')
elif (cfg.get_action() == 'noresponse'):
    sys.exit(0)
elif (cfg.get_action() == 'usererror'):
    sys.stdout.write('user error')
    sys.exit(1)
elif (cfg.get_action() == 'apperror'):
    sys.stdout.write('application error')
    sys.exit(2)
elif (cfg.get_action() == 'encrypt'):
    params = cfg.get_parameters()
    if (params.get('#password') == 'password'):
        sys.stdout.write('success')
    else:
        sys.stdout.write('failed')
        sys.exit(1)
else:
    sys.stdout.write('undefined action' + cfg.get_action())
    sys.exit(2)
