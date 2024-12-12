TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Tuple, Union 
    VERSION_TUPLE = Tuple[Union[int, str], ...]
else:
    VERSION_TUPLE = object 

version: str
__version__: str
__version_tuple__: VERSION_TUPLE
version_tuple: VERSION_TUPLE

__version__ = version = '0.0.1.post1'
__version_tuple__ = version_tuple = (0, 0, 1)