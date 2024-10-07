def format_linter_error(error: dict) -> dict:
    return [
        {"line": err["line_number"],
         "column": err["column_number"],
         "message": err["text"],
         "name": err["code"],
         "source": "flake8"} for file_errors in error.values() for err in file_errors]
    pass


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    pass


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
