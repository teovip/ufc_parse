import requests
import json
import os

cookies = {
    '_cfuvid': 'vTRmaXFZMDbHdXNfrPYz1ybcj2IeZ5ulAEf6mily1SM-1721732798299-0.0.1.1-604800000',
    '__cf_bm': 'kRVc7z7ldcQY2fHx7uOuVBDWnGv83AJlDhLjK9yaNvg-1721755021-1.0.1.1-Y7Vj8hPtfSqnSTz_14KPEUtnVYmdh1d6YGOJMZlBw2O_3ILgKEMb5gvWmS4D4KJVofCFG8QYWT9uE6iO9sdoeiIf2rtJGRmlJJ6RRV1Rp_k',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9,es;q=0.8',
    'client-sdk': 'ANSWERS_CORE=1.6.0, ANSWERS_THEME=1.29.0, ANSWERS_SEARCH_UI_SDK=v1.14.3',
    # 'cookie': '_cfuvid=vTRmaXFZMDbHdXNfrPYz1ybcj2IeZ5ulAEf6mily1SM-1721732798299-0.0.1.1-604800000; __cf_bm=kRVc7z7ldcQY2fHx7uOuVBDWnGv83AJlDhLjK9yaNvg-1721755021-1.0.1.1-Y7Vj8hPtfSqnSTz_14KPEUtnVYmdh1d6YGOJMZlBw2O_3ILgKEMb5gvWmS4D4KJVofCFG8QYWT9uE6iO9sdoeiIf2rtJGRmlJJ6RRV1Rp_k',
    'origin': 'https://answers-embed-client.ufc.com.pagescdn.com',
    'priority': 'u=1, i',
    'referer': 'https://answers-embed-client.ufc.com.pagescdn.com/',
    'sec-ch-ua': '"Chromium";v="124", "YaBrowser";v="24.6", "Not-A.Brand";v="99", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36',
}

n = 21

for offset in range (0, n+1, 21):

    n += n
    params = {
    'experienceKey': 'answers-en',
    'api_key': '850a88aeb3c29599ce2db46832aa229f',
    'v': '20220511',
    'version': 'PRODUCTION',
    'locale': 'en',
    'input': '',
    'verticalKey': 'athletes',
    'limit': '21',
    'offset': offset,
    'retrieveFacets': 'true',
    'facetFilters': '{}',
    'session_id': '8cedf456-efd2-4848-9cf9-5a3f8c330774',
    'sessionTrackingEnabled': 'true',
    'sortBys': '[]',
    'referrerPageUrl': 'https://www.ufc.com/',
    'source': 'STANDARD',
    'jsLibVersion': 'v1.14.3',
}


    response = requests.get(
    'https://liveapi.yext.com/v2/accounts/me/answers/vertical/query',
    params=params,
    cookies=cookies,
    headers=headers,
)

    if response.status_code == 200:
        info = response.json()
        r = info['response']
        results = r['results']
        results_Lenth = len(results)
        #print(results_Lenth)
        if results_Lenth > 0:
            for data in range(results_Lenth):
                data_fighter = results[data]['data']
                
                if 'c_photo' in data_fighter:

                    c_photo = data_fighter['c_photo']
                    url = c_photo['url']
                    #print(url)
                    photo_response = requests.get(url, headers = headers)
                    fighter_name = data_fighter['name'].lower().replace(' ', '_')


                    if photo_response.status_code == 200:

                        filename = os.path.basename(fighter_name) + '.png'
                        save_path = r'C:\Users\showc\Documents\ufc' #change to your directory
                        with open(os.path.join(save_path, filename), 'wb') as f:
                            f.write(photo_response.content)
                        #print(filename)

                else:
                    print('url not found')        
            #url = c_photo['url']
            #print(url)
        else:
            print('no data in results') 
            break
    else:
        print("we've got blocked", response.status_code, 'error')
    continue
print('done, lets fight') 