# -*- coding: cp949 -*-
print "����� �¾ �⵵�� �Է��ϼ���"
year = int(raw_input())
nai = 2015 - year + 1
if(nai>=20 and nai<=26):
  print "���л�"
elif(nai>=17 and nai<20):
  print "����л�"
elif(nai>=14 and nai<17):
  print "���л�"
elif(nai>=8 and nai<14):
  print "�ʵ��л�"
else:
  print "�л��� �ƴմϴ�"
