import urllib
import urllib.error
import urllib.request

try:
    print('Site\t\t\t\tAccessible?\tError')
    print('=' * 90)
    url = ['https://www.pudim.com.br']
    urllib.request.urlopen(url[0])

except urllib.error.URLError as errors:
    print(f'\033[0;31m{url[0]}\tNo\t\t{errors.reason}\033[m')

else:
    print(f'\033[0;33m{url[0]}\tYes\t\tNone\033[m')
