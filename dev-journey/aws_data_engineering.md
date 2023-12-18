Data structures, data modeling, sampling techniques using git, a review of the SQL 를 우선 배울거다.


## Types of Data
- Structured    (구조화)
- Unstructured  (비구조화)
- Semi-Structured   (반구조화)

### Structured Data
일반적으로 관계형 DB(Relational Database)에서 볼 수 있는 특정 방식이나 스키마로 구성된 데이터를 말함.  
구조화된 데이터는 쉽게쿼리할 수 있고(Easily queryable) 행과 열로 구성됐으며(Organized in rows and columns) 일관된 구조를(Has a consistent structure) 가지고 있다. 즉, 이미 데이터 클리닝이 된 상태다. 주로 CSV 파일, 엑셀 스프레드시트들을 예로 들 수 있다.

### Unstructured Data
정해진 구조나 스키마가 없는 데이터다. 쿼리를 하기전에 무슨 데이터인지 파악해야하는 데이터 덩어리일 뿐이다.  
전처리 없이는 쿼리하기 힘들고 매우 다양한 포맷의 데이터들이 있일 수도 있다. 텍스트파일, 이미지, 비디오, 오디오, 이메일 등등 다양한 데이터가 여기에 속한다.  

### Semi-Structured Data
Structured Data와 Unstructured Data 사이의 데이터로 완전히 체계화되지 않은 데이터다.  
특정 방식으로 태그되거나 카테고라이즈됐을 수 있고, 구조화된 데이터보다 유연하나 비구조화 데이터보단 덜 혼란스럽다고 말할 수 있다. 한 파일안에 다양한 종류의 스키마를 가질 수 있는 XML, JSON이 대표적인 예시다. 스키마가 일관되진 않더라도 존재는 하기 때문. 그리고 반구조화된 이메일 헤더도 있다. 날짜, 주제, 로그파일 등도 포함될 수 있다. 특히 로그파일은 프로그램마다 다른 형식이고 누락된 데이터도 있을 수 있기 때문에 일관되지 않다. 

<br>

## Properties of Data
- Volume
- Velocity
- Variety
- $+a$ veracity

### Volume
볼륨은 말 그대로 얼마나 크고 많은지에 대한거다. 데이터의 양이나 크기가 얼마나 되는지에 따라 데이터를 저장하고 처리하는 방법에 영향을 미친다. 예를 들어 꽤나 큰 업체라면 수 페타바이트에 달하는 정보가 생길텐데 이를 다룰 때는 분산 및 병렬처리를 고려해야 할 수 있다.
볼륨은 데이터 엔지니어링 파이프라인을 어떻게 만들지에 대해 중요한 역할을 한다.

### Velocity
새로운 데이터가 생성되고 수집되고 처리되는 속도를 말한다.

### Variety
서로 다른 타입, 구조, 출처를 말한다. 서로 다른 타입 즉, 구조화, 비구조화, 반구조화 데이터를 어떻게 섞을 지. 때문에 Variety는 어떻게 저장할지 문제해결을 위해 다양한 구조의 쿼리를 어떻게 통합할지 등을 고민해봐야 한다.

<br>

## Data Warehouses vs. Data Lakes