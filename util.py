import time

from network.http_client import client

__last_time_kakao_public_key = time.time() - 36000
__kakao_public_key = []


async def kakao_public_key():
    global __last_time_kakao_public_key, __kakao_public_key
    if __last_time_kakao_public_key + 36000 < time.time():
        response = await client.get("https://kapi.kakao.com/v1/user/access_token_info")
        __kakao_public_key = [key["kid"] for key in response.json().get("keys")]
        __last_time_kakao_public_key = time.time()
    return __kakao_public_key
