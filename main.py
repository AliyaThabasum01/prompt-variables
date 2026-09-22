from template_engine import extract_variables, fill_template

print("🧩 Prompt Variables")
print("=" * 40)

template = input("Enter prompt template:\n> ")

variables = extract_variables(template)

if not variables:
    print("\n⚠️ No variables found.")
else:
    values = {}

    print("\nFill the variables:")

    for variable in variables:
        values[variable] = input(f"{variable}: ")

    result = fill_template(template, values)

    print("\n✨ Final Prompt")
    print("=" * 40)
    print(result)
