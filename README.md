# sosecrets-core

Version = "0.1.0"

This Repo is a Cython implementation of a `Secret` class that allows you to hide a value or function behind a layer of security. The idea is that you can expose the secret value or function only a limited number of times, and only through a function call that checks the current exposure count against a maximum exposure count.

The `Secret` class has four attributes:

`inner_secret`: a private attribute that stores the actual secret value or function.
`expose_count`: a readonly attribute that keeps track of how many times the secret has been exposed.
`max_expose_count`: a public (read and write) attribute that sets the maximum number of times the secret can be exposed. If set to any negative integers, there is no limit to the number of exposures.
`apply`: a public method that applies a given function to the exposed secret and returns a new `Secret` object with the result.

## API

### Secret

A class representing a secret value with controlled exposure.

> `__init__(self, value: Optional[Any] = ..., *, func: Optional[Any] = ..., func_args: Tuple[Any, ...] = ..., func_kwargs: Dict[str, Any] = ..., max_expose_count: int = ...) -> Secret`

Initialize a `Secret` object.

* value: The initial value of the `Secret` object. If provided, it takes precedence over `func`.
* func: A function used to generate the initial value of the `Secret` object. Ignored if value is provided.
* func_args: Positional arguments to pass to the `func` function.
* func_kwargs: Keyword arguments to pass to the `func` function.
* max_expose_count: The maximum number of times the `Secret` object can be exposed. Set to -1 for unlimited.

Raises:

* ValueError: If both `value` and `func` arguments are provided.

### `Secret.expose_secret()`

Exposes the secret value.

> `expose_secret(self) -> object`

Returns:

The inner secret value.

Raises:

* AttributeError: If the Secret object has reached the maximum exposure count.

### `Secret.apply(...)`

Apply a function to the inner secret value and return a new `Secret` object.

> `apply(self, func: Callable[[Any, ...], Any], *, func_args: Tuple[Any, ...] = ..., func_kwargs: Dict[str, Any] = ...) -> Secret`

* func: The function to apply to the inner secret value.
* func_args: Positional arguments to pass to the `func` function.
* func_kwargs: Keyword arguments to pass to the `func` function.

Returns:

A new Secret object with the result of applying the function to the inner secret value.

## License
This code is released under the MIT License.