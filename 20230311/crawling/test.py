import requests
from bs4 import BeautifulSoup
import pandas as pd


def has_id(tag):
    return tag.has_attr('id')

#  보고서 번호 확인
start_date_arr=['20000101','20030101','20060101','20090101','20120101','20150101','20180101','20210101']
end_date_arr=['20021231','20051231','20081231','20111231','20141231','20171231','20201231','20230308']


for i in range(len(start_date_arr)):
    current_page = 1
    end_page = 100
    start_date, end_date = start_date_arr[i], end_date_arr[i]
    result_cnt = 0
    total = 0
    result = []
    rcp_num = []                # 보고서 번호 모은 목록

    while current_page <= end_page:
        print("===================page : ", current_page)
        url = f'https://dart.fss.or.kr/dsab007/detailSearch.ax?currentPage={current_page}&maxResults=100&maxLinks=10&sort=rpt&series=asc&reportNamePopYn=Y&option=report&startDate={start_date}&endDate={end_date}&corporationType=P&finalReport=recent&publicType=A001&publicType=A002&publicType=A003'        # A001 사업보고서, A002 반기보고서, A003 분기보고서

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        if current_page == 1:
            # 페이지 수 확인
            temp = str(soup.find("div", class_='psWrap').find_all("div"))
            end_page = int(temp[temp.find("/")+1:temp.find("]")])
            print("end_page : ", end_page)

            # 검색 결과 갯수 확인
            result_cnt = temp[temp.find("[총 ") + 3:temp.find("건]")]
            result_cnt = list(result_cnt)
            result_cnt.remove(',')
            result_cnt = int(''.join(s for s in result_cnt))
            print("result_cnt :", result_cnt)

        # 기업 보고서 확인
        search_list = soup.find("tbody", id='tbody').find_all(has_id)
        for s in search_list:
            # print(s['id'][2:])
            rcp_num.append(s['id'][2:])

        print(len(search_list))
        total += len(search_list)
        current_page += 1

    data = {"rcp_num" : rcp_num}
    df = pd.DataFrame(data)
    df.to_csv(f'{start_date}-{end_date}.csv', index=False, encoding = "UTF-8")
    print("생성 완료")

    continue
