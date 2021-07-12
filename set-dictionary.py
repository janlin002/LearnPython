#coding=UTF-8
s1={1, 2, 3, 4};
s2={3, 4, 5, 6};

#print(3 in s1);
#print(10 not in s2)

s3=s1&s2
#print(s3, '&')

s4=s1|s2;
#print(s4, '|')

s5=s1-s2;
#print(s5, '-');

s6= s1^s2;
#print(s6, '^');

s=set("Hello");
#print(s)
#print('a' in s)
#print('h' in s) 

#dic={"apple": "蘋果"}
#dic={'fruit': 'apple', 'car': 'toyota'}
#print(dic['car'])
#dic['car'] = 'benz';
#print(dic)
#print('car' in dic)
#del dic['car'];
#print(dic)

dic={x: x*2 for x in [3, 4 ,5]}
print(dic)

#print(dic['apple'])