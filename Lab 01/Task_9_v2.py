def foo_moo(n):
    is_div_by_2 = n % 2 == 0
    is_div_by_3 = n % 3 == 0

    if is_div_by_2 and is_div_by_3:
        return "FooMoo"
    elif is_div_by_2:
        return 'Foo'
    elif is_div_by_3:
        return "Moo"
    else:
        return "Boo"

print(foo_moo(6))
