import os
import time
import random
from database import init_db, save_items
from nemo_scraper import fetch_nemo_data

def main():
    # 경로 설정 (상대 경로 사용)
    db_path = os.path.join("data", "nemo_data.db")
    
    print("NemoApp 전체 데이터 수집을 시작합니다...")
    
    page_index = 0
    total_saved = 0
    db_initialized = False
    conn = None
    
    while True:
        print(f"페이지 {page_index} 수집 중...")
        items = fetch_nemo_data(page_index=page_index)
        
        if not items:
            print("더 이상 수집할 데이터가 없습니다. 루프를 종료합니다.")
            break
            
        print(f"페이지 {page_index}: {len(items)}개의 아이템을 수집했습니다.")
        
        # 첫 페이지 수집 시 DB 초기화 (스키마 생성)
        if not db_initialized:
            conn = init_db(db_path, sample_item=items[0])
            db_initialized = True
        
        # 데이터 저장
        saved_count = save_items(conn, items)
        total_saved += saved_count
        print(f"현재까지 총 {total_saved}개의 데이터 저장 완료.")
        
        # 다음 페이지로
        page_index += 1
        
        # 서버 부하 방지를 위한 랜덤 지연 (1~2초)
        time.sleep(random.uniform(1.0, 2.0))
    
    if conn:
        conn.close()
    
    print(f"전체 작업이 완료되었습니다. 총 수집 데이터: {total_saved}개")

if __name__ == "__main__":
    main()
