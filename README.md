# HTMGEM (in progress)

Generate html with Python.


```py

from htmgem.tags import *


html_string = \
html({'lang':'en'}, [
    head([
        meta({'charset':'UTF-8'}),
        meta({'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}),
        link({'rel':'stylesheet', 'href':'https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.1.2/tailwind.min.css'}), 
        script({'src':'https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js', 'defer':None})
    ]),

    body([
        h1("Interesting title"),

        p("""

            A very long paragraph

        """),

        ul({"class": "somediv"}, [
            (li, "item1"),
            (li, "item2"),
            (li, {"id": "myid", "class":"important"}, "item3"),
        ])
    ])
])


# And that's it 

```

The `html_string` will be the parsed html string.



