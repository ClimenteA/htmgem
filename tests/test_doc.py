# print("test_doc pkg: ",__package__)
import unittest
from htmgem.doc import Doc
from htmgem.tags import *


page = Doc()


class TestDoc(unittest.TestCase):

    def test_html_boilerplate(self):

        html_str = \
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

        # print(html_str)

        neededhtml = '<html lang="en"><head><meta charset="UTF-8"></meta> <meta name="viewport" content="width=device-width, initial-scale=1.0"></meta> <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.1.2/tailwind.min.css"></link> <script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js" defer></script></head> <body><h1>Interesting title</h1> <p>'

        assert neededhtml in html_str  
        
