import re


def extract_variables(template):
    return list(dict.fromkeys(
        re.findall(r"\{([a-zA-Z0-9_]+)\}", template)
    ))


def fill_template(template, values):
    for key, value in values.items():
        template = template.replace(
            "{" + key + "}",
            value
        )

    return template
