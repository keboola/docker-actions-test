import sys
import time
from keboola import docker

cfg = docker.Config()

if (cfg.get_action() == 'test'):
    print('{"test": "test"}')
    sys.exit(0)
elif (cfg.get_action() == 'timeout'):
    time.sleep(60)
    sys.exit(0)
elif (cfg.get_action() == 'invalidjson'):
    print('{"tables": ["a", "b", "c"]')
    sys.exit(0)
elif (cfg.get_action() == 'noresponse'):
    sys.exit(0)
elif (cfg.get_action() == 'usererror'):
    print('user error')
    sys.exit(1)
elif (cfg.get_action() == 'apperror'):
    print('application error')
    sys.exit(2)
elif (cfg.get_action() == 'decrypt'):
    params = cfg.get_parameters()
    if (params.get('#password') == 'password'):
        print('{"password":"' + params.get('#password') + '"}')
    else:
        print('failed')
        print(params)
        sys.exit(1)
else:
    print('undefined action' + cfg.get_action())
    sys.exit(2)
