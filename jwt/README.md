# 目录

- [目录](#目录)
  - [什么是JWT](#什么是jwt)
  - [JWT作用](#jwt作用)
  - [相关名词解释](#相关名词解释)
  - [JWT构成](#jwt构成)
  - [python jwt](#python-jwt)
  - [Usage](#usage)
  - [实施细节](#实施细节)
    - [支持算法](#支持算法)
    - [支持python](#支持python)
  - [jwt实现原理](#jwt实现原理)
    - [生成规则](#生成规则)

## 什么是JWT

`JWT`(`JSON Web Token`)指的是一种规范，这种规范允许我们使用JWT在两个组织之间传递安全可靠的信息。而`JWS`(`JSON Web Signature`)和`JWE`(`JSON Web Encryption`)是`JWT`规范的两种不同实现，我们平时最常使用的实现就是JWS

## JWT作用

主要作用于B/S以安全的方式来转移声明
主要场景：

1. 认证 Authentication
2. 授权 Authorization
3. 联合识别；
4. 客户端会话（无状态的会话）
5. 客户端机密

## 相关名词解释

- JWS：Sigened JWT
- JWE：Encryted JWT 部分payload经过加密的jwt
- JWK：JWT密钥
- JWKset：密钥对，JWT key set在非对称加密
- nonsecure JWT：不签名算法，不安全，任何人可改修改

## JWT构成

三大体：

- header: 声明了JWT签名算法

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

- payload: 成功在各种声明并传递明文数据

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
```

- signuture: 签了名的JWS

```json
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)
```

## python jwt

`python jwt` 是由 `Gehirn Inc` 开发的`python`中的`json web`令牌（`jwt`）实现

## Usage

若需要使用，项目中`requirement`放入自己的项目，执行下方`pip3`命令即可

若想看本项目运行效果，直接执行下面的三条命令即可看到效果

```sh
# 拉取代码
$ https://github.com/MMobot/jwt_demo.git
# 安装依赖
$ pip3 install -r requirements.txt
# 运行.py文件
$ python xx.py
```

## 实施细节

### 支持算法

- 不安全
  - 无
- 对称加密HMAC（哈希消息验证码）
  - HS256
  - HS384
  - HS512
- 非对称加密RSASSA（RAS签名算法）
  - RS256
  - RS384
  - RS512
- ECDSA（椭圆曲线数据签名算法）
  - ES256
  - ES384
  - ES512

### 支持python

python3.5 - python3.7

## jwt实现原理

jwt的生成token格式如下，即：由 . 连接的三段字符串组成
`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`

### 生成规则

- headers: 固定包含算法和token类型，base64url加密

> ex.

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

- payload: 包含一些数据，base64url加密

> ex.

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
  ...
}
```

- signature: 前两段的base密文通过.拼接，然后对其进行HS256加密，再对hs256密文进行base64url加密
  1. headers的base密文 + payload的base密文
  2. 对1生成进行HS256加密
  3. 对2生成进行base64url加密

> ex.

```json
base64url(
    HMACSHA256(
      base64UrlEncode(header) + "." + base64UrlEncode(payload),
      your-256-bit-secret (秘钥加盐)
    )
)
```
