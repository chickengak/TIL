# MongoDB
MongoDB는 강력한 NoSQL 데이터베이스로, 유연한 스키마, 확장성, 고성능을 제공하는 특징을 가지고 있다. 전통적인 관계형 데이터베이스와 다르게, MongoDB는 비관계형 데이터를 저장하고, JSON과 유사한 BSON(Binary JSON) 형식을 사용하여 데이터를 저장한다. 이러한 특성 때문에, 대규모 데이터 세트를 다루고, 빠르게 진화하는 데이터 모델을 가진 애플리케이션에 적합함.

## MongoDB의 주요 특징
1. 문서 지향적 저장: MongoDB는 '문서(document)'라고 부르는 데이터 구조를 사용합니다. 이 문서는 JSON과 유사한 BSON 형식으로 저장되며, 다양한 데이터 유형(텍스트, 숫자, 배열, 객체 등)을 포함할 수 있습니다. 문서는 SQL 데이터베이스의 '레코드'와 유사하지만, 훨씬 더 유연한 데이터 모델을 제공합니다. (BSON: https://bsonspec.org/ )

2. 스키마리스: MongoDB 컬렉션은 고정된 스키마를 갖지 않습니다. 즉, 동일한 컬렉션 내의 문서들이 서로 다른 구조를 가질 수 있습니다. 이는 데이터베이스를 디자인하고 사용하는 데 있어 유연성을 제공하며, 애플리케이션의 요구사항이 변경될 때 데이터베이스를 쉽게 수정할 수 있게 해줍니다.

3. 확장성: MongoDB는 수평적 확장성을 지원합니다. 데이터의 양이 증가하면, 샤딩(sharding)을 통해 데이터를 여러 서버에 분산시킬 수 있습니다. 이를 통해 애플리케이션은 더 많은 트래픽과 데이터를 처리할 수 있게 됩니다.

4. 고성능: 인덱싱, 샤딩, 복제 등의 기능을 통해 고성능을 제공합니다. 인덱스를 활용하면 빠른 데이터 조회가 가능하며, 복제를 통해 데이터의 안정성과 가용성을 높일 수 있습니다. 샤딩을 통해 대규모 데이터셋을 효과적으로 관리할 수 있습니다.

5. 안정성과 내구성: 데이터 복제(replication) 기능을 통해 데이터의 안정성을 보장합니다. 복제 세트(replica set)는 동일한 데이터의 복사본을 여러 서버에 분산시켜, 하나의 서버에 문제가 발생해도 데이터에 지속적으로 접근할 수 있도록 합니다.

6. 집계 프레임워크: MongoDB는 강력한 집계 프레임워크를 제공합니다. 이를 통해 데이터를 처리하고, 분석하여 복잡한 질의를 실행할 수 있습니다. MapReduce, 집계 파이프라인 등 다양한 도구를 사용하여 데이터를 집계하고 분석할 수 있습니다.

db.jstest.insertOne({'name': '서강준', 'handsome': 100});

show dbs;

use [db이름];

show collections;
 - insert 할 때, 자동으로 만들어짐.

db.multi.insertOne(
{'name': 'hong-gd', 'class': 'de', 'midterm': {'kor': 100, 'eng': 60, 'math':80}});

var lee = {'name': 'lee-ss', 'midterm': {'kor': 70, 'eng': 90, 'mat': 100}, 'final': {'kor': 80, 'eng': 70, 'mat': 100, 'sci': 100}, 'class': 'ds'}
db.multi.insertOne(lee);

db.multi.insertMany([
... lee,
... {'name': 'kim', 'class':'de', 'kor':100, 'eng':100, 'mat': 50},
... {'name': 'kang', 'class': 'ds', 'kor': 80, 'eng': 50, 'mat': 70},
... {'name': 'you', 'class': 'de', 'kor': 96, 'eng': 40, 'mat': 100},
... ])


db.multi.find({조건}, {출력하고 싶은 필드});
select name, age from multi where class = 'ds';
db.multi.find({class:'ds'}, {'name': 1,'age': 1});

db.multi.find({}, {'name': 1});
db.multi.find({}, {'_id': 0, name: 1});
db.multi.find({}, {'midterm': 1});
db.multi.find({'class': 'de'});

Q. midterm이라는 field가 존재하고 영어가 60점 이상인 document들만 출력
db.multi.find({'midterm': {$exists: true}, 'midterm.eng': {$gte: 60}});
$gt, $gte, $lt, $lte, $eq, $ne, $in, $nin

Q. select * from multi where kor < 100 and math >= 60;
db.multi.find({'midterm.kor': {$lt: 100}, 'midterm.mat': {$gte: 60}});

Q. select * from multi where name like '%k%'
db.multi.find({'name': /k/});
db.multi.find({'name': {$regex: 'k'}});


db.multi.find().sort({'name': 1})       오름차순 정렬
db.multi.find().sort({'name': -1})      내림차순 정렬
db.multi.find().sort({'name': -1}).sort({'class': 1}).limit(2).skip(1)

db.multi.update({'name': /hong/}
~~~

Q. midterm 필드가 존재하는 documnet들의 class를 'graduated'로 바꾸기.
db.multi.updateMany({'midterm': {$exists: true}}, {$set:{'class': 'graduated'}});

// array
db.myfriends.insertOne({'name': '아이언맨', buddy: ['토르', '헐크', '호크아이']})
db.myfriends.insertOne({'name': '슈퍼맨', buddy: ['배트맨', '원더우먼', '아쿠아맨', '조커']})

db.myfriends.updateOne({'name': '아이언맨'}, {$push: {'buddy': {$each: ['캡틴아메리카', '블랙위도우']}}})

db.myfriends.updateOne({'name': '슈퍼맨'}, {$pop: {'buddy': 1}})
db.myfriends.updateOne({'name': '슈퍼맨'}, {$pull: {'buddy': 1}})    ?


db.multi.insertMany([
    {name:'hong-gd', kor:65, eng:60, math:100},
    {name:'kim-sd', kor:100, eng:100, math:40},
    {name:'you-js', kor:96, eng:40, math:100}
])

db.multi.aggregate(
    {$match: {'kor': {$gt: 50}}},
    {$project: {'kor': 1}},
    {$group: {_id: 'test', 'average': {$avg: '$kor'}}}
)

※ $$는 System Variables에 접근을 가능하게 해준다.

// name에 s가 들어가는 document들의 kor값을 모두 더해서 {_id: 'test', 'sum': ???}로 출력.
db.multi.aggregate(
    {$match: {'name': /s/}},
    {$project: {'kor': 1}},
    {$group: {_id: 'test', 'sum': {$sum: '$kor'}}}
)



db.score.insertMany([
   {name:"홍길동",kor:90,eng:80,math:98,test:"midterm"},
   {name:"이순신",kor:100,eng:100,math:76,test:"final"},
   {name:"김선달",kor:80,eng:55,math:67,test :"midterm"},
   {name:"강호동",kor:70,eng:69,math:89,test:"midterm"},   
   {name:"유재석",kor:60,eng:80,math:78,test:"final"},
   {name:"신동엽",kor:100,eng:69,math:89,test:"midterm"},
   {name:"조세호",kor:75,eng:100,math:100,test:"final"}
])

// test가 final인 document들의 이름과 수학, 영어를 aggregate를 사용해서 출력하자.
db.score.aggregate(
    {$match: {'test': 'final'}},
    {$project: {_id: 0, 'name': 1, 'math': 1, 'eng': 1}},
)

// test가 midterm인 document들의 eng만 가지고 eng의 평균을 출력하자
db.score.aggregate(
    {$match: {'test': 'midterm'}},
    {$project: {'eng': 1}},
    {$group: {_id: 'average', 'eng': {$avg: '$eng'}}}
)