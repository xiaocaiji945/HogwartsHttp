import pystache


def test_mu():
    a = pystache.render(
        'Hi {{person}}!{{test1}}',
        {'person': 'seveniruby','test1': 'hahaha'}
    )
    print(a)
