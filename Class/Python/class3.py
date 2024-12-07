def test(a):
    if(a == 10):
        return 3
    print(a)
    test(a + 1)

test(3)