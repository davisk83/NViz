""""
Reference and Guidance: ZeroCrystal @https://myanimelist.net/profile/ZeroCrystal
MyAnimeList API Authorization Documentation: https://myanimelist.net/apiconfig/references/authorization
MyAnimeList API beta Version 2 Documentation: https://myanimelist.net/apiconfig/references/api/v2
"""
import json
import requests
import secrets


CLIENT_ID = 'b0ad0284094c024d3c5d1560b239f2c9'
CLIENT_SECRET = '6763e8659f1b4d0b7a2464ff0537b6927642ae72a1a05e2e0e42da44acc99167'


def get_new_code_verifier() -> str:
    """Generate a code verifier / code challenge which is a high-entropy, cryptographic, random string containing only the characters [A-Z] / [a-z] / [0-9] / "-" / "." / "_" / "~" for the PKCE protocol. (128 Characters)
    
    >>> get_new_code_verifier()
    NklUDX_CzS8qrMGWaDzgKs6VqrinuVFHa0xnpWPDy7_fggtM6kAar4jnTwOgzK7nPYfE9n60rsY4fhDExWzr5bf7sEvMMmSXcT2hWkCstFGIJKoaimoq5GvAEQD8NZ8g
    """
    token = secrets.token_urlsafe(64)
    return token[:128]


def print_new_authorization_url(code_challenge: str):
    """Print the URL needed to authorize the application.

    >>> print_new_authorization_url("NklUDX_CzS8qrMGWaDzgKs6VqrinuVFHa0xnpWPDy7_fggtM6kAar4jnTwOgzK7nPYfE9n60rsY4fhDExWzr5bf7sEvMMmSXcT2hWkCstFGIJKoaimoq5GvAEQD8NZ8g")
    Authorize your application by clicking here: https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id=b0ad0284094c024d3c5d1560b239f2c9&code_challenge=NklUDX_CzS8qrMGWaDzgKs6VqrinuVFHa0xnpWPDy7_fggtM6kAar4jnTwOgzK7nPYfE9n60rsY4fhDExWzr5bf7sEvMMmSXcT2hWkCstFGIJKoaimoq5GvAEQD8NZ8g
    """
    url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={CLIENT_ID}&code_challenge={code_challenge}'
    print(f'Authorize your application by clicking here: {url}\n')


def generate_new_token(authorization_code: str, code_verifier: str) -> dict:
    """Redirect to the webpage specified in the API panel after authorizing the application. The URL will contain a parameter named "code" (the Authorization Code) that is needed to be fed to the application. The parameter is used to send a POST request to get the token and be stored in token.json file.

    >>> generate_new_token(def50200a3ac1767a3843f8ca319216297e47ea031db832eb7e2dfdb7232c74aebfd5e40c4e9dd8ccdb7cac5b186a2d46fa0ffa1d11fb3cfadb6e868f766da339a6f1572e06d8f7940e79e2bc3cf31d2a712fdfdf8312f581a5d0b5e43de96daecaff928d84bc088b001955b52f3ce11851b4b5099f496d079e98b18481b91b1f6a99b3ec93a52a0c51d68c8d8dbcbdbf39289507bc4e3e86994991f3aacf57f3e77a654436474970f5aee757bd61440a103a8afe3a1d3c34e663ad89674ee7b505efecc44147377102e5ac317fdaa3bd55d619e0859f6856fd8c492d5a399be609406b0ca26388a6c45dfd4d58861400055b0bb016b51e7ed8eb7ad359e8ef950d3ae391bbda5a0cebcc5c2a47e9b48eafd1e70f335cb4a925c96c852618707e52e2d9f4b2b401bdab21d83b6089474fa02cc2cb646d29e03f84735416e9a881982e738dac9e90cca445019d4d721022aafe5315083d1913b4b6a57c3954169c7ff133224457f3c7dcc0b203952e34d213a3aa17f0957f2ae747d3684d331019b137062dd3d555fd03dd4abeda0b41787fd9666580be90e935ce1081b12698144ddcfca26f7d39e7afdfa13dc985e0e53c5972d07cf43f1e51712914e24f8e7, NklUDX_CzS8qrMGWaDzgKs6VqrinuVFHa0xnpWPDy7_fggtM6kAar4jnTwOgzK7nPYfE9n60rsY4fhDExWzr5bf7sEvMMmSXcT2hWkCstFGIJKoaimoq5GvAEQD8NZ8g)
    Token generated successfully!
    Token saved in "token.json"
    """
    url = 'https://myanimelist.net/v1/oauth2/token'
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': authorization_code,
        'code_verifier': code_verifier,
        'grant_type': 'authorization_code'
    }

    response = requests.post(url, data)
    response.raise_for_status()  # check whether the request contains errors

    token = response.json()
    response.close()
    print('Token generated successfully!')

    with open('token.json', 'w') as file:
        json.dump(token, file, indent = 4)
        print('Token saved in "token.json"')

    return token


def print_user_info(access_token: str):
    """Print and greet the name of the user by requesting profile information by sending a GET request.

    >>> print_user_info(eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjQ4MWZjNmM3MGNiMjc3MDIzM2RlZTg0ZjQwOGRhZTA1N2M1ZDY0NjRlZTdjZGE1MmQ2NDgxNmZjZGZiNzVmNzAwZjUwZTg0NGEwMDZiNzlkIn0.eyJhdWQiOiJiMGFkMDI4NDA5NGMwMjRkM2M1ZDE1NjBiMjM5ZjJjOSIsImp0aSI6IjQ4MWZjNmM3MGNiMjc3MDIzM2RlZTg0ZjQwOGRhZTA1N2M1ZDY0NjRlZTdjZGE1MmQ2NDgxNmZjZGZiNzVmNzAwZjUwZTg0NGEwMDZiNzlkIiwiaWF0IjoxNjc2MTY3MzM1LCJuYmYiOjE2NzYxNjczMzUsImV4cCI6MTY3ODU4NjUzNSwic3ViIjoiMTE1MDc5ODIiLCJzY29wZXMiOltdfQ.R5IULc4dg1zbjMpSZC8VE1Le3Gfbpy-H2I9IA31cfOP-K6PHFvESZmGWZusbzEfRMqeZybcKDvDxp95fuemcd49KHMVlgvOmmGpj0IbvTp7uRNZEekSxAPg1pjRGiA0Z3wYYjC3UG5i7CirKrvIvp8SZovHleAaPXlVkRSW9O_k70C9vIeTyWMUxFjEri9byXR3b49MhnVY8esjvV2LbXyTYEXsRo4JEP-aO6chDECcQgR8BzP26miFCBHof1IWw79nXcHBVxzsbKpgS121Rg2TWLjfvO8TZfNK-ZjuBzGj3X6UouRNOu59PKbIAkzC-zDw9pMsDw1QWKh4P0M2kpA`)
    >>> Greetings NumzMAL! <<<
    """
    url = 'https://api.myanimelist.net/v2/users/@me'
    response = requests.get(url, headers = {
        'Authorization': f'Bearer {access_token}'
        })
    
    response.raise_for_status()
    user = response.json()
    response.close()

    print(f"\n>>> Greetings {user['name']}! <<<")


if __name__ == '__main__':
    code_verifier = code_challenge = get_new_code_verifier()
    print_new_authorization_url(code_challenge)

    authorization_code = input('Copy-paste the Authorization Code: ').strip()
    token = generate_new_token(authorization_code, code_verifier)

    print_user_info(token['access_token'])