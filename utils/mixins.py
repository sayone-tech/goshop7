from import_export.admin import ExportMixin
from import_export.formats import base_formats

DEFAULT_FORMATS = (
    base_formats.CSV,
    base_formats.XLS,
    base_formats.TSV,
    base_formats.ODS,
    base_formats.JSON,
    base_formats.YAML,
)
class CustomExportMixin(ExportMixin):
    formats = DEFAULT_FORMATS