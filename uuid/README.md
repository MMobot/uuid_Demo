# uuid

- [uuid](#uuid)
  - [什么是uuid](#什么是uuid)
  - [什么是RFC](#什么是rfc)
  - [用途](#用途)
    - [若需要唯一id](#若需要唯一id)
  - [类uuid.SafeUUID](#类uuidsafeuuid)
    - [新版功能](#新版功能)
  - [UUID实例的只读属性](#uuid实例的只读属性)
    - [UUID功能](#uuid功能)
    - [以下只针对uuid3()和uuid5()](#以下只针对uuid3和uuid5)
    - [经典示例](#经典示例)

## 什么是uuid

- 提供不可变uuid对象
- 四个功能(生成1/3/4/5版本uuid)
  - uuid1()
  - uuid3()
  - uuid4()
  - uuid5()

## 什么是RFC

```txt
RFC 4122-通用唯一标识符（UUID）URN命名空间
该规范定义了UUID的统一资源名称名称空间，UUID的内部格式以及生成UUID的方法
```

## 用途

### 若需要唯一id

使用uuid1()或uuid4()

- uuid1()
`可能损害隐私，因为创建了包含计算机网络的uuid`
- uuid4()
`创建了一个随机的uuid`

## 类uuid.SafeUUID

### 新版功能

- safe
`uuid是由平台以多处理安全方式生成的`
- unsafe
`uuid不是由平台以多处理安全方式生成的`
- unknown
`该平台不提供有关是否已安全生成的uuid信息`

> ex.

```txt
类uuid.UUID（hex = None，bytes = None，bytes_le = None，fields = None，int = None，version = None，*，is_safe = SafeUUID.unknown ）
```

```py
UUID('{12345678-1234-5678-1234-567812345678}')
UUID('12345678123456781234567812345678')
UUID('urn:uuid:12345678-1234-5678-1234-567812345678')
UUID(bytes=b'\x12\x34\x56\x78'*4)
UUID(bytes_le=b'\x78\x56\x34\x12\x34\x12\x78\x56' +
              b'\x12\x34\x56\x78\x12\x34\x56\x78')
UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678))
UUID(int=0x12345678123456781234567812345678)
```

## UUID实例的只读属性

1. UUID.bytes：
UUID为16字节的字符串（包含按big-endian字节顺序排列的六个整数字段）。

2. UUID.bytes_le：
UUID为16字节的字符串（具有little_endian 字节顺序的time_low，time_mid和time_hi_version）。

3. UUID.fields：
以元组形式存放的UUID的6个整数域，有六个单独的属性和两个派生属性：

| 域                   | 含义                   |
| -------------------- | ---------------------- |
| time_low             | UUID的前32位           |
| time_mid             | 接前一域的16位         |
| time_hi_version      | 接前一域的16位         |
| clock_seq_hi_variant | 接前一域的8位          |
| clock_seq_low        | 接前一域的8位          |
| node                 | UUID的最后48位         |
| time                 | UUID的总长60位的时间戳 |
| clock_seq            | 14位的序列号           |

4. UUID.hex：
32个字符的十六进制字符串。

5. UUID.int：
128位整数。

6. UUID.urn：
UUID作为URN，如 RFC 4122。

7. UUID.variant：
UUID变体，用于确定UUID的内部布局。这将是一个常量RESERVED_NCS，RFC_4122， RESERVED_MICROSOFT，或RESERVED_FUTURE。

8. UUID.version：
UUID版本号（1到5，仅当变体为时才有意义 RFC_4122）。

9. UUID.is_safe：
其枚举SafeUUID表示平台是否以多处理安全的方式生成了UUID。

### UUID功能

1. uuid.getnode()

> 在3.7版更改中：通用管理的MAC地址优于本地管理的MAC地址，因为保证前者在全局上是唯一的，而后者则不是全局唯一的
以48位正整数获取硬件地址

2. uuid.uuid1（node = None，clock_seq = None)

根据主机ID，序列号和当前时间生成UUID
- clock_seq
    - 如果有clock_seq，则值作为序列号
    - 如果没有clock_seq，自动随机14位序列号

3. uuid.uuid3(namespace, name)
根据namespace(uuid)和name(string)的MD5哈希值生成uuid

4. uuid.uuid4()
生成一个随机uuid

5. uuid.uuid5(namespace, name)
根据namespace(uuid)和name(string)的SHA-1哈希值生成uuid

### 以下只针对uuid3()和uuid5()

- 与namespace相关
  - uuid.NAMESPACE_DNS
    - 名称字符串是完全限定的域名
  - uuid.NAMESPACE_URL
    - 名称字符串是URL
  - uuid.NAMESPACE_OID
    - 名称字符串为ISO OID
  - uuid.NAMESPACE_X500
    - 名称字符串是DER或文本输出格式的X.500 DN。
- 该uuid模块为variant属性的可能值定义以下常量：
  - uuid.RESERVED_NCS
    - 保留用于NCS兼容性
  - uuid.RFC_4122
    - 指定在中给出的UUID布局 RFC 4122
  - uuid.RESERVED_MICROSOFT
    - 保留用于Microsoft兼容性
  - uuid.RESERVED_FUTURE
    - 保留以供将来定义。

### 经典示例

```py
import uuid

# make a UUID based on the host ID and current time
uuid.uuid1()

# make a UUID using an MD5 hash of a namespace UUID and a name
uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')

# make a random UUID
uuid.uuid4()

# make a UUID using a SHA-1 hash of a namespace UUID and a name
uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')

# make a UUID from a string of hex digits (braces and hyphens ignored)
x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')

# convert a UUID to a string of hex digits in standard form
str(x)

# get the raw 16 bytes of the UUID
x.bytes

# make a UUID from a 16-byte string
uuid.UUID(bytes=x.bytes)
```
