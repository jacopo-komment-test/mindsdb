from mindsdb.integrations.libs.const import HANDLER_TYPE

from .__about__ import __version__ as version, __description__ as description
try:
    from .anyscale_endpoints_handler import AnyscaleEndpointsHandler as Handler
    import_error = None
except Exception as e:
    Handler = None
    import_error = e

title = 'Anyscale Endpoints'
name = 'anyscale_endpoints'
type = HANDLER_TYPE.ML
permanent = True

__all__ = [
    'Handler', 'version', 'name', 'type', 'title', 'description', 'import_error'
]
