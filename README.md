# bibtex2html-fix

This python script applies a few minor tweaks to html files output by [`bibtex2html`](https://www.lri.fr/~filliatr/bibtex2html/). The html tables output by it use `valign="top"`, which has been replaced by `style="vertical-align:top"`. This error produces numbered bibliographies with the numbers aligned in the center of the entry and not the top. This script fixes the output html file.

An optional flag `-l` can be used to tell `bibtex2html-fix` to add a link in the form of `<ID>Cite`. When you create your citations you should include an anchor of the same tag. This allows you to jump between citation and bibliography entry.

Meant for use with Jupyter Lab or other environments where you would need to add a bibliography manually.
