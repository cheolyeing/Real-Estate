import urllib.request
import xml.etree.ElementTree

URL = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'

SERVICE_KEY = 'I2Rhaz5QabxWRQ6zG46Q%2Fpae4ivSUKRQyo2NF0cIkGRjOdudXni58gPVcgOUOfcU9A9f1fMCenQQ30ckEi5WiQ%3D%3D' #인증키
PAGE_NO = '1' #페이지 번호
NUM_OF_ROWS = '9999' #한 페이지 결과수
LAWD_CD = '11710' #지역코드
DEAL_YMD = '202101' #계약월
QUERY_PARAMS = '?' + 'ServiceKey=' + SERVICE_KEY + \
              '&' + 'pageNo=' + PAGE_NO + \
              '&' + 'numOfRows=' + NUM_OF_ROWS + \
              '&' + 'LAWD_CD=' + LAWD_CD + \
              '&' + 'DEAL_YMD=' + DEAL_YMD

START_YMD = ''
FINISH_YMD = ''

req = urllib.request.Request(URL+QUERY_PARAMS)
with urllib.request.urlopen(req) as response:
    the_page = response.read()

    root_element = xml.etree.ElementTree.fromstring(the_page)
    iter_element = root_element.iter()

    HELIO_CITY = []
    apt = {
        '월': '',
        '일': '',
        '전용면적':'',
        '층': '',
        '아파트' : '',
    }

    INFO = ['월', '일', '전용면적', '층', '아파트']

    for element in iter_element:
        if element.tag == 'item':
            if apt['아파트'] == '헬리오시티':
                HELIO_CITY.append(apt)
            apt = {
                '월': '',
                '일': '',
                '전용면적': '',
                '층': '',
                '아파트': '',
            }
        tag = element.tag
        text = element.text
        if tag in INFO :
            apt[tag] = text

for element in HELIO_CITY :
    print(element)