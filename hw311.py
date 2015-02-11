#! /usr/bin/python
#1
n=re.findall(r"5", names)
print(n.group())
#2
m=re.findall(r"(d)(e)", names)
print(m.group())
#3
p= re.search(r"de", names)
print(p.group())
#4
q = re.search(r"d[\w]e", names)
print(q.group())
#5
s = re.search(r"(de)", names) or re.search(r"(ed)", names)
print(s.group())
#6
t = re.search(r"^x", names) or re.search(r"^y", names)
print(t.group())
#7
u = re.search(r"(^x)(e$)", names) or re.search(r"(^y)(e$)", names)
print(u.group())
#8
v = re.search(r"[\d]{3}+", names)
print(v.group())
#9
w = re.search(r"($d)[arp]", names)
print(w.group())

