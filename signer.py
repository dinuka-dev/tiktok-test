import time, json, binascii

def rotate_left(a, k):
    k = k % 32
    return ((a << k) & 0xFFFFFFFF) | ((a & 0xFFFFFFFF) >> (32 - k))


def FF_j(X, Y, Z, j):
    if 0 <= j and j < 16:
        ret = X ^ Y ^ Z
    elif 16 <= j and j < 64:
        ret = (X & Y) | (X & Z) | (Y & Z)
    return ret


def GG_j(X, Y, Z, j):
    if 0 <= j and j < 16:
        ret = X ^ Y ^ Z
    elif 16 <= j and j < 64:
        ret = (X & Y) | ((~X) & Z)
    return ret


def P_0(X):
    return X ^ (rotate_left(X, 9)) ^ (rotate_left(X, 17))


def P_1(X):
    return X ^ (rotate_left(X, 15)) ^ (rotate_left(X, 23))


def CF(V_i, B_i, T_j):
    W = []
    for i in range(16):
        weight = 0x1000000
        data = 0
        for k in range(i * 4, (i + 1) * 4):
            data = data + B_i[k] * weight
            weight = int(weight / 0x100)
        W.append(data)

    for j in range(16, 68):
        W.append(0)
        W[j] = P_1(W[j - 16] ^ W[j - 9] ^ (rotate_left(W[j - 3], 15))) ^ (rotate_left(W[j - 13], 7)) ^ W[j - 6]

    W_1 = []
    for j in range(0, 64):
        W_1.append(0)
        W_1[j] = W[j] ^ W[j + 4]
        str1 = "%08x" % W_1[j]

    A, B, C, D, E, F, G, H = V_i

    for j in range(0, 64):
        SS1 = rotate_left(((rotate_left(A, 12)) + E + (rotate_left(T_j[j], j))) & 0xFFFFFFFF, 7)
        SS2 = SS1 ^ (rotate_left(A, 12))
        TT1 = (FF_j(A, B, C, j) + D + SS2 + W_1[j]) & 0xFFFFFFFF
        TT2 = (GG_j(E, F, G, j) + H + SS1 + W[j]) & 0xFFFFFFFF
        D = C
        C = rotate_left(B, 9)
        B = A
        A = TT1
        H = G
        G = rotate_left(F, 19)
        F = E
        E = P_0(TT2)

        A = A & 0xFFFFFFFF
        B = B & 0xFFFFFFFF
        C = C & 0xFFFFFFFF
        D = D & 0xFFFFFFFF
        E = E & 0xFFFFFFFF
        F = F & 0xFFFFFFFF
        G = G & 0xFFFFFFFF
        H = H & 0xFFFFFFFF

    V_i_1 = []
    V_i_1.append(A ^ V_i[0])
    V_i_1.append(B ^ V_i[1])
    V_i_1.append(C ^ V_i[2])
    V_i_1.append(D ^ V_i[3])
    V_i_1.append(E ^ V_i[4])
    V_i_1.append(F ^ V_i[5])
    V_i_1.append(G ^ V_i[6])
    V_i_1.append(H ^ V_i[7])
    return V_i_1


def sm3_hash(msg, key):
    IV = key

    IV = int(IV.replace(" ", ""), 16)

    a = []
    for i in range(0, 8):
        a.append(0)
        a[i] = (IV >> ((7 - i) * 32)) & 0xFFFFFFFF
    IV = a

    T_j = []
    for i in range(0, 16):
        T_j.append(0)
        T_j[i] = 0x79CC4519
    for i in range(16, 64):
        T_j.append(0)
        T_j[i] = 0x7A879D8A

    msg = bytearray(msg)
    len1 = len(msg)
    reserve1 = len1 % 64
    msg.append(0x80)
    reserve1 = reserve1 + 1

    range_end = 56
    if reserve1 > range_end:
        range_end = range_end + 64

    for i in range(reserve1, range_end):
        msg.append(0x00)

    bit_length = (len1) * 8
    bit_length_str = [bit_length % 0x100]
    for i in range(7):
        bit_length = int(bit_length / 0x100)
        bit_length_str.append(bit_length % 0x100)
    for i in range(8):
        msg.append(bit_length_str[7 - i])

    group_count = round(len(msg) / 64)

    B = []
    for i in range(0, group_count):
        B.append(msg[i * 64 : (i + 1) * 64])

    V = []
    V.append(IV)
    for i in range(0, group_count):
        V.append(CF(V[i], B[i], T_j))

    y = V[i + 1]
    
    res = b""
    for i in y:
        res += int(i).to_bytes(4, "big")

    return res

def hex_592(s):

    str = ""
    for i in s:
        str = i + str
    return str

def x(data, key = 5):
    return ''.join([hex(int(x ^ key))[2:] for x in data.encode('utf-8')])


def e(s):
    pieces = []
    for i in range(0, len(s), 57):
        chunk = s[i : i + 57]
        pieces.append(binascii.b2a_base64(chunk))
    return b"".join(pieces).decode()

def sign(data: str, unix: int) -> dict:
    
    buffer_str = (
        str(unix).encode().hex()
    )
    
    return {
        "x-gorgon"  : f'0404{sm3_hash(data.encode("utf-8"), buffer_str).hex()}',
        "x-khronos" : str(unix),
        "x-argus"   : e(hex_592(e(str(x(buffer_str, key=int(unix))).encode())).replace("=", "").encode()).replace("=", "").strip(),
        "x-ladon"   : e(hex_592(e(str(unix).encode())).replace("=", "").encode()).replace("=", "").strip()
    }

if __name__ == "__main__":

    unix = int(time.time())
    x = sign("https://api22-normal-c-alisg.tiktokv.com/aweme/v1/commit/item/digg/?aweme_id=7236119860051184942&enter_from=homepage_hot&friends_upvote=false&type=1&channel_id=0&iid=7252531555938092805&device_id=6953206281364620802&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=300203&version_name=30.2.3&device_platform=android&os=android&ab_version=30.2.3&ssmix=a&device_type=SM-G965N&device_brand=samsung&language=en&os_api=28&os_version=9&openudid=b664e07cdfd60348&manifest_version_code=2023002030&resolution=900*1600&dpi=320&update_version_code=2023002030&_rticket=1688611855592&current_region=US&app_type=normal&sys_region=US&mcc_mnc=46002&timezone_name=Asia%2FCalcutta&carrier_region_v2=310&residence=LK&app_language=en&carrier_region=LK&ac2=wifi5g&uoo=0&op_region=LK&timezone_offset=19800&build_number=30.2.3&host_abi=arm64-v8a&locale=en&region=US&ts=1688611855&cdid=8076ea0e-e896-4f5c-a4d6-be79faf68b49", unix)
    print(json.dumps(x, indent=4))
