class PackageError(Exception):
    pass


class SourceError(PackageError):
    pass


class DataError(PackageError):
    pass


class SettingsError(PackageError):
    pass