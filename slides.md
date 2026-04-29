---
marp: true
theme: default
paginate: true
backgroundColor: #F5F500
header: ' '
footer: 'NEMOAPP x NEO-BRUTALISM'
style: |
  @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');
  
  section {
    font-family: 'Courier New', 'Space Mono', monospace;
    background-color: #F5F500;
    padding: 40px;
    color: #000000;
    font-weight: 700;
  }
  
  /* 타일 제목 스타일 */
  h1 {
    font-family: 'Impact', sans-serif;
    font-size: 85px;
    line-height: 0.9;
    color: #000000;
    text-transform: uppercase;
    background: #FF2D55; /* Hot Pink */
    display: block;
    width: fit-content;
    padding: 20px;
    border: 8px solid #000000;
    box-shadow: 15px 15px 0px #000000;
    transform: rotate(-2deg);
    margin-bottom: 60px;
  }
  
  h2 {
    font-family: 'Impact', sans-serif;
    font-size: 55px;
    background: #FFFFFF;
    color: #000000;
    display: inline-block;
    padding: 10px 20px;
    border: 6px solid #000000;
    box-shadow: 10px 10px 0px #000000;
    margin-bottom: 40px;
  }
  
  /* 리스트 박스 */
  ul {
    background: #FFFFFF;
    border: 6px solid #000000;
    box-shadow: 12px 12px 0px #000000;
    padding: 40px 60px;
    list-style: square;
    margin-top: 20px;
  }
  
  li {
    font-size: 30px;
    margin-bottom: 20px;
    color: #000000;
  }
  
  strong {
    background: #00FF00; /* Lime Green */
    padding: 0 10px;
    border: 3px solid #000000;
  }
  
  /* 이미지 스타일링 */
  img {
    border: 8px solid #000000;
    box-shadow: 15px 15px 0px #000000;
    background: #FFFFFF;
    max-height: 400px;
    transform: rotate(1deg);
  }
  
  /* 테이블 */
  table {
    background: #FFFFFF;
    border: 6px solid #000000;
    box-shadow: 12px 12px 0px #000000;
    width: 100%;
    transform: rotate(-1deg);
  }
  
  th {
    background: #00F5FF;
    border: 4px solid #000000;
    padding: 20px;
    font-size: 30px;
  }
  
  td {
    padding: 20px;
    border: 3px solid #000000;
    font-size: 26px;
    text-align: center;
  }
  
  footer {
    background: #000000;
    color: #F5F500;
    font-size: 18px;
    padding: 5px 20px;
    border: none;
  }

  /* 홀수/짝수 슬라이드 배경 반전 */
  section:nth-child(even) {
    background-color: #FF2D55;
  }
  section:nth-child(even) h2 {
    background-color: #00F5FF;
  }
  section:nth-child(even) ul {
    background-color: #F5F500;
  }

  /* 제목 슬라이드 전용 */
  section.title-page {
    background-color: #000000;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  section.title-page h1 {
    background-color: #F5F500;
    font-size: 120px;
    transform: rotate(3deg);
  }
  section.title-page h3 {
    background-color: #00F5FF;
    color: #000000;
    font-size: 40px;
    padding: 10px 30px;
    border: 6px solid #000000;
    box-shadow: 10px 10px 0px #FFFFFF;
    font-family: 'Impact', sans-serif;
  }
---

<!-- _class: title-page -->
# NEMO <br> **EDA**
### DATA DOES NOT LIE.

<!--
[발표자 노트]
진정한 네오브루탈리즘 스타일로 재탄생한 NemoApp 분석 보고서입니다.
규칙을 파괴하는 강렬한 디자인만큼이나 압도적인 데이터 인사이트를 보여드리겠습니다.
-->

---

## EXECUTIVE SUMMARY
- **TARGET**: 강남/역삼역 매물 673건
- **RATIO**: **99.5%** RENTAL MARKET
- **GAP**: EXTREME POLARIZATION
- **ACTION**: USE **MEDIAN**, NOT AVERAGE.

<!--
[발표자 노트]
핵심 요약입니다. 강남은 전쟁터입니다. 임대 시장이 99%를 넘는다는 건 운영 실력 없인 살아남을 수 없다는 뜻이죠. 평균에 속지 마십시오.
-->

---

## DATA INTEGRITY
- **SAMPLES**: 673 UNIQUE DATA
- **QUALITY**: **ZERO** ERROR / NULL
- **PROCESS**: FULLY CLEANED.

<!--
[발표자 노트]
데이터 무결성 검증 완료. 오직 팩트로만 승부합니다.
-->

---

## REAL BENCHMARK
- DEPOSIT: **4,000만 원**
- MONTHLY: **340만 원**
- SIZE: **31평**

<!--
[발표자 노트]
여러분이 진짜로 만날 매물들의 모습입니다. 이 숫자를 머리에 새기십시오. 이게 강남의 진짜 얼굴입니다.
-->

---

## MONTHLY RENT DIST.
![임대료 분포](images/monthly_rent_dist.png)
- **300~500만 원** ZONE IS BLOODY.

<!--
[발표자 노트]
그래프를 보십시오. 왼쪽의 저 거대한 피크가 우리가 싸워야 할 주류 시장입니다.
-->

---

## DEPOSIT DIST.
![보증금 분포](images/deposit_dist.png)
- **4,000만 원** IS THE STANDARD.

<!--
[발표자 노트]
보증금 역시 4천만 원대에 모든 화력이 집중되어 있습니다.
-->

---

## BIZ ECOSYSTEM
1. **GENERAL BIZ** (WHITE-BOX)
2. **MULTI-PURPOSE** (FLEXIBLE)
3. **CAFE/FOOD** (OFFICE TARGET)

<!--
[발표자 노트]
어떤 업종이든 들어올 수 있는 공간이 대세입니다. 강남은 유연함을 원합니다.
-->

---

## CORRELATION (R=0.95)
![상관관계](images/deposit_vs_rent.png)
- DEPOSIT & RENT ARE **BROTHERS**.

<!--
[발표자 노트]
보증금 높여서 월세 깎겠다는 생각은 버리십시오. 강남은 그런 타협을 하지 않습니다.
-->

---

## SIZE SPECTRUM
![면적 분포](images/size_dist.png)
- **31평** IS THE GOLDEN RATIO.

<!--
[발표자 노트]
30평 내외가 가장 효율적인 '스윗 스팟'입니다.
-->

---

## FLOOR PARADOX
![층수 빈도](images/floor_freq.png)
- **B1** > **2F** (VALUE FOR MONEY)

<!--
[발표자 노트]
2층 갈 바엔 지하로 가십시오. 넓고 싼 공간을 찾는 실속파들의 성지입니다.
-->

---

## PRICE PER PYUNG
![면적당 가격](images/area_price_dist.png)
- AVG **440만 원** / PYUNG

<!--
[발표자 노트]
평당 440만 원이라는 기준점을 가지고 매물의 거품을 걷어내십시오.
-->

---

## RENT BY BUSINESS
![업종별 월세](images/avg_rent_by_biz.png)
- **F&B**: KILLING FIXED COSTS.

<!--
[발표자 노트]
음식점 하려면 월 1,100만 원 이상의 월세를 견딜 체력이 있어야 합니다.
-->

---

## MULTIVARIATE ANALYSIS
![다변량 분석](images/multivariate_analysis.png)
- **FLOOR** > SIZE.

<!--
[발표자 노트]
좁아도 1층입니다. 하지만 간판 노출 안 중요하면 층수를 올리십시오.
-->

---

## TEXT MINING (TF-IDF)
1. **LOCATION**: GANGNAM/YEOKSAM
2. **EFFICIENCY**: NO PREMIUM / TURN-KEY

<!--
[발표자 노트]
사람들은 '인테리어'와 '무권리'라는 단어에 지갑을 엽니다. 시설비 폭등 시대의 전략입니다.
-->

---

## STRATEGY: TENANT
- **THINK DIFFERENT**: USE B1/UPPER FLOORS.
- **COST CUT**: FIND TURN-KEY UNITS.
- **STAY REAL**: BEP BASED ON MEDIAN.

<!--
[발표자 노트]
창업자 여러분, 간판 노출 안 중요하면 층수를 올리십시오. 남는 돈으로 마케팅하는 게 이득입니다.
-->

---

## STRATEGY: LANDLORD
- **FLEXIBILITY**: WHITE-BOX IS KING.
- **INFRA**: UPGRADE WATER/ELECTRICITY.
- **DATA**: PROPOSE FAIR RENT.

<!--
[발표자 노트]
임대인 여러분, 공실 낼 바엔 유연해지십시오. 기초 공사만 미리 해둬도 임차인은 줄을 섭니다.
-->

---

<!-- _class: title-page -->
# THANK YOU
### DATA DRIVEN DECISION.
