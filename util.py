import time

from network.http_client import client

__last_time_kakao_public_key = time.time() - 3600
__kakao_public_key = {}


async def kakao_public_key():
    global __last_time_kakao_public_key, __kakao_public_key
    if __last_time_kakao_public_key + 3600 < time.time():
        response = await client.get("https://kauth.kakao.com/.well-known/jwks.json")
        __kakao_public_key = response.json()
        __last_time_kakao_public_key = time.time()
    return __kakao_public_key
