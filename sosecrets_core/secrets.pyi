from typing import Callable, Optional, Any, Dict, Tuple, ClassVar

class Secret:
    expose_count: ClassVar[int]
    max_expose_count: ClassVar[int]

    def __init__(
        self,
        value: Optional[Any] = ...,
        *,
        func: Optional[Any] = ...,
        func_args: Tuple[Any, ...] = ...,
        func_kwargs: Dict[str, Any] = ...,
        max_expose_count: int = ...,
    ) -> None:
        """
        Initialize a Secret object.

        Args:
            value: The initial value of the Secret object. If provided, it takes precedence over `func`.
            func: A function used to generate the initial value of the Secret object. Ignored if `value` is provided.
            func_args: Positional arguments to pass to the `func` function.
            func_kwargs: Keyword arguments to pass to the `func` function.
            max_expose_count: The maximum number of times the Secret object can be exposed. Set to -1 for unlimited.

        Raises:
            ValueError: If both `value` and `func` arguments are provided.

        """
        ...

    def expose_secret(self) -> object:
        """
        Expose the secret value.

        Returns:
            The inner secret value.

        Raises:
            AttributeError: If the Secret object has reached the maximum exposure count.

        """
        ...

    def apply(
        self,
        func: Callable[[Any], Any],
        *,
        func_args: Tuple[Any, ...] = ...,
        func_kwargs: Dict[str, Any] = ...,
    ) -> 'Secret':
        """
        Apply a function to the inner secret value and return a new Secret object.

        Args:
            func: The function to apply to the inner secret value.
            func_args: Positional arguments to pass to the `func` function.
            func_kwargs: Keyword arguments to pass to the `func` function.

        Returns:
            A new Secret object with the result of applying the function to the inner secret value.

        """
        ...
