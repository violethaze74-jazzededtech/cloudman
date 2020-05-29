import tempfile
import yaml

from contextlib import contextmanager


@contextmanager
def TempInputFile(text, prefix="helmsman"):
    """
    Context manager to carry out an action
    after creating a temporary file with the
    given text content.

    :params text: The text to write to a file
    Usage:
        with TempInputFile("hello world"):
            do_something()
    """
    with tempfile.NamedTemporaryFile(mode="w", prefix=prefix) as f:
        f.write(text)
        yield f


@contextmanager
def TempValuesFile(values, prefix="helmsman"):
    """
    Context manager to carry out an action
    after creating a temporary file with the
    given yaml values.

    :params values: The yaml values to write to a file
    Usage:
        with TempValuesFile({'hello': 'world'}):
            do_something()
    """
    with tempfile.NamedTemporaryFile(mode="w", prefix=prefix) as f:
        yaml.safe_dump(values, stream=f, default_flow_style=False)
        yield f
