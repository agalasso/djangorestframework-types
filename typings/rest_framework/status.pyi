from typing_extensions import Literal

def is_informational(code: int) -> bool: ...
def is_success(code: int) -> bool: ...
def is_redirect(code: int) -> bool: ...
def is_client_error(code: int) -> bool: ...
def is_server_error(code: int) -> bool: ...

HTTP_100_CONTINUE: Literal[100]
HTTP_101_SWITCHING_PROTOCOLS: Literal[101]
HTTP_200_OK: Literal[200]
HTTP_201_CREATED: Literal[201]
HTTP_202_ACCEPTED: Literal[202]
HTTP_203_NON_AUTHORITATIVE_INFORMATION: Literal[203]
HTTP_204_NO_CONTENT: Literal[204]
HTTP_205_RESET_CONTENT: Literal[205]
HTTP_206_PARTIAL_CONTENT: Literal[206]
HTTP_207_MULTI_STATUS: Literal[207]
HTTP_208_ALREADY_REPORTED: Literal[208]
HTTP_226_IM_USED: Literal[226]
HTTP_300_MULTIPLE_CHOICES: Literal[300]
HTTP_301_MOVED_PERMANENTLY: Literal[301]
HTTP_302_FOUND: Literal[302]
HTTP_303_SEE_OTHER: Literal[303]
HTTP_304_NOT_MODIFIED: Literal[304]
HTTP_305_USE_PROXY: Literal[305]
HTTP_306_RESERVED: Literal[306]
HTTP_307_TEMPORARY_REDIRECT: Literal[307]
HTTP_308_PERMANENT_REDIRECT: Literal[308]
HTTP_400_BAD_REQUEST: Literal[400]
HTTP_401_UNAUTHORIZED: Literal[401]
HTTP_402_PAYMENT_REQUIRED: Literal[402]
HTTP_403_FORBIDDEN: Literal[403]
HTTP_404_NOT_FOUND: Literal[404]
HTTP_405_METHOD_NOT_ALLOWED: Literal[405]
HTTP_406_NOT_ACCEPTABLE: Literal[406]
HTTP_407_PROXY_AUTHENTICATION_REQUIRED: Literal[407]
HTTP_408_REQUEST_TIMEOUT: Literal[408]
HTTP_409_CONFLICT: Literal[409]
HTTP_410_GONE: Literal[410]
HTTP_411_LENGTH_REQUIRED: Literal[411]
HTTP_412_PRECONDITION_FAILED: Literal[412]
HTTP_413_REQUEST_ENTITY_TOO_LARGE: Literal[413]
HTTP_414_REQUEST_URI_TOO_LONG: Literal[414]
HTTP_415_UNSUPPORTED_MEDIA_TYPE: Literal[415]
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE: Literal[416]
HTTP_417_EXPECTATION_FAILED: Literal[417]
HTTP_418_IM_A_TEAPOT: Literal[418]
HTTP_422_UNPROCESSABLE_ENTITY: Literal[422]
HTTP_423_LOCKED: Literal[423]
HTTP_424_FAILED_DEPENDENCY: Literal[424]
HTTP_426_UPGRADE_REQUIRED: Literal[426]
HTTP_428_PRECONDITION_REQUIRED: Literal[428]
HTTP_429_TOO_MANY_REQUESTS: Literal[429]
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE: Literal[431]
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS: Literal[451]
HTTP_500_INTERNAL_SERVER_ERROR: Literal[500]
HTTP_501_NOT_IMPLEMENTED: Literal[501]
HTTP_502_BAD_GATEWAY: Literal[502]
HTTP_503_SERVICE_UNAVAILABLE: Literal[503]
HTTP_504_GATEWAY_TIMEOUT: Literal[504]
HTTP_505_HTTP_VERSION_NOT_SUPPORTED: Literal[505]
HTTP_506_VARIANT_ALSO_NEGOTIATES: Literal[506]
HTTP_507_INSUFFICIENT_STORAGE: Literal[507]
HTTP_508_LOOP_DETECTED: Literal[508]
HTTP_509_BANDWIDTH_LIMIT_EXCEEDED: Literal[509]
HTTP_510_NOT_EXTENDED: Literal[510]
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED: Literal[511]
