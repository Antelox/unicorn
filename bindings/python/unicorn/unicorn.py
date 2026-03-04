import sys as _sys

# legacy
if _sys.version_info.major == 2:
    from .unicorn_py2 import *
    from .unicorn_const import (
        UC_VERSION_MAJOR as __MAJOR,
        UC_VERSION_MINOR as __MINOR,
        UC_VERSION_PATCH as __PATCH
    )

    __version__ = "%u.%u.%u" % (__MAJOR, __MINOR, __PATCH)
else:
    from .unicorn_py3 import *

    try:
        from importlib import metadata
    except ImportError:
        import importlib_metadata as metadata  # Backport for Python < 3.8

    __version__ = metadata.version("unicorn")
