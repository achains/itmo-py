# Use a base image with Python and pip installed
FROM python:3.11-slim

# Install LaTeX
RUN apt-get update && \
    apt-get install -y --no-install-recommends texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY hw-2/create_figure.py /app/create_figure.py
COPY hw-2/artifacts/image.png /app/image.png

RUN mkdir -p /app/hw-2/artifacts
RUN pip install -i https://test.pypi.org/simple/ pytexhwpy

RUN python create_figure.py
RUN pdflatex -output-directory=/app/hw-2/artifacts /app/hw-2/artifacts/example_figure.tex
