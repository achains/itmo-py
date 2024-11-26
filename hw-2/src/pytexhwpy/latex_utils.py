__all__ = ["generate_latex_table", "generate_latex_figure"]


def generate_latex_table(data) -> str:
    """
    Generates a LaTeX table from a 2D list (matrix).

    :param data 2D table data
    :returns generated latex table
    """
    if not data or len(data) < 2:
        return ""

    latex = [
        "\\begin{table}[h!]",
        "\\centering",
        f"\\begin{{tabular}}{{|{'l' * len(data[0])}|}}"
    ]

    header = " & ".join([f"\\textbf{{{str(item)}}}" for item in data[0]])
    latex.extend([
        "\\hline",
        f"{header} \\\\",
        "\\hline"
    ])

    # Add body rows
    for row in data[1:]:
        row_str = " & ".join([str(item) for item in row])
        latex.append(f"{row_str} \\\\")
        latex.append("\\hline")

    # Close table
    latex.extend([
        "\\end{tabular}",
        "\\caption{Your caption here.}",
        "\\label{table:your_label_here}",
        "\\end{table}"
    ])

    return "\n".join(latex)

def generate_latex_figure(image_path: str, caption="Your caption") -> str:
    """
    Generates LaTeX code to include an image

    :param image_path path to the image file
    :param caption image caption
    :returns latex wrapper code to include an image
    """
    return f"""\\begin{{figure}}[ht]
\\centering
\\includegraphics[width=0.8\\textwidth]{{{image_path}}}
\\caption{{{caption}}}
\\end{{figure}}"""
