from pytexhwpy.latex_utils import generate_latex_figure

image = "sample.jpg"
caption = "Hello homework"
figure_code = generate_latex_figure(image, caption)

latex_doc = f"""
\\documentclass{{article}}
\\usepackage{{graphicx}}
\\begin{{document}}
{figure_code}
\\end{{document}}
"""

with open("hw-2/artifacts/example_figure.tex", "w") as f:
    f.write(latex_doc)
