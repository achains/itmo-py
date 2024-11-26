from pytexhwpy.latex_utils import generate_latex_table


data = [
    ["A", "B", "C"],
    ["0", "1", "2"],
    ["3", "4", "5"],
    ["6", "7", "8"]
]

latex_code = generate_latex_table(data)

with open("hw-2/artifacts/example_table.tex", "w") as file:
    file.write(latex_code)