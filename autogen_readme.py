import ast, os

def extract_code_summaries(file_path):
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())

    summaries = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            name = node.name
            docstring = ast.get_docstring(node)
            if docstring:
                summaries.append(f"### {name}\n{docstring}\n")
            else:
                summaries.append(f"### {name}\n(No docstring available)\n")
    return summaries
    

def update_readme(section_title, new_content):
    with open("README.md", "r") as f:
        lines = f.readlines()

    start = None
    end = None

    for i, line in enumerate(lines):
        if section_title in line:
            start = i + 1
        if start and (line.startswith("## ") or i == len(lines) - 1):
            end = i
            break

    if start and end:
        updated = lines[:start] + new_content + lines[end:]
        with open("README.md", "w") as f:
            f.writelines(updated)

if __name__ == "__main__":
    summaries = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py") and file != "autogen_readme.py":
                summaries += extract_code_summaries(os.path.join(root, file))

    content_lines = ["\n"] + summaries + ["\n"]
    update_readme("## Auto Documentation", content_lines)

