from hello import my_abs

print(my_abs(111))

inits = []
def append_end(L = inits):
    L.append("end")
    return L


print(append_end())
print(append_end())
print(inits)

nums = [1,2,3]
s = set(nums)
print(*s)

# 关键字参数
def person(name, age, **kw):
    print("name =", name, "age=", age, kw)

person("bob", 10, city = "beijing")

def asdf(name, age = 10, *args, city, **kw):
    print("name =",name,"age =",age)
    print(args)
    print(city)
    print(kw)
    return

asdf("hoult", 12, "hahhah", city="beijing", country="china", weather="good")