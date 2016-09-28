def test(a, b, *args, **kwargs):
    print(a)
    print(b)
    for i in args:
        print('args:', i)
    for (x, y) in kwargs.items():
        print("key:", x, "value:", y)

list1 = [1, 2, 3, 5]
map1 = {"city": "北京", "age": 23, "gent": "男"}
test(*list1, **map1)

