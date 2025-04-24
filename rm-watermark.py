#!/usr/bin/env python

# rm-watermark cleans pdfs of watermarks for readability and accessibility.
# Copyright (C) 2025 Johannes Janssen <0xJJ@hanni.dev>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: AGPL-3.0-only

import re

import pymupdf


def remove_adobe_watermark(input: str, output: str, **kwargs):
    """Tries to remove watermarks created by Adobe software from ``input`` pdf
    and save result as ``output`` pdf. This is achieved by searching for
    xobjects in each page, which are watermarks and remove commands to draw
    them (e.g. /Fm0 Do), as well as the whole surrounding graphic state between
    q and Q.

    Args:
        input: filename of input pdf
        output: filename of output pdf
        kwargs: options passed to Document.ez_save() function of pymupdf
    """
    watermark = re.compile("/ADBE_CompoundType.*/Watermark", re.DOTALL)

    doc = pymupdf.open(input)
    for page in doc:
        for xref, name, _, _ in page.get_xobjects():
            s = doc.xref_object(xref, compressed=False)
            if watermark.search(s) is not None:
                for c in page.get_contents():
                    s = doc.xref_stream(c)
                    s = re.sub(
                        bytes("q(?s:.)*/{}.*Do(?s:.)*Q".format(name), "ascii"),
                        rb"",
                        s,
                    )
                    doc.update_stream(xref, s)
        page.clean_contents()
    doc.ez_save(output, **kwargs)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        sys.exit("usage: {} input output".format(sys.argv[0]))

    remove_adobe_watermark(
        sys.argv[1],
        sys.argv[2],
    )
