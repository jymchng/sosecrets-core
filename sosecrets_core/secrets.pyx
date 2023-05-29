#cython: language_level=3
from typing import Optional, Dict, Callable, Any, Tuple, TypeVar


T = TypeVar('T')


cdef class Secret:

    cdef object inner_secret
    cdef readonly int expose_count
    cdef public int max_expose_count

    def __init__(self,
                 value: Optional[T] = None,
                 *,
                 func: Optional[Callable[[Any],
                                T]] = None,
                 func_args: Tuple[Any] = (),
                 func_kwargs: Dict[str, Any] = {},
                 max_expose_count: int = -1):
        if func is not None and value is not None:
            raise ValueError("`Secret` cannot be initialized with both `value` positional argument and `func` keyword")
        if func is not None:
            value = func(*func_args, **func_kwargs)
        self.inner_secret = value
        self.expose_count = 0
        self.max_expose_count = max_expose_count

    cpdef object expose_secret(self):
        if self.max_expose_count != -1:
            if self.expose_count < self.max_expose_count:
                self.expose_count += 1
                return self.inner_secret
            else:
                raise AttributeError('`Secret` cannot be exposed more than {} times'.format(self.max_expose_count))
        else:
            self.expose_count += 1
            return self.inner_secret

    def apply(self, func: Optional[Callable[[Any], T]], *, func_args: Tuple[Any]=(), func_kwargs: Dict[Any, Any]={}):
        inner_secret = self.inner_secret
        max_expose_count = self.max_expose_count
        # print(inner_secret, max_expose_count)
        # new_secret value is None
        # new_secret = Secret.__new__(Secret, func(inner_secret, *func_args, **func_kwargs), max_expose_count=max_expose_count)
        # new_secret.max_expose_count = max_expose_count
        # print(new_secret.expose_secret(), new_secret.expose_count, new_secret.max_expose_count)
        return Secret(func(inner_secret, *func_args, **func_kwargs), max_expose_count=max_expose_count)

    