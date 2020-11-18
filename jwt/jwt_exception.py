import jwt
import time
from jwt import exceptions

headers = {
  "alg": "HS256",
  "typ": "JWT"
}
salt = "asgfdgerher"
# 设置立即失效
exp = int(time.time() - 1)
payload = {
  "name": "dawsonenjoy",
  "exp": exp
}

token = jwt.encode(payload=payload, key=salt, algorithm='HS256', headers=headers).decode('utf-8')
try:
    info = jwt.decode(token, salt, True, algorithm='HS256')
    print(info)
except exceptions.ExpiredSignatureError:
    print('token已失效')
except jwt.DecodeError:
    print('token认证失败')
except jwt.InvalidTokenError:
    print('非法的token')