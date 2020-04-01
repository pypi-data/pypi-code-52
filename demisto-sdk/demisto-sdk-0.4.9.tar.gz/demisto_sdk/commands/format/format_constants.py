DEFAULT_VERSION = -1
NEW_FILE_DEFAULT_5_FROMVERSION = '5.0.0'
OLD_FILE_DEFAULT_1_FROMVERSION = '1.0.0'
SCHEMAS_PATH = "schemas"
SUCCESS_RETURN_CODE = 0
ERROR_RETURN_CODE = 1
SKIP_RETURN_CODE = 2

ARGUMENTS_DEFAULT_VALUES = {
    'content': (True, ['IncidentFieldJSONFormat', 'IndicatorFieldJSONFormat']),
    'system': (
        False, ['IncidentFieldJSONFormat', 'IncidentTypesJSONFormat', 'IndicatorFieldJSONFormat', 'IndicatorTypeJSONFormat']),
    'required': (False, ['IncidentFieldJSONFormat', 'IndicatorFieldJSONFormat']),
}
