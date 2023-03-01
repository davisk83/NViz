import json
import requests


def print_top_ranks_anime(access_token: str):
    """
    
    >>> print_top_ranks_anime(eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjQ4MWZjNmM3MGNiMjc3MDIzM2RlZTg0ZjQwOGRhZTA1N2M1ZDY0NjRlZTdjZGE1MmQ2NDgxNmZjZGZiNzVmNzAwZjUwZTg0NGEwMDZiNzlkIn0.eyJhdWQiOiJiMGFkMDI4NDA5NGMwMjRkM2M1ZDE1NjBiMjM5ZjJjOSIsImp0aSI6IjQ4MWZjNmM3MGNiMjc3MDIzM2RlZTg0ZjQwOGRhZTA1N2M1ZDY0NjRlZTdjZGE1MmQ2NDgxNmZjZGZiNzVmNzAwZjUwZTg0NGEwMDZiNzlkIiwiaWF0IjoxNjc2MTY3MzM1LCJuYmYiOjE2NzYxNjczMzUsImV4cCI6MTY3ODU4NjUzNSwic3ViIjoiMTE1MDc5ODIiLCJzY29wZXMiOltdfQ.R5IULc4dg1zbjMpSZC8VE1Le3Gfbpy-H2I9IA31cfOP-K6PHFvESZmGWZusbzEfRMqeZybcKDvDxp95fuemcd49KHMVlgvOmmGpj0IbvTp7uRNZEekSxAPg1pjRGiA0Z3wYYjC3UG5i7CirKrvIvp8SZovHleAaPXlVkRSW9O_k70C9vIeTyWMUxFjEri9byXR3b49MhnVY8esjvV2LbXyTYEXsRo4JEP-aO6chDECcQgR8BzP26miFCBHof1IWw79nXcHBVxzsbKpgS121Rg2TWLjfvO8TZfNK-ZjuBzGj3X6UouRNOu59PKbIAkzC-zDw9pMsDw1QWKh4P0M2kpA)
    """
    url = 'https://api.myanimelist.net/v2/anime/ranking'
    response = requests.get(url, headers = {
        'Authorization': f'Bearer {access_token}'
        })

    response.raise_for_status()
    rankings = response.json()
    response.close()
    
    # print(json.dumps(data, indent=4))

    print("Top 10 Best Anime Series of All Time:")
    for ranking in rankings['data']:
        print(f"-{ranking['node']['title']}")

    print("\nTop 100 Best Anime Series of All Time:")


if __name__ == '__main__':
    with open('token/token.json', 'r') as file:
        token = json.load(file)
        access_token = token["access_token"]

    print_top_ranks_anime(access_token)