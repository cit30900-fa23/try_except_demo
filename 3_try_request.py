import requests

def get_text(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        # print(e)
        return None
    else:
        return response.text

def get_html(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        # print(e)
        return None
    else:
        return response.text

def get_json(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        # print(e)
        return None
    else:
        return response.json()
    
def main():
    x = get_text('https://requestsdemo.sdfkjsdkfsdlkfsdlkfjsdkljfklsd.io/index.txt')
    print(x) if x else print('Error')

    y = get_html('https://requestsdemo.github.io/index.html')
    print(y) if y else print('Error')

    z = get_json('https://requestsdemo.github.io/recipes.json')
    print(z) if z else print('Error')

if __name__ == "__main__":
    main()