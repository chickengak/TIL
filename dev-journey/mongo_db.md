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