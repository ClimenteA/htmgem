# HTMGEM

Generate html with Python.


```py

html_str = ul({"class": "somediv"}, [
    (li, "item1"),
    (li, "item2"),
    (li, {"id": "myid", "class":"important"}, "item3"),
])

```

The `html_str` will be:

```html
<ul class="somediv"><li>item1</li> <li>item2</li> <li id="myid" class="important">item3</li></ul>
```



