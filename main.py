from flask import json

from api.endpoints import api

urlvars = False
swagger = True

data = api.as_postman(urlvars=urlvars, swagger=swagger)
print(json.dumps(data))
