import time
import jwt

# headers 固定参数
# jku: 发送JWK的地址；最好用HTTPS来传输
# jwk: 就是之前说的JWK
# kid: jwk的ID编号
# x5u: 指向一组X509公共证书的URL
# x5c: X509证书链
# x5t：X509证书的SHA-1指纹
# x5t#S256: X509证书的SHA-256指纹
# typ: 在原本未加密的JWT的基础上增加了 JOSE 和 JOSE+ JSON。JOSE序列化后文会说及。适用于JOSE标头的对象与此JWT混合的情况。
# crit: 字符串数组，包含声明的名称，用作实现定义的扩展，必须由 this->JWT的解析器处理。不常见
headers = {
    'alg': "HS256",
    "typ": "JWT"
}

# 随机的salt密钥，只有token生成者（同时也是校验者）自己能有，用于校验生成的token是否合法
salt = "asgfdgerher"

# 设置超时时间：当前时间的100s以后超时
exp = int(time.time()+1)

# payload 固定参数
# iss  【issuer】发布者的url地址
# sub  【subject】该JWT所面向的用户，用于处理特定应用，不是常用的字段
# aud  【audience】接受者的url地址
# exp  【expiration】 该jwt销毁的时间；unix时间戳
# nbf  【not before】 该jwt的使用时间不能早于该时间；unix时间戳
# iat  【issued at】 该jwt的发布时间；unix 时间戳
# jti  【JWT ID】 该jwt的唯一ID编号
payload = {
    "name": "joker",
    "exp": exp
}

# 调用jwt库，生成json web token
jwt_token = jwt.encode(
    payload=payload,
    key=salt,
    algorithm="HS256",
    headers=headers
).decode('utf-8')
# 生成token
print(jwt_token)

# 解码token
# 第是哪个参数标识是否检验，False，只要有token就能解码
info = jwt.decode(jwt_token, salt, True, algorithm="HS256")
print(info)

# 等待2s后再次验证token，因超时将导致验证失败
time.sleep(2)
try:
    info = jwt.decode(jwt_token, salt, True, algorithm='HS256')
    print(info)
except Exception as e:
    print(repr(e))

# 第三个参数设置为False，不进行校验，直接解码token
info = jwt.decode(jwt_token, '', False, algorithm='HS256')
print(info)

