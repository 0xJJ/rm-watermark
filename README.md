# rm-watermark

rm-watermark is a little python script to remove annoying watermarks from pdfs
for better readability and accessibility.

## Usage

./rm-watermark.py input output

## Watermarks
The software was only tested with a pdf, where the watermarks seam to be created
by some Adobe software. If you like to have support for pdfs which are not
working with this script, patches and example pdfs are always welcome. 

## Dependencies
Only direct dependency is PyMuPDF. Hence libmupdf and its python bindings are
also required.

## License

As PyMuPDF is used, the script is licensed under the GNU Affero GPL 3.0.
