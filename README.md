# rm-watermark

`rm-watermark` is a small Python script that removes annoying watermarks from PDFs
to improve readability and accessibility.

## Usage

`./rm-watermark.py input output`

## Watermarks
The software has only been tested on a PDF where the watermarks seem to be
created by some Adobe software. If you want support for PDFs that do not work
with this script, patches and sample PDFs are always welcome. 

## Dependencies
The only direct dependency is [`PyMuPDF`](https://github.com/pymupdf/PyMuPDF).
So [`libmupdf`](https://mupdf.com/) and its Python bindings are also required.

## License

As `PyMuPDF` is used, the script is licensed under the GNU Affero GPL 3.0.
