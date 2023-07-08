import requests

cookies = {
    'passport_csrf_token': '21e402cb1fd71cde076e56bac8eb4756',
    'passport_csrf_token_default': '21e402cb1fd71cde076e56bac8eb4756',
    'multi_sids': '7077924241736270849%3A028ac7c46b7110e62379700197ecfa1b',
    'cmpl_token': 'AgQQAPNdF-RPsLIHOD9n4904_sfIUSsHP6jZYM7oug',
    'd_ticket': 'fd9269b2a0bb683f1a3a0292b3286dc188992',
    'uid_tt': '19360d1e14c9a6081dfd22a8e783f6ec0179c3f69896f4f498aaaf9225f731d3',
    'uid_tt_ss': '19360d1e14c9a6081dfd22a8e783f6ec0179c3f69896f4f498aaaf9225f731d3',
    'sid_tt': '028ac7c46b7110e62379700197ecfa1b',
    'sessionid': '028ac7c46b7110e62379700197ecfa1b',
    'sessionid_ss': '028ac7c46b7110e62379700197ecfa1b',
    'store-idc': 'useast2a',
    'store-country-code': 'cy',
    'store-country-code-src': 'uid',
    'tt-target-idc': 'useast2a',
    'tt-target-idc-sign': 'L0hiAHmsQsxDyIhH4LbCnaAKKUOeT5T7Ll-DfTLNYk5z3AhoANOca6_ArcgxwMf-oZvbr1vPAJbyqQCnolE1VZCb0wX96dhiZVBMmEwWM7sU3xr4l3SOAIschqv3zSun0xxlpwaXUaKj5PIWiBcl2b50O_8Psea2uACHrAoRPGMm_0_J8y9UOIgxdZV_cPMpRxdjxSzG_YUVHU3m801XvlhJdW9FqhIeMFZYEgsGEINmntYd9gzhVOovL0uPJSheTISrGbh7_guQUE-_-kijPOUMijkBejCbrXb1nECCaVoShRml56oJz5e8PB594DE4JDljsmFl54r7aWNH1UK1Ygkkleiu7Cfo7wptynQZTufNBW6K8it7foBMcUWS5lN5eDqmez__WoZVktAzidgrAn4jFz-yJDNwg0YJZrzN1yoByxqfQLvuYnw_mupQmZR3xYqxoRNwOuQKbLVBT0ov_H9WvoVgTbFqrJPGR2MXBfQF7JVkJ_oHz_mlxD7lltCX',
    'install_id': '7252574786127415067',
    'ttreq': '1$8b1452cbda02ab276c930b864e57b6f0aad84a11',
    'odin_tt': '268d83425a7d69bf86cc398ba363d802f2f3e04cc31cf84a52b2f61290e6af397b3ecd33ef480a4fff01b695e2a03131afbed2ed9cce643315f72c6ce6cd744c36cfca0c5a8c5d278a51a9cc4b57ddc2',
    'msToken': 'EWXSroZaUTHkhxO5Uw2pvfdFYcF_B5R5oiUtQ3tA_tSwZx2MEYXCcxE5spjfgMMNsdhPgRVmJKRlmYwNdeV-Jt5dUTNkWEHSUE6eK2eFkHQ4qZpyW7VdHYtAZA==',
    'sid_guard': '028ac7c46b7110e62379700197ecfa1b%7C1688720421%7C15552000%7CWed%2C+03-Jan-2024+09%3A00%3A21+GMT',
}

headers = {
    # 'accept-encoding': 'gzip',
    'connection': 'Keep-Alive',
    # 'cookie': 'passport_csrf_token=21e402cb1fd71cde076e56bac8eb4756; passport_csrf_token_default=21e402cb1fd71cde076e56bac8eb4756; multi_sids=7077924241736270849%3A028ac7c46b7110e62379700197ecfa1b; cmpl_token=AgQQAPNdF-RPsLIHOD9n4904_sfIUSsHP6jZYM7oug; d_ticket=fd9269b2a0bb683f1a3a0292b3286dc188992; uid_tt=19360d1e14c9a6081dfd22a8e783f6ec0179c3f69896f4f498aaaf9225f731d3; uid_tt_ss=19360d1e14c9a6081dfd22a8e783f6ec0179c3f69896f4f498aaaf9225f731d3; sid_tt=028ac7c46b7110e62379700197ecfa1b; sessionid=028ac7c46b7110e62379700197ecfa1b; sessionid_ss=028ac7c46b7110e62379700197ecfa1b; store-idc=useast2a; store-country-code=cy; store-country-code-src=uid; tt-target-idc=useast2a; tt-target-idc-sign=L0hiAHmsQsxDyIhH4LbCnaAKKUOeT5T7Ll-DfTLNYk5z3AhoANOca6_ArcgxwMf-oZvbr1vPAJbyqQCnolE1VZCb0wX96dhiZVBMmEwWM7sU3xr4l3SOAIschqv3zSun0xxlpwaXUaKj5PIWiBcl2b50O_8Psea2uACHrAoRPGMm_0_J8y9UOIgxdZV_cPMpRxdjxSzG_YUVHU3m801XvlhJdW9FqhIeMFZYEgsGEINmntYd9gzhVOovL0uPJSheTISrGbh7_guQUE-_-kijPOUMijkBejCbrXb1nECCaVoShRml56oJz5e8PB594DE4JDljsmFl54r7aWNH1UK1Ygkkleiu7Cfo7wptynQZTufNBW6K8it7foBMcUWS5lN5eDqmez__WoZVktAzidgrAn4jFz-yJDNwg0YJZrzN1yoByxqfQLvuYnw_mupQmZR3xYqxoRNwOuQKbLVBT0ov_H9WvoVgTbFqrJPGR2MXBfQF7JVkJ_oHz_mlxD7lltCX; install_id=7252574786127415067; ttreq=1$8b1452cbda02ab276c930b864e57b6f0aad84a11; odin_tt=268d83425a7d69bf86cc398ba363d802f2f3e04cc31cf84a52b2f61290e6af397b3ecd33ef480a4fff01b695e2a03131afbed2ed9cce643315f72c6ce6cd744c36cfca0c5a8c5d278a51a9cc4b57ddc2; msToken=EWXSroZaUTHkhxO5Uw2pvfdFYcF_B5R5oiUtQ3tA_tSwZx2MEYXCcxE5spjfgMMNsdhPgRVmJKRlmYwNdeV-Jt5dUTNkWEHSUE6eK2eFkHQ4qZpyW7VdHYtAZA==; sid_guard=028ac7c46b7110e62379700197ecfa1b%7C1688720421%7C15552000%7CWed%2C+03-Jan-2024+09%3A00%3A21+GMT',
    'host': 'api22-normal-c-useast2a.tiktokv.com',
    'multi_login': '1',
    'passport-sdk-version': '19',
    'sdk-version': '2',
    'user-agent': 'com.zhiliaoapp.musically/2023002030 (Linux; U; Android 9; en; SM-A805N; Build/PQ3B.190801.06281541;tt-ok/3.12.13.1)',
    'x-argus': '6fDGlH3NjR6jNAPjdV6+Slh2za+xUu/v7UN4wzquZsZjQHvHIY91rvZPHJnTo9pFv40a6RBgp6JakNsIXXb0BZX5nx1lmailcwZ7CVzGwkYnf57/CIPC8ShFBGxVQXzvO8KZ2JYJHRwPDeHsDNueC+MsX1tgcMqWjooPdMbpBMECTbDfemZo1R5OGWWBcJtmuHKMmMDvBSPbX8AWTTRdYfCfqQCNfR6HiCpeMQSJ4SkX1DpqGCFvBuciHeoT0Ho1fLCXvUilphArPoZ/YsICoTNAFPrO1RkHrwOgt5IcN+xAXc5c2swGioLDl4XYu8kHI4PiXNju1riZ1i7tDqkGH9eCUDZsOg+sSgEvrouDPPJUsFSSHpWo/MLm0x6lCEbP9xbeN/VrSPlOXRcAEImMeYrN6DW8HwOXUffkB8fi3QZ0I9kDmAX/yvSbtE8r3wOpnnRGBMKr8Yu130YDrykngS85CE6RK3dHqI9Fmzwxe41nvmHqaJd7sK7PvMmvEPiuJBc7r1XkxtAc5HPpf3QcTat4H8XjU1kom3Dx/AM5tmJef4pOcEt2GLG8XbNUNA2QUBVXFjW3jiVgHb1zgiIa74iIlXjCsOnbeW8ByS1Bwz3CFncoDTzo7E/RoS9efZZk1I4=',
    'x-bd-client-key': '#wHF0ZPwJW0M5VvzthwNBLbXGs9QAEOUSTcoRfrbTQE5gAHUc+nrFp6mOYLs2WmRf8DxvW32R1YgQl0hs',
    'x-bd-kmsv': '0',
    'x-gorgon': '8404c0404001c777b9b86f1c6c2c98cc244b3df2962690205dec',
    'x-khronos': '1688799225',
    'x-ladon': 'Bu0NXUHsr9XW7mpPDlM2ZJvq7xywREI1DzcogXEVkRGWLV3j',
    'x-ss-req-ticket': '1688799225899',
    'x-tt-dm-status': 'login=1;ct=1;rt=1',
    'x-tt-multi-sids': '7077924241736270849%3A028ac7c46b7110e62379700197ecfa1b',
    'x-tt-store-region': 'cy',
    'x-tt-store-region-src': 'uid',
    'x-tt-token': '03028ac7c46b7110e62379700197ecfa1b034df136bc55f47c17c49dd558e68bf6cf39983d4eb310e502a6eaba66ec7b8122e1d8dd091b258771ac6a78baecb2b0f66a84ecc30b900825eb259f322b8f1d8de8c4f91e0d7bcd0c7f650ad2d42fb9ea4-CkBjYjRmZDllODg2ZTU2YTU3MjQ0MmUwZGYxOTY4ODk5YTYyNzVjMGJjMjg3YmI0ODEzZjIwOGJmYjIyZjE4YmQx-2.0.0',
    'x-vc-bdturing-sdk-version': '2.3.1.i18n',
}

response = requests.get(
    'https://api22-normal-c-useast2a.tiktokv.com/aweme/v1/commit/item/digg/?aweme_id=7251427642245729538&enter_from=homepage_hot&friends_upvote=false&type=1&channel_id=0&iid=7252574786127415067&device_id=7252573733499962922&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=300203&version_name=30.2.3&device_platform=android&os=android&ab_version=30.2.3&ssmix=a&device_type=SM-A805N&device_brand=samsung&language=en&os_api=28&os_version=9&openudid=14ccd7cfca75ec6d&manifest_version_code=2023002030&resolution=900*1600&dpi=320&update_version_code=2023002030&_rticket=1688799225897&current_region=LK&app_type=normal&sys_region=US&mcc_mnc=41301&timezone_name=Asia%2FColombo&carrier_region_v2=413&residence=LK&app_language=en&carrier_region=LK&ac2=wifi5g&uoo=0&op_region=LK&timezone_offset=19800&build_number=30.2.3&host_abi=arm64-v8a&locale=en&region=US&ts=1688799225&cdid=a3c6b461-5d96-4085-8c07-6dcb8f8b9567',
    cookies=cookies,
    headers=headers,
)
