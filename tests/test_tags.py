import unittest
from htmgem.tags import *


class TestGem(unittest.TestCase):

    def test_no_params(self):
        self.assertEqual(h1(), '<h1></h1>')        

    def test_tag_with_attrs_and_text_child(self):
        res = h1({"class":"test"}, "Some title")
        self.assertEqual(res, '<h1 class="test">Some title</h1>')


    def test_tag_with_attrs_and_list_children(self):
        res = article(
            {"class":"test"}, 
                [
                    p({}, "some text"), 
                    p({}, "some another text")
                ]
            )

        self.assertEqual(res, '<article class="test"><p>some text</p> <p>some another text</p></article>')
        

    def test_tag_no_attrs_text_children(self):
        self.assertEqual(h1("just text"), '<h1>just text</h1>')


    def test_tag_attrs_list_tuple_children(self):
        res = ul({"class": "somediv"}, [
            (li, "item1"),
            (li, "item2"),
            (li, {"id": "myid", "class":"important"}, "item3"),
        ])

        # print(res)

        self.assertEqual(res, '<ul class="somediv"><li>item1</li> <li>item2</li> <li id="myid" class="important">item3</li></ul>')


    def test_generate_list_with_map(self):

        some_list = [
            "item",         # just children str
            1,              # just children int  
            {"id": "myid"}, # just attrs

            ( #tuple with attrs and children and some alpinejs
                {
                    "class":["mx-auto", "p-4"], 
                    "@click.away":"open = false",
                    "x-data":"{ open: false }"
                }, 
                "some content for li"
            )
        ]

        res = div(
            ul( {"class":["collection", "margin-top"]}, [li(i) for i in some_list] )
        )

        # print(res)

        self.assertEqual(res, '<div><ul class="collection margin-top"><li>item</li> <li>1</li> <li id="myid"></li> <li class="mx-auto p-4" @click.away="open = false" x-data="{ open: false }">some content for li</li></ul></div>')
        

    def test_list_of_children(self):
        res = head([
            meta({'charset':'UTF-8'}),
            meta({'name':'viewport', 'content':'width=device-width, initial-scale=1.0'})
        ])

        # print(res)

        self.assertEqual(res, '<head><meta charset="UTF-8"></meta> <meta name="viewport" content="width=device-width, initial-scale=1.0"></meta></head>')

    def test_script_js(self):

        res = script({'src':'https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js', 'defer':None})
            
        # print(res)

        self.assertEqual(res, '<script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js" defer></script>')




if __name__ == '__main__':
    unittest.main()
