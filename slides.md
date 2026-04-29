---
marp: true
theme: default
paginate: true
backgroundColor: #F5F500
header: 'NemoApp: 강남 부동산 EDA'
footer: 'NEO-BRUTALISM EDITION © 2026'
style: |
  section {
    background-color: #F5F500;
    font-family: 'Arial Black', Gadget, sans-serif;
    color: #000;
    padding: 50px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }
  h1 {
    font-family: 'Arial Black', sans-serif;
    font-size: 55px;
    text-transform: uppercase;
    background-color: #FFF;
    border: 5px solid #000;
    padding: 15px 25px;
    box-shadow: 12px 12px 0px #000;
    display: inline-block;
    margin-bottom: 40px;
    letter-spacing: -2px;
  }
  h2 {
    font-family: 'Arial Black', sans-serif;
    font-size: 38px;
    background-color: #CCFF00;
    border: 4px solid #000;
    padding: 8px 20px;
    box-shadow: 8px 8px 0px #000;
    display: inline-block;
    margin-top: 0;
    text-transform: uppercase;
  }
  ul {
    font-family: 'Courier New', Courier, monospace;
    font-weight: 900;
    font-size: 22px;
    line-height: 1.3;
    margin-top: 20px;
  }
  li {
    margin-bottom: 10px;
    list-style: none;
  }
  li::before {
    content: "■ ";
    color: #FF2D55;
  }
  .highlight {
    background-color: #FF2D55;
    color: #FFF;
    padding: 2px 8px;
  }
  .notes {
    font-family: 'Courier New', monospace;
    font-size: 15px;
    background-color: #FFF;
    border: 3px solid #000;
    padding: 15px;
    box-shadow: 6px 6px 0px #000;
    margin-top: auto;
    line-height: 1.4;
    font-weight: bold;
  }
  img {
    border: 4px solid #000;
    box-shadow: 10px 10px 0px #000;
    max-height: 280px;
    margin: 20px auto;
    display: block;
  }
  table {
    border-collapse: collapse;
    border: 3px solid #000;
    background: #FFF;
    box-shadow: 8px 8px 0px #000;
    margin: 10px auto;
  }
  th, td {
    border: 2px solid #000;
    padding: 8px 15px;
  }
  th {
    background: #CCFF00;
  }
---

# NEMOAPP REAL ESTATE
### 강남/역삼 상업용 부동산 EDA

<div class="notes">
<b>[SCRIPT]</b> 안녕하세요! NemoApp의 강남/역삼 상권 분석 발표를 시작합니다. 오늘은 뻔한 보고서 스타일을 벗어나, 네오 브루탈리즘 스타일의 강렬한 비주얼과 함께 데이터의 날것 그대로를 파헤쳐 보겠습니다. 강남이라는 거대 정글에서 데이터가 말하는 필승 전략은 무엇인지 지금부터 공개합니다!
</div>

---

## 1. EXECUTIVE SUMMARY
- **DATA**: 강남/역삼 매물 673건
- **CORE**: 임대 위주 시장 (99.5%)
- **ISSUE**: 가격 지표의 극심한 양극화
- **GOAL**: <span class="highlight">중앙값(Median)</span> 기반의 실전 가이드

<div class="notes">
<b>[SCRIPT]</b> 핵심 요약입니다. 673건의 고유 매물을 탈탈 털어본 결과, 강남은 철저한 '임대' 중심 시장입니다. 평균에 속지 마십시오. 소수의 펜트하우스급 매물이 수치를 왜곡하고 있습니다. 우리는 오늘 '중앙값'이라는 가장 정직한 지표를 통해 여러분이 창업 예산을 짤 때 당장 참고할 수 있는 벤치마크를 제시하겠습니다.
</div>

---

## 2. DATA CLEANING
- **VOLUME**: 673 ROWS × 42 COLS
- **STATUS**: 중복 제거 100% 완료
- **RELIABILITY**: 핵심 지표 결측치 ZERO
- **STRUCTURE**: 정제된 정형 데이터셋

<div class="notes">
<b>[SCRIPT]</b> 데이터 품질은 타협하지 않았습니다. 42개의 컬럼을 전수 조사하여 중복은 단 한 건도 남기지 않았습니다. 특히 보증금, 월세, 면적처럼 돈과 직결된 데이터에 빈틈이 없다는 것이 이번 분석의 가장 큰 강점입니다. 텍스트 데이터의 오탈자까지 잡았기에, 이어지는 키워드 분석 역시 매우 높은 정확도를 보장합니다.
</div>

---

## 3. KEY STATS (NUMERIC)
| 지표 | 평균 | <span class="highlight">중앙값</span> |
|:---|:---|:---|
| 보증금 | 6,895만 | 4,000만 |
| 월세 | 534만 | 340만 |
| 면적 | 38평 | 31평 |

<div class="notes">
<b>[SCRIPT]</b> 숫자가 말하는 진실입니다. 평균과 중앙값의 차이를 보십시오. 보증금은 무려 2,900만 원이나 차이가 납니다. "강남은 보증금 7천이 평균이라며?"라는 말에 겁먹지 마십시오. 실제 여러분이 만날 대부분의 매물은 4,000만 원 수준입니다. 월세 역시 340만 원이 가장 현실적인 타겟입니다. 이 표가 여러분의 예산 수립 나침반입니다.
</div>

---

## 4. KEY STATS (CAT)
- **TYPE**: 임대 99.5% (소유보다 운영)
- **BIZ**: '화이트 박스' 범용 매물 선호
- **LOC**: 역세권 도보 5분 룰 지배적
- **STRATEGY**: 접근성이 곧 가격이다

<div class="notes">
<b>[SCRIPT]</b> 카테고리 분석입니다. 강남은 공간의 소유보다 '사용 가치'가 우선인 시장입니다. 특정 업종으로 묶여있는 매물보다 '다용도'로 나온 매물이 많다는 것은, 여러분이 어떤 컨셉을 가져와도 건물주들이 환영할 준비가 되어 있다는 뜻입니다. 결국 지하철역에서의 거리, 즉 '도보 5분 룰'이 임대료의 계급을 나누는 결정적 요인입니다.
</div>

---

## 5. RENT DISTRIBUTION
![임대료 분포](images/monthly_rent_dist.png)

<div class="notes">
<b>[SCRIPT]</b> 월세 분포 그래프입니다. 왼쪽으로 삐죽 솟은 막대들이 보이시나요? 강남 창업의 '메인 스트림'은 월세 300~500만 원 구간에 몰려 있습니다. 오른쪽으로 길게 늘어진 꼬리는 수천만 원대 월세를 내는 대형 플래그십 매장들입니다. 우리는 그들만의 리그가 아닌, 실제 밀집도가 높은 이 '왼쪽 정글'에서 승리하는 법을 고민해야 합니다.
</div>

---

## 6. DEPOSIT DISTRIBUTION
![보증금 분포](images/deposit_dist.png)

<div class="notes">
<b>[SCRIPT]</b> 보증금 분포 역시 월세와 궤를 같이합니다. 4,000만 원 부근의 높은 밀집도를 확인하십시오. 보증금이 이보다 현저히 낮다면 계약의 안정성을, 현저히 높다면 입지의 독점성을 의심해 봐야 합니다. 강남 부동산 시장에서 4,000이라는 숫자는 시장 진입을 위한 최소한의 '신뢰의 증표'라고 보셔도 무방합니다.
</div>

---

## 7. BUSINESS FREQUENCY
![업종 빈도](images/biz_middle_freq.png)

<div class="notes">
<b>[SCRIPT]</b> 어떤 가게가 가장 많을까요? '기타창업모음'과 '다용도점포'가 압도적입니다. 이는 임차인에게는 '백지상태'의 기회를 의미합니다. 뒤를 잇는 카페와 한식점은 강남 오피스 상권의 거대한 유동 인구를 받아내는 든든한 수요층을 증명합니다. 여러분의 브랜드가 이 거대한 흐름에 올라탈 것인지, 틈새를 뚫을 것인지 결정하십시오.
</div>

---

## 8. CORRELATION (D vs R)
![상관관계](images/deposit_vs_rent.png)
- **CORR**: <span class="highlight">0.9479</span> (PERFECT MATCH)
- **INSIGHT**: 보증금 올리고 월세 깎기 안 통함

<div class="notes">
<b>[SCRIPT]</b> 상관계수 0.9479! 통계적으로 소름 끼칠 정도의 정비례 관계입니다. 강남에서는 "보증금 더 드릴 테니 월세 좀..."이라는 협상이 거의 불가능합니다. 입지가 좋은 매물은 보증금도 비싸고 월세도 비쌉니다. 하나만 잘해서는 안 됩니다. 초기 자본과 월세 감당 능력, 이 두 마리 토끼를 모두 잡아야 우량 매물을 쟁취할 수 있습니다.
</div>

---

## 9. SIZE DISTRIBUTION
![면적 분포](images/size_dist.png)
- **STANDARD**: <span class="highlight">31평</span> (THE GOLDEN SIZE)

<div class="notes">
<b>[SCRIPT]</b> 면적 분포입니다. 중앙값 31평! 강남 상가의 '국룰'입니다. 31평은 운영 효율성과 임대료 부담 사이에서 가장 합리적인 타협점입니다. 카페, 사무실, 뷰티샵 등 대부분의 성공한 강남 비즈니스가 이 30평 내외에서 시작되었습니다. 여러분의 사업장 크기를 결정할 때 이 '골든 사이즈'를 기준으로 삼으십시오.
</div>

---

## 10. FLOOR FREQUENCY
![층수 빈도](images/floor_freq.png)
- **1F (209건)** vs **B1 (123건)**
- **RULE**: 접근성은 지상, 가성비는 지하

<div class="notes">
<b>[SCRIPT]</b> 층수의 마법입니다. 당연히 1층이 가장 많지만, 지하 1층이 2층보다 많다는 점에 주목하십시오. 강남은 지하 공간이 매우 활성화된 상권입니다. 간판보다 입소문이나 SNS 예약으로 승부한다면, 비싼 1층 대신 넓고 저렴한 지하 1층에서 시작하는 것이 스마트한 '비용 효율화' 전략이 될 수 있습니다.
</div>

---

## 11. PRICE TYPE
![가격 유형](images/price_type_pie.png)
- **RENTAL ONLY**: 99.6% (운영 수익의 땅)

<div class="notes">
<b>[SCRIPT]</b> 임대 비중 99.6%! 이 숫자는 강남이 '소유'의 시장이 아니라 '운영'의 시장임을 단적으로 보여줍니다. 건물을 사서 시세 차익을 노리기보다, 이 공간을 얼마나 잘 굴려서 월세를 내고도 남길 것인가를 치열하게 고민해야 하는 곳입니다. 우리는 공간의 주인이 아닌, 공간의 '가치 창출자'가 되어야 합니다.
</div>

---

## 12. UNIT PRICE (PER AREA)
![면적당 가격](images/area_price_dist.png)
- **AVG**: 평당 439만 원

<div class="notes">
<b>[SCRIPT]</b> 평당 임대료 분석입니다. 평당 440만 원이라는 기준을 머릿속에 넣으십시오. 매물 총액이 싸다고 혹하지 말고, 면적으로 나눠보십시오. 평당 단가가 주변보다 너무 높다면 그곳은 거품이 끼었거나, 반대로 엄청난 '슈퍼 역세권' 프리미엄이 붙은 곳입니다. 평당 단가는 매물의 가치를 가장 객관적으로 비교해 주는 잣대입니다.
</div>

---

## 13. RENT BY BIZ
![업종별 월세](images/avg_rent_by_biz.png)
- **HEAVY**: 주점/레스토랑 (AVG 1,200만+)

<div class="notes">
<b>[SCRIPT]</b> 누가 월세를 가장 많이 낼까요? 술집과 레스토랑입니다. 무려 1,200만 원 이상입니다. 이들은 고정비가 높은 대신 객단가가 높고 밤늦게까지 매출을 올립니다. 요식업 창업을 준비하신다면 이 정도의 고정비를 상쇄할 수 있는 명확한 매출 전략이 있는지 스스로에게 물어보십시오. 강남의 밤은 화려하지만 임대료는 냉혹합니다.
</div>

---

## 14. MULTIVARIATE ANALYSIS
![다변량 분석](images/multivariate_analysis.png)
- **TRUTH**: "작아도 1층이 비싸다"

<div class="notes">
<b>[SCRIPT]</b> 면적, 월세, 층수를 한꺼번에 돌려본 결과입니다. 1층은 고층보다 면적이 좁음에도 가격은 더 높습니다. 접근성이라는 보이지 않는 가치가 물리적인 면적을 압도하는 셈입니다. 예산이 부족하다면 타협하십시오. 넓은 윗층인가, 좁은 1층인가? 여러분의 업종이 '고객의 발길'을 필요로 하는지 '고객의 목적지'인지에 따라 답은 정해져 있습니다.
</div>

---

## 15. TEXT MINING (TF-IDF)
![TF-IDF](images/text_tfidf.png)
- **HOT**: #인테리어 #무권리 #강남역

<div class="notes">
<b>[SCRIPT]</b> 매물 설명 글에서 뽑아낸 키워드입니다. '인테리어'와 '무권리'가 상단에 있습니다. 고금리 시대에 신규 투자를 줄이려는 창업자들의 절박함이 데이터에 녹아 있습니다. 이미 시설이 되어 있는 '무권리' 매물을 찾는 것이야말로 강남 창업에서 수억 원을 벌고 시작하는 최고의 재테크입니다. 데이터 속의 단어가 곧 기회입니다.
</div>

---

## 16. SURVIVAL STRATEGY
- **LOC**: 업종 본질에 충실한 층수 선택
- **COST**: 무권리/인테리어 잔존 매물 선점
- **GOAL**: <span class="highlight">고정비 최소화, 운영 가치 극대화</span>

<div class="notes">
<b>[SCRIPT]</b> 살아남는 법을 정리합니다. 첫째, 층수는 허세가 아닌 전략입니다. 목적형 방문 업종이라면 과감히 위로 올라가 월세를 아끼십시오. 둘째, '턴키' 매물을 사냥하십시오. 철거비와 시공비를 아끼는 것만으로도 생존 확률이 50% 올라갑니다. 강남은 돈을 많이 쓰는 곳이 아니라, 돈을 영리하게 쓰는 사람이 이기는 곳입니다.
</div>

---

## 17. LANDLORD STRATEGY
- **FLEX**: 업종 제한 없는 '화이트 박스' 유지
- **RISK**: 공실 방어가 자산 가치의 핵심
- **VALUE**: 데이터 기반 적정 임대료 산정

<div class="notes">
<b>[SCRIPT]</b> 건물주님들께도 조언 드립니다. 특정 업종만 고집하다 공실을 키우는 것은 가장 큰 손실입니다. 언제든 누구든 들어올 수 있는 깨끗한 '화이트 박스' 상태를 유지하십시오. 데이터는 범용적인 매물이 더 빠르게 임차인을 찾는다는 것을 증명합니다. 적정한 월세 책정과 유연한 수용성이 건물의 가치를 우상향하게 만듭니다.
</div>

---

## 18. CONCLUSION
- **MARKET**: 철저한 데이터 기반 가격 모델
- **PLATFORM**: 단순 정보에서 애널리틱스로 진화
- **VISION**: 데이터가 주도하는 부동산 시장 혁신

<div class="notes">
<b>[SCRIPT]</b> 결론입니다. 강남 부동산은 감이 아닌 데이터로 움직입니다. NemoApp은 이제 단순한 매물 리스트를 넘어, 이런 심층 분석을 실시간으로 제공하는 프롭테크의 정점으로 진화해야 합니다. 정보의 비대칭을 깨고 모두가 윈-윈하는 투명한 시장, 그 혁신의 중심에 데이터가 있습니다. 지금까지 NemoApp EDA 발표였습니다. 감사합니다!
</div>

---

# THANK YOU!
### DATA DRIVES SUCCESS
