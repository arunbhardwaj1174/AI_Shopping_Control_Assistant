def parse_float(value, field_name):
    if value is None or str(value).strip() == "":
        raise ValueError(f"{field_name} is required.")
    try:
        parsed = float(value)
    except ValueError:
        raise ValueError(f"{field_name} must be a number.")
    if parsed < 0:
        raise ValueError(f"{field_name} must be zero or positive.")
    return parsed


def parse_int(value, field_name):
    if value is None or str(value).strip() == "":
        raise ValueError(f"{field_name} is required.")
    try:
        parsed = int(float(value))
    except ValueError:
        raise ValueError(f"{field_name} must be an integer.")
    if parsed < 0:
        raise ValueError(f"{field_name} must be zero or positive.")
    return parsed
