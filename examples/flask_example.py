from flask import Flask, request
from htmgem.tags import *
from functools import lru_cache


app = Flask(__name__)


# The head component
@lru_cache(maxsize=None) # add cache for performance (you can use cache decorator if you have python 3.9+) 
def Head():
    return head([  
        meta({'charset':'UTF-8'}),
        meta({'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}),
        # link({'rel':'stylesheet', 'href':'https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.1.2/tailwind.min.css'}), 
        # script({'src':'https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js', 'defer':None})
    ])


# Define a base html
base_html = lambda content: \
html({'lang':'en'}, [
    Head(),
    body({'class': ['bg-blue-100', 'p-10']}, content)
])

# You can define a page layout
def page_layout(page_title, page_content):
    return base_html([
        h1(
            {"class":"text-2xl text-center"}, 
            page_title
        ),
        page_content
    ])


# This is a component
def Link(path, content):

    class_list = [
        'bg-blue-200',
        'p-4',
        'cursor-pointer'
    ]    

    return a(
        {"href": path, "class": class_list, 'style':'margin-left:2rem;'}, 
        content
    )




# As you can see up you have fine grained control on how the page looks
# You can place the components in .py files 
# add some lru_cache/cache for performance and you are set.

# Let's see some endpoints bellow

# We will save some names later (mock db)
names_saved = []

#A list of names saved
def NamesSaved():
    #Whatever operations you want to do on data
    name_list = []
    for name in names_saved:
        name_list.append(li(name))

    return [
        h4(f"Currently saved names {len(names_saved)}"),
        br(),
        ul(name_list)
    ]
    

@app.route("/")
def index():  
    return page_layout(
        page_title   = "Welcome to home page!", 
        page_content = [ #list of components or just the component
            p("""
            You can go to form page to save your name
            """),
            Link(path='/send-data', content="Go to form page"),
            Link(path='/htmgem-big-list', content="Generate a big list with Python"),
            Link(path='/html-big-list', content="Generate a big list with Javascript"),
            NamesSaved()
        ]
    )


#The Form component
def Form():
    # Html tags that conflict with python have a underscore after them
    # that's way input tag is `input_`

    return form({
        'action': '/save-data', 
        'method': 'POST',
        'style': 'margin:0 auto;padding-top:2rem',
    }, [
        label({'for':'username'}, "Save your name:"), 
        br(),
        input_({'type': 'text', 'id':'username', 'name':'username'}), 
        br(),
        button({'type': 'submit'}, 'Save my name')
    ])



@app.route("/send-data", methods=['GET'])
def sendData(): 
    return page_layout(
        page_title   = "Welcome to form page!", 
        page_content = [
            Link(path='/', content="Go to home page"),
            Form()
        ]
    )


@app.route("/save-data", methods=['POST'])
def saveData(): 

    username_to_save = request.form.get('username')

    if username_to_save: #validate/sanitaze your data
        names_saved.append(username_to_save)

    return page_layout(
        page_title   = f"Name '{username_to_save}' was saved!", 
        page_content = Link(path='/', content="Go to home page")
    )



nbr_items = 100_000

@app.route("/htmgem-big-list", methods=['GET'])
def bigList():

    return page_layout(
        page_title   = f"Big list of {nbr_items} items created with Python!", 
        page_content = [
            Link(path='/', content="Go to home page"),
            ul([li(item+1) for item in range(nbr_items)])
        ]
    )



@app.route("/big-list-js", methods=['GET'])
def bigListJs():

    return {'data': list(range(nbr_items))}


@app.route("/html-big-list", methods=['GET'])
def bigListJsTemplate():

    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<h1>Big list of items created with JS!</h1>
<a href="/" class="bg-blue-200 p-4 cursor-pointer" style="margin-left:2rem;">Go to home page</a>


<ul id="items">
    <!-- Content added by js -->
</ul>


<script>
    
fetch('http://localhost:5000/big-list-js')
.then(response => response.json())
.then(data => {

    let ul = document.getElementById('items')
    
    data['data'].forEach(nbr => {
        let li = document.createElement('li')
        li.innerHTML = nbr
        ul.appendChild(li)
    })
}
)

</script>

    
</body>
</html>

"""



if __name__ == "__main__":
    app.run(debug=True)
