import requests

def fetch_nemo_data(page_index=0):
    """NemoApp API로부터 데이터를 수집합니다."""
    url = "https://www.nemoapp.kr/api/store/search-list"
    
    # docs/nemo_scraping_prompt.md에서 제공된 파라미터
    params = {
        "Subway": "222",
        "Radius": "1000",
        "CompletedOnly": "false",
        "NELat": "37.524082652435375",
        "NELng": "127.04633639319073",
        "SWLat": "37.471760955370655",
        "SWLng": "127.00886288970709",
        "Zoom": "17",
        "SortBy": "29",
        "PageIndex": page_index
    }
    
    # docs/nemo_scraping_prompt.md에서 제공된 헤더
    headers = {
        "referer": "https://www.nemoapp.kr/store",
        "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # items 리스트 반환
        return data.get("items", [])
    except Exception as e:
        print(f"API 요청 중 오류 발생: {e}")
        return []
