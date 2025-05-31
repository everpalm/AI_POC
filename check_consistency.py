import os
import ast
import re


REQUIREMENTS_FILE = "requirements.md"
SRC_DIR = "src"


def parse_requirements_md(path):
    """
    Parses requirements.md for class and method specifications.

    Returns a dict: {class_name: {method_name: docstring/desc}}
    """
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    class_methods = {}
    class_pattern = re.compile(
        r'(\w+) class.*?methods?:((?:.|\n)*?)(?=\n\w+ class|\Z)',
        re.IGNORECASE
    )
    method_pattern = re.compile(r'-\s*(\w+)\((.*?)\):\s*(.*)')
    for class_match in class_pattern.finditer(content):
        class_name = class_match.group(1)
        methods_block = class_match.group(2)
        methods = {}
        for method_match in method_pattern.finditer(methods_block):
            method_name = method_match.group(1)
            method_desc = method_match.group(3)
            methods[method_name] = method_desc
        class_methods[class_name] = methods
    return class_methods


def scan_python_code(src_dir):
    """
    Scans src/ for Python files, extracts class/method signatures
    and docstrings.

    Returns a dict:
    {class_name: {method_name: docstring or None, is_placeholder: bool}}
    """
    code_map = {}
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read(), filename=path)
                for node in ast.iter_child_nodes(tree):
                    if isinstance(node, ast.ClassDef):
                        class_name = node.name
                        methods = {}
                        for item in node.body:
                            if isinstance(item, ast.FunctionDef):
                                docstring = ast.get_docstring(item)
                                is_placeholder = (
                                    len(item.body) == 1
                                    and isinstance(item.body[0], ast.Expr)
                                    and isinstance(item.body[0].value, ast.Str)
                                )
                                methods[item.name] = {
                                    "docstring": docstring,
                                    "is_placeholder": is_placeholder
                                }
                        code_map[class_name] = methods
    return code_map


def compare_requirements_and_code(reqs, code):
    """
    Compares requirements and code, reports missing/inconsistent elements
    and placeholders.
    """
    report = []
    for class_name, methods in reqs.items():
        if class_name not in code:
            report.append(f"Missing class: {class_name}")
            continue
        for method_name in methods:
            if method_name not in code[class_name]:
                report.append(f"Missing method: {class_name}.{method_name}")
            else:
                if code[class_name][method_name]["is_placeholder"]:
                    report.append(
                        f"Placeholder detected: {class_name}.{method_name}"
                    )
    for class_name in code:
        if class_name not in reqs:
            report.append(f"Extra class in code: {class_name}")
        else:
            for method_name in code[class_name]:
                if method_name not in reqs[class_name]:
                    report.append(
                        f"Extra method in code: {class_name}.{method_name}"
                    )
    return report


if __name__ == "__main__":

    reqs = parse_requirements_md(REQUIREMENTS_FILE)
    code = scan_python_code(SRC_DIR)
    report = compare_requirements_and_code(reqs, code)
    if report:
        print("Consistency Check Report:")
        for line in report:
            print("-", line)
    else:
        print("Codebase is consistent with requirements.md.")
