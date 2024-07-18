import pandas as pd
import requests
import xml.etree.ElementTree as ET

kopis_api_key = 'c16e37f36c9c4109b6e069f6357022f4'
seoul_code = '11'

def extract_performance_data(url):
    params = {
        'service': kopis_api_key,
        'stdate': '20240717',
        'eddate': '20240815',
        'cpage': '1',
        'rows': '3000',
        'signgucode': seoul_code
    }
    return requests.get(url=url, params=params)


def extract_facilities_data(url):
    params = {
        'service': kopis_api_key,
        'cpage': '1',
        'rows': '3000',
        'signgucode': seoul_code
    }
    return requests.get(url=url, params=params)

def parse_perform_data(xml_string):
    xml_root = ET.fromstring(xml_string)
    all_data = []
    for db in xml_root.findall('db'):
        row = {
            'mt20id': db.find('mt20id').text,
            'prfnm': db.find('prfnm').text,
            'prfpdfrom': db.find('prfpdfrom').text,
            'prfpdto': db.find('prfpdto').text,
            'fcltynm': db.find('fcltynm').text,
            'poster': db.find('poster').text,
            'genrenm': db.find('genrenm').text,
            'openrun': db.find('openrun').text,
            'prfstate': db.find('prfstate').text,
        }
        all_data.append(row)
    return pd.json_normalize(all_data)

def parse_fest_data(xml_string):
    xml_root = ET.fromstring(xml_string)
    all_data = []
    for db in xml_root.findall('db'):
        row = {
            'mt20id': db.find('mt20id').text,
            'prfnm': db.find('prfnm').text,
            'prfpdfrom': db.find('prfpdfrom').text,
            'prfpdto': db.find('prfpdto').text,
            'fcltynm': db.find('fcltynm').text,
            'poster': db.find('poster').text,
            'genrenm': db.find('genrenm').text,
            'prfstate': db.find('prfstate').text,
            'festival' : db.find('festival').text
        }
        all_data.append(row)
    return pd.json_normalize(all_data)

def parse_facility_data(xml_string):
    xml_root = ET.fromstring(xml_string)
    all_data = []
    for db in xml_root.findall('db'):
        row = {
            'fcltynm': db.find('fcltynm').text,
            'mt10id': db.find('mt10id').text,
            'mt13cnt': db.find('mt13cnt').text,
            'fcltychartr': db.find('fcltychartr').text,
            'sidonm': db.find('sidonm').text,
            'gugunnm': db.find('gugunnm').text,
            'opende': db.find('opende').text,
        }
        all_data.append(row)
    return pd.json_normalize(all_data)

kopis_perform_url = "http://kopis.or.kr/openApi/restful/pblprfr"
response = extract_performance_data(kopis_perform_url)
df = parse_perform_data(response.text)
print(df)
# df.to_csv('seoul_performances.csv', index=False)
# kopis_fest_url = "http://kopis.or.kr/openApi/restful/prffest"
# response = extract_performance_data(kopis_fest_url)
# df = parse_fest_data(response.text)
# df.to_csv('seoul_today_festivals.csv', index=False)
# kopis_faciliteis_url = "http://kopis.or.kr/openApi/restful/prfplc"
# response = extract_facilities_data(kopis_faciliteis_url)
# df = parse_facility_data(response.text)
# df.to_csv("seoul_performance_facilities.csv", index=False)