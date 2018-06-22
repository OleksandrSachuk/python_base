def test(arg):
    def inner():
        return "Text: '%s'" % arg

    return inner


a = test('a')
b = test('b')

print('Type a: ', a)
print('Type b: ', b)

print('Result a: ' + a())
print('Result b: ' + b())
