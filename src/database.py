import sqlite3
import os
import json

def init_db(db_path, sample_item=None):
    """데이터베이스 및 테이블 초기화 (평탄화된 구조)"""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 기존 테이블 삭제 (스키마 변경을 위해)
    cursor.execute('DROP TABLE IF EXISTS stores')
    
    # 컬럼 생성 로직
    if sample_item:
        columns = []
        for key, value in sample_item.items():
            if isinstance(value, (int, float)):
                col_type = "REAL"
            else:
                col_type = "TEXT"
            columns.append(f'"{key}" {col_type}')
        
        col_string = ", ".join(columns)
        # PK 컬럼명을 row_id로 변경하여 데이터 내 'id' 필드와 충돌 방지
        create_query = f'CREATE TABLE stores (row_id INTEGER PRIMARY KEY AUTOINCREMENT, {col_string}, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'
    else:
        # 기본 구조 (데이터가 없을 때)
        create_query = 'CREATE TABLE stores (row_id INTEGER PRIMARY KEY AUTOINCREMENT, store_id TEXT, item_data TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'
    
    cursor.execute(create_query)
    conn.commit()
    return conn

def save_items(conn, items):
    """수집된 아이템 리스트를 평탄화하여 DB에 저장"""
    if not items:
        return 0
        
    cursor = conn.cursor()
    count = 0
    
    # 첫 번째 아이템의 키를 기준으로 컬럼 추출
    keys = list(items[0].keys())
    placeholders = ", ".join(["?"] * len(keys))
    col_names = ", ".join([f'"{k}"' for k in keys])
    
    query = f'INSERT INTO stores ({col_names}) VALUES ({placeholders})'
    
    for item in items:
        values = []
        for key in keys:
            val = item.get(key)
            # 리스트나 딕셔너리는 JSON 문자열로 저장
            if isinstance(val, (list, dict)):
                values.append(json.dumps(val, ensure_ascii=False))
            else:
                values.append(val)
        
        try:
            cursor.execute(query, values)
            count += 1
        except Exception as e:
            print(f"Error saving item: {e}")
            
    conn.commit()
    return count
