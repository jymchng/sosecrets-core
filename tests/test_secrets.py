import pytest
from sosecrets_core.secrets import Secret


def test_after_apply_max_expose_count_remains_same_and_raises():
    def funcc(a, gg, bye='hihi'):
        return bye + a + gg

    s = Secret("bye", max_expose_count=3)
    d = s.apply(funcc, func_args=('lol',), func_kwargs=dict(bye='bb'))
    assert d.max_expose_count == 3

    with pytest.raises(AttributeError):
        for i in range(5):
            scrt = d.expose_secret()
            assert scrt.expose_count == 1 + i
            assert scrt == 'bbbyelol'
            print(scrt, end=" ")
            print(d.expose_count, end=" ")


def test_max_expose_count_works():
    s = Secret("bye", max_expose_count=3)
    
    with pytest.raises(AttributeError):
        for i in range(5):
            scrt = s.expose_secret()
            assert scrt.expose_count == i + 1
            assert scrt == 'bye'
            print(scrt, end=" ")
            print(s.expose_count, end=" ")


def test_apply_works():
    s = Secret("bye", max_expose_count=3)
    assert s.max_expose_count == 3
    def funcc(a, gg, kk='hihi'):
        return kk + a + gg
    d = s.apply(funcc, func_args=('zz',), func_kwargs=dict(kk='lol'))
    assert d.max_expose_count == 3
    with pytest.raises(AttributeError):
        for _ in range(5):
            scrt = d.expose_secret()
            assert scrt == 'lolbyezz'
            print(scrt, end=" ")
            print(d.expose_count, end=" ")


def test_inner_secret_not_accessible():
    s = Secret("bye", max_expose_count=3)
    with pytest.raises(AttributeError):
        s.inner_secret
        
        
def test_secret_exposed_as_many_times_as_wished():
    s = Secret("bye")
    
    for i in range(1000):
        assert s.max_expose_count == -1
        assert s.expose_count == i
        assert s.expose_secret() == 'bye'
        
        
def test_secret_exposed_as_many_times_as_wished_after_apply():
    s = Secret("bye")
    
    def funcc(a, gg, kk='hihi'):
        return kk + a + gg
    d = s.apply(funcc, func_args=('zz',), func_kwargs=dict(kk='lol'))
    
    for i in range(1000):
        assert d.max_expose_count == -1
        assert d.expose_count == i
        assert d.expose_secret() == 'lolbyezz' 


def test_from_func():
    def funcc(a, gg, kk='hihi'):
        return kk + a + gg

    s = Secret(
        func=funcc,
        func_args=(
            'zz',
            'bb'),
        func_kwargs={
            "kk": 'byebye'},
        max_expose_count=5)
    assert s.max_expose_count == 5
    assert s.expose_secret() == 'byebyezzbb' # expose_count raises to 1
    
    with pytest.raises(AttributeError):
        for i in range(5):
            assert s.expose_count == i + 1
            assert s.expose_secret() == 'byebyezzbb'
    
    
def test_from_func_two():
    def funcc(a, gg, kk='hihi'):
        return kk + a + gg

    s = Secret(
        func=funcc,
        func_args=(
            'zz',
            'bb'),
        max_expose_count=5)
    
    assert s.max_expose_count == 5
    assert s.expose_secret() == 'hihizzbb' # expose_count raises to 1
    
    with pytest.raises(AttributeError):
        for i in range(5):
            assert s.expose_count == i + 1
            assert s.expose_secret() == 'hihizzbb'


def test_raises_if_both_value_and_func():
    def funcc(a, gg, kk='hihi'):
        return kk + a + gg

    with pytest.raises(ValueError):
        s = Secret("hello", func=funcc, func_args=('zz', 'bb'))
