#!/usr/bin/env python3

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(dest='bib', metavar='bib.html',
                    help='The html bibliography output by bibtex2html')
parser.add_argument('--link', '-l', action='store_true',
                    help='Add link for predetermined citation id in order to \
                    allow for navigation from bibliography to first occurance \
                    of citation in text. \n\
                    Citation id takes the form of bib entry id + "Cite".\n\
                    i.e. entry = "Froehlich2005", citation id = \
                    "Froehlich2005Cite"'
                    )
args = parser.parse_args()

with open(args.bib, 'r') as f:
    fdata = f.read()

print('Correcting alignment...')

# Replace valign and align to comply with HTML5
fdata = fdata.replace('<tr valign="top">\n<td align="right"',
                      '<tr>\n<td style="vertical-align:top; text-align:right;"'
                      )

# Add hyperlink for citation. Citation id will be bibliography id + 'Cite'
# i.e. bibentry = "Froehlich2005" citation = "Froehlich2005Cite"
# Entry id's will be preceeded by 'class="bibtexnumber">\n[<a name="'
if args.link:
    key = 'class="bibtexnumber">\n[<a name="'
    index = fdata.find(key, 0)
    while index != -1:
        # Get entry id
        start = index + len(key)
        end = fdata.find('"', start)
        entry = fdata[start:end]

        # Create link entry
        link = ' href="#' + entry + 'Cite"'

        # Check if link entry exists already
        if fdata.find(link, end, end + len(link) + 1) == -1:
            print('Inserting link for "' + entry + '"')
            fdata = fdata[:end + 1] + link + fdata[end + 1:]
        else:
            print('Link already exists for "' + entry + '"')

        index = fdata.find(key, index + 1)

with open(args.bib, 'w') as f:
    f.write(fdata)
