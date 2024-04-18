# Language brute forcing script
# Example 'http://localhost:3000/assets/i18n/da_DK.json'
import string

import requests

def main():
    for first_letter in string.ascii_lowercase:
        print(f'Checking for {first_letter}')
        for second_letter in string.ascii_lowercase:
            for first_letter1 in string.ascii_uppercase:
                for second_letter1 in string.ascii_uppercase:
                    lang = first_letter + second_letter + '_' + first_letter1 + second_letter1
                    url = f'http://localhost:3000/assets/i18n/{lang}.json'
                    if '</html>' not in requests.get(url).text:
                        print(f'Language found: {lang}')


if __name__ == "__main__":
    main()
