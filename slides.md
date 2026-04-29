---
marp: true
theme: default
paginate: true
backgroundColor: #ffffff
header: ' '
footer: 'NEMOAPP: REAL ESTATE EDA'
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Pretendard:wght@400;700;900&display=swap');
  
  section {
    font-family: 'Pretendard', 'Inter', sans-serif;
    background-color: #FFD600; /* 네오브루탈리즘 대표 컬러 (옐로우) */
    padding: 50px;
    color: #000000;
  }
  
  /* 전역 네오브루탈리즘 스타일링 */
  h1 {
    font-size: 70px;
    font-weight: 900;
    color: #000000;
    text-transform: uppercase;
    background: #FF90E8; /* 핑크 포인트 */
    display: inline-block;
    padding: 10px 20px;
    border: 5px solid #000000;
    box-shadow: 10px 10px 0px #000000;
    margin-bottom: 40px;
  }
  
  h2 {
    font-size: 45px;
    font-weight: 900;
    background: #00F5FF; /* 시안 포인트 */
    display: inline-block;
    padding: 5px 15px;
    border: 4px solid #000000;
    box-shadow: 6px 6px 0px #000000;
    margin-bottom: 30px;
  }
  
  ul {
    background: #ffffff;
    border: 4px solid #000000;
    box-shadow: 8px 8px 0px #000000;
    padding: 30px 50px;
    list-style-type: '👉 ';
  }
  
  li {
    font-weight: 700;
    font-size: 26px;
    margin-bottom: 15px;
  }
  
  strong {
    color: #000000;
    background: #FF90E8;
    padding: 0 5px;
    border: 2px solid #000000;
  }
  
  img {
    border: 5px solid #000000;
    box-shadow: 12px 12px 0px #000000;
    background: white;
    max-height: 400px;
    margin-top: 20px;
  }
  
  table {
    background: #ffffff;
    border: 4px solid #000000;
    box-shadow: 10px 10px 0px #000000;
    width: 100%;
  }
  
  th {
    background: #00F5FF;
    border-bottom: 4px solid #000000;
    padding: 15px;
    font-weight: 900;
  }
  
  td {
    padding: 15px;
    border-right: 2px solid #000000;
    font-weight: 700;
  }
  
  footer {
    font-weight: 900;
    color: #000000;
    background: #ffffff;
    border: 2px solid #000000;
    padding: 5px 10px;
  }

  /* 특정 슬라이드 배경색 변화 */
  section:nth-child(even) {
    background-color: #00F5FF;
  }
  section:nth-child(even) h1 {
    background-color: #FFD600;
  }
  section:nth-child(even) h2 {
    background-color: #FF90E8;
  }
  
  section.title-slide {
    background-color: #FF90E8;
    text-align: center;
  }
  section.title-slide h1 {
    background-color: #FFD600;
  }
---

<!-- _class: title-slide -->
# NemoApp <br> **Real Estate**
### 데이터로 찢어버리는 강남 상권

<!--
[발표자 노트]
안녕하세요. 네오브루탈리즘 스타일로 강렬하게 준비한 NemoApp 데이터 분석 보고서입니다. 
기존의 지루한 디자인에서 벗어나 데이터의 강력한 메시지를 시각적으로도 극대화했습니다. 
바로 본론으로 들어가겠습니다.
-->

---

## 1. Executive Summary
- **대상**: 강남/역삼역 매물 673건
- **구조**: **99.5%**가 임대 시장 지배
- **현상**: 극단적 양극화 (Winner takes all)
- **제언**: **중앙값** 기반의 현실적 전략

<!--
[발표자 노트]
핵심 요약입니다. 강남은 전쟁터입니다. 임대 시장이 99%를 넘는다는 건 운영 실력 없인 살아남을 수 없다는 뜻이죠. 평균에 속지 마세요. 우리는 오늘 가장 리얼한 숫자인 중앙값에 집중할 겁니다.
-->

---

## 2. 데이터 무결성
- **표본**: 673건 (42개 변수)
- **품질**: 중복/결측치 **Zero**
- **정제**: 위치 및 업종 표준화 완료

<!--
[발표자 노트]
분석의 재료는 완벽합니다. 중복과 빈틈을 모두 메운 고품질 데이터로 도출한 결과입니다.
-->

---

## 3. 리얼 벤치마크
- **보증금**: **4,000만 원**
- **월 임대료**: **340만 원**
- **전용면적**: **31평**

<!--
[발표자 노트]
여러분이 진짜로 만날 매물들의 모습입니다. 이 숫자를 머리에 새기세요. 이게 강남 상권의 '진짜' 기준입니다.
-->

---

## 4. 월세 분포 현황
![임대료 분포](images/monthly_rent_dist.png)
- **300~500만 원** 구간에 미친 듯이 몰려있음

<!--
[발표자 노트]
그래프를 보세요. 왼쪽의 저 거대한 막대가 우리가 싸워야 할 주류 시장입니다.
-->

---

## 5. 보증금 분포 현황
![보증금 분포](images/deposit_dist.png)
- **4,000만 원** 라인이 무너질 수 없는 벽

<!--
[발표자 노트]
보증금 역시 4천만 원대에 모든 화력이 집중되어 있습니다.
-->

---

## 6. 업종 생태계 구조
1. **기타창업모음** (화이트박스 선호)
2. **다용도점포** (무한 변신 가능)
3. **카페/한식** (직장인 타겟)

<!--
[발표자 노트]
어떤 업종이든 들어올 수 있는 공간이 대세입니다. 강남은 유연함을 원합니다.
-->

---

## 7. 가격 상관관계 (R=0.95)
![상관관계](images/deposit_vs_rent.png)
- 보증금과 월세는 **형제** (둘 다 같이 오름)

<!--
[발표자 노트]
보증금 높여서 월세 깎겠다는 생각은 버리세요. 강남 우량 매물은 그런 타협을 하지 않습니다.
-->

---

## 8. 전용면적 스펙트럼
![면적 분포](images/size_dist.png)
- **31평**이 공간의 황금비율

<!--
[발표자 노트]
30평 내외가 가장 효율적이고 매물이 풍부한 '스윗 스팟'입니다.
-->

---

## 9. 층수의 역설
![층수 빈도](images/floor_freq.png)
- **지하 1층**의 강력한 가성비 수요

<!--
[발표자 노트]
2층 갈 바엔 지하로 가세요. 넓고 싼 공간을 찾는 실속파들의 성지입니다.
-->

---

## 10. 평당 단가 프리미엄
![면적당 가격](images/area_price_dist.png)
- 평균 평당 **440만 원**

<!--
[발표자 노트]
평당 440만 원이라는 기준점을 가지고 매물의 거품을 걷어내십시오.
-->

---

## 11. 업종별 월세 부담
![업종별 월세](images/avg_rent_by_biz.png)
- **F&B**: 살인적 고정비 감내 중

<!--
[발표자 노트]
음식점 하려면 월 1,100만 원 이상의 월세를 견딜 체력이 있어야 합니다.
-->

---

## 12. 다변량 분석 결과
![다변량 분석](images/multivariate_analysis.png)
- **층수**가 면적보다 비싸다

<!--
[발표자 노트]
좁아도 1층입니다. 하지만 목적형 방문 업종이라면 고층으로 도망가서 면적을 확보하세요.
-->

---

## 13. 마케팅 키워드
1. **역세권**: 강남/역삼 무조건 강조
2. **비용**: 인테리어/무권리에 열광

<!--
[발표자 노트]
사람들은 '인테리어'와 '무권리'라는 단어에 지갑을 엽니다. 시설비 폭등 시대의 전략입니다.
-->

---

## 14. 임차인 필승 전략
- **역발상**: 간판 필요 없으면 지하/고층 선점
- **실속**: 무권리 턴키 매물 죽어라 찾기
- **기준**: 보증금 4천, 월세 340 고수

<!--
[발표자 노트]
창업자 여러분, 간판 노출 안 중요하면 층수를 올리세요. 남는 돈으로 마케팅하는 게 이득입니다.
-->

---

## 15. 임대인 운영 전략
- **유연성**: 어떤 업종이든 들어오게 하라
- **인프라**: 수도/전기 미리 뚫어두기
- **합리성**: 데이터로 납득할 임대료 제시

<!--
[발표자 노트]
임대인 여러분, 공실 낼 바엔 유연해지세요. 기초 공사만 미리 해둬도 임차인은 줄을 섭니다.
-->

---

<!-- _class: title-slide -->
# 감사합니다
### NEMOAPP DATA PROJECT
