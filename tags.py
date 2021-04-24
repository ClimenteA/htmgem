#This module generates html function tags (needs to run only once)
from inspect import isfunction


def _prep_attrs(attrs):
    
    if "class" in attrs:
        if isinstance(attrs["class"], list):
            attrs["class"] = " ".join(attrs["class"])
    
    attrs = " ".join([f'{k}="{v}"' for k,v in attrs.items()])
    attrs = " " + attrs if attrs else attrs 
    
    return attrs


def _prep_children(children):
    
    if isfunction(children):
        return children()
    
    if isinstance(children, list):
        children_list = []
        for obj in children:
            if isfunction(obj): 
                children_list.append(obj())
            elif isinstance(obj, tuple):
                if len(obj) == 3:
                    children_list.append(obj[0](obj[1], obj[2]))
                elif len(obj) == 2:
                    children_list.append(obj[0](obj[1]))
            elif isinstance(obj, str):
                children_list.append(obj)
            else:
                raise Exception(f"Can't parse children:{children}({type(children)})")
    
        children = " ".join([c for c in children_list])
        
    return children


def _prep_args(attrs, children):

    # print("_prep_args attrs:", attrs, "children:", children)
    
    attrs = str(attrs) if isinstance(attrs, int) else attrs
    children = str(children) if isinstance(children, int) else children

    no_children   = children == None
    no_attrs      = attrs == None
    dict_attrs    = isinstance(attrs, dict)
    str_attrs    = isinstance(attrs, str)
    list_children = isinstance(children, list)
    text_children = isinstance(children, str)
    
    if no_attrs and no_children: 
        return "", ""

    if dict_attrs and (list_children or text_children):
        return _prep_attrs(attrs), _prep_children(children)

    if str_attrs and no_children:
        return "", _prep_children(attrs)

    if dict_attrs and no_children:
        return _prep_attrs(attrs), ""
    
    raise Exception(f"Can't parse attrs:{attrs}({type(attrs)}) and children:{children}({type(children)})")
    
       


def a(attrs=None, children=None):
    """ Defines a hyperlink """
    attrs, children = _prep_args(attrs, children)
    return f"<a{attrs}>{children}</a>"


def abbr(attrs=None, children=None):
    """ Defines an abbreviation or an acronym """
    attrs, children = _prep_args(attrs, children)
    return f"<abbr{attrs}>{children}</abbr>"


def address(attrs=None, children=None):
    """ Defines contact information for the author/owner of a document """
    attrs, children = _prep_args(attrs, children)
    return f"<address{attrs}>{children}</address>"


def area(attrs=None, children=None):
    """ Defines an area inside an image-map """
    attrs, children = _prep_args(attrs, children)
    return f"<area{attrs}>{children}</area>"


def article(attrs=None, children=None):
    """ Defines an article """
    attrs, children = _prep_args(attrs, children)
    return f"<article{attrs}>{children}</article>"


def aside(attrs=None, children=None):
    """ Defines content aside from the page content """
    attrs, children = _prep_args(attrs, children)
    return f"<aside{attrs}>{children}</aside>"


def audio(attrs=None, children=None):
    """ Defines sound content """
    attrs, children = _prep_args(attrs, children)
    return f"<audio{attrs}>{children}</audio>"


def b(attrs=None, children=None):
    """ Defines bold text """
    attrs, children = _prep_args(attrs, children)
    return f"<b{attrs}>{children}</b>"


def base(attrs=None, children=None):
    """ Specifies the base URL/target for all relative URLs in a document """
    attrs, children = _prep_args(attrs, children)
    return f"<base{attrs}>{children}</base>"


def bdi(attrs=None, children=None):
    """ Isolates a part of text that might be formatted in a different direction from other text outside it """
    attrs, children = _prep_args(attrs, children)
    return f"<bdi{attrs}>{children}</bdi>"


def bdo(attrs=None, children=None):
    """ Overrides the current text direction """
    attrs, children = _prep_args(attrs, children)
    return f"<bdo{attrs}>{children}</bdo>"


def body(attrs=None, children=None):
    """ Defines the document's body """
    attrs, children = _prep_args(attrs, children)
    return f"<body{attrs}>{children}</body>"


def br(attrs=None, children=None):
    """ Defines a single line break """
    attrs, children = _prep_args(attrs, children)
    return f"<br{attrs}>{children}</br>"


def button(attrs=None, children=None):
    """ Defines a clickable button """
    attrs, children = _prep_args(attrs, children)
    return f"<button{attrs}>{children}</button>"


def canvas(attrs=None, children=None):
    """ Used to draw graphics, on the fly, via scripting (usually JavaScript) """
    attrs, children = _prep_args(attrs, children)
    return f"<canvas{attrs}>{children}</canvas>"


def caption(attrs=None, children=None):
    """ Defines a table caption """
    attrs, children = _prep_args(attrs, children)
    return f"<caption{attrs}>{children}</caption>"


def cite(attrs=None, children=None):
    """ Defines the title of a work """
    attrs, children = _prep_args(attrs, children)
    return f"<cite{attrs}>{children}</cite>"


def code(attrs=None, children=None):
    """ Defines a piece of computer code """
    attrs, children = _prep_args(attrs, children)
    return f"<code{attrs}>{children}</code>"


def col(attrs=None, children=None):
    """ Specifies column properties for each column within a <colgroup> element  """
    attrs, children = _prep_args(attrs, children)
    return f"<col{attrs}>{children}</col>"


def colgroup(attrs=None, children=None):
    """ Specifies a group of one or more columns in a table for formatting """
    attrs, children = _prep_args(attrs, children)
    return f"<colgroup{attrs}>{children}</colgroup>"


def datalist(attrs=None, children=None):
    """ Specifies a list of pre-defined options for input controls """
    attrs, children = _prep_args(attrs, children)
    return f"<datalist{attrs}>{children}</datalist>"


def dd(attrs=None, children=None):
    """ Defines a description/value of a term in a description list """
    attrs, children = _prep_args(attrs, children)
    return f"<dd{attrs}>{children}</dd>"


def del_(attrs=None, children=None):
    """ Defines text that has been deleted from a document """
    attrs, children = _prep_args(attrs, children)
    return f"<del{attrs}>{children}</del>"


def details(attrs=None, children=None):
    """ Defines additional details that the user can view or hide """
    attrs, children = _prep_args(attrs, children)
    return f"<details{attrs}>{children}</details>"


def dfn(attrs=None, children=None):
    """ Represents the defining instance of a term """
    attrs, children = _prep_args(attrs, children)
    return f"<dfn{attrs}>{children}</dfn>"


def dialog(attrs=None, children=None):
    """ Defines a dialog box or window """
    attrs, children = _prep_args(attrs, children)
    return f"<dialog{attrs}>{children}</dialog>"


def div(attrs=None, children=None):
    """ Defines a section in a document """
    attrs, children = _prep_args(attrs, children)
    return f"<div{attrs}>{children}</div>"


def dl(attrs=None, children=None):
    """ Defines a description list """
    attrs, children = _prep_args(attrs, children)
    return f"<dl{attrs}>{children}</dl>"


def dt(attrs=None, children=None):
    """ Defines a term/name in a description list """
    attrs, children = _prep_args(attrs, children)
    return f"<dt{attrs}>{children}</dt>"


def em(attrs=None, children=None):
    """ Defines emphasized text  """
    attrs, children = _prep_args(attrs, children)
    return f"<em{attrs}>{children}</em>"


def embed(attrs=None, children=None):
    """ Defines a container for an external (non-HTML) application """
    attrs, children = _prep_args(attrs, children)
    return f"<embed{attrs}>{children}</embed>"


def fieldset(attrs=None, children=None):
    """ Groups related elements in a form """
    attrs, children = _prep_args(attrs, children)
    return f"<fieldset{attrs}>{children}</fieldset>"


def figcaption(attrs=None, children=None):
    """ Defines a caption for a <figure> element """
    attrs, children = _prep_args(attrs, children)
    return f"<figcaption{attrs}>{children}</figcaption>"


def figure(attrs=None, children=None):
    """ Specifies self-contained content """
    attrs, children = _prep_args(attrs, children)
    return f"<figure{attrs}>{children}</figure>"


def footer(attrs=None, children=None):
    """ Defines a footer for a document or section """
    attrs, children = _prep_args(attrs, children)
    return f"<footer{attrs}>{children}</footer>"


def form(attrs=None, children=None):
    """ Defines an HTML form for user input """
    attrs, children = _prep_args(attrs, children)
    return f"<form{attrs}>{children}</form>"


def h1(attrs=None, children=None):
    """  Defines HTML headings """
    attrs, children = _prep_args(attrs, children)
    return f"<h1{attrs}>{children}</h1>"


def h2(attrs=None, children=None):
    """  Defines HTML headings """
    attrs, children = _prep_args(attrs, children)
    return f"<h2{attrs}>{children}</h2>"


def h3(attrs=None, children=None):
    """  Defines HTML headings """
    attrs, children = _prep_args(attrs, children)
    return f"<h3{attrs}>{children}</h3>"


def h4(attrs=None, children=None):
    """  Defines HTML headings """
    attrs, children = _prep_args(attrs, children)
    return f"<h4{attrs}>{children}</h4>"


def h5(attrs=None, children=None):
    """  Defines HTML headings """
    attrs, children = _prep_args(attrs, children)
    return f"<h5{attrs}>{children}</h5>"


def h6(attrs=None, children=None):
    """  Defines HTML headings """
    attrs, children = _prep_args(attrs, children)
    return f"<h6{attrs}>{children}</h6>"


def head(attrs=None, children=None):
    """ Defines information about the document """
    attrs, children = _prep_args(attrs, children)
    return f"<head{attrs}>{children}</head>"


def header(attrs=None, children=None):
    """ Defines a header for a document or section """
    attrs, children = _prep_args(attrs, children)
    return f"<header{attrs}>{children}</header>"


def hr(attrs=None, children=None):
    """  Defines a thematic change in the content """
    attrs, children = _prep_args(attrs, children)
    return f"<hr{attrs}>{children}</hr>"


def html(attrs=None, children=None):
    """ Defines the root of an HTML document """
    attrs, children = _prep_args(attrs, children)
    return f"<html{attrs}>{children}</html>"


def i(attrs=None, children=None):
    """ Defines a part of text in an alternate voice or mood """
    attrs, children = _prep_args(attrs, children)
    return f"<i{attrs}>{children}</i>"


def iframe(attrs=None, children=None):
    """ Defines an inline frame """
    attrs, children = _prep_args(attrs, children)
    return f"<iframe{attrs}>{children}</iframe>"


def img(attrs=None, children=None):
    """ Defines an image """
    attrs, children = _prep_args(attrs, children)
    return f"<img{attrs}>{children}</img>"


def input(attrs=None, children=None):
    """ Defines an input control """
    attrs, children = _prep_args(attrs, children)
    return f"<input{attrs}>{children}</input>"


def ins(attrs=None, children=None):
    """ Defines a text that has been inserted into a document """
    attrs, children = _prep_args(attrs, children)
    return f"<ins{attrs}>{children}</ins>"


def kbd(attrs=None, children=None):
    """ Defines keyboard input """
    attrs, children = _prep_args(attrs, children)
    return f"<kbd{attrs}>{children}</kbd>"


def keygen(attrs=None, children=None):
    """ Defines a key-pair generator field (for forms) """
    attrs, children = _prep_args(attrs, children)
    return f"<keygen{attrs}>{children}</keygen>"


def label(attrs=None, children=None):
    """ Defines a label for an <input> element """
    attrs, children = _prep_args(attrs, children)
    return f"<label{attrs}>{children}</label>"


def legend(attrs=None, children=None):
    """ Defines a caption for a <fieldset> element """
    attrs, children = _prep_args(attrs, children)
    return f"<legend{attrs}>{children}</legend>"


def li(attrs=None, children=None):
    """ Defines a list item """
    attrs, children = _prep_args(attrs, children)
    return f"<li{attrs}>{children}</li>"


def link(attrs=None, children=None):
    """ Defines the relationship between a document and an external resource (most used to link to style sheets) """
    attrs, children = _prep_args(attrs, children)
    return f"<link{attrs}>{children}</link>"


def main(attrs=None, children=None):
    """ Specifies the main content of a document """
    attrs, children = _prep_args(attrs, children)
    return f"<main{attrs}>{children}</main>"


def map(attrs=None, children=None):
    """ Defines a client-side image-map """
    attrs, children = _prep_args(attrs, children)
    return f"<map{attrs}>{children}</map>"


def mark(attrs=None, children=None):
    """ Defines marked/highlighted text """
    attrs, children = _prep_args(attrs, children)
    return f"<mark{attrs}>{children}</mark>"


def menu(attrs=None, children=None):
    """ Defines a list/menu of commands """
    attrs, children = _prep_args(attrs, children)
    return f"<menu{attrs}>{children}</menu>"


def menuitem(attrs=None, children=None):
    """ Defines a command/menu item that the user can invoke from a popup menu """
    attrs, children = _prep_args(attrs, children)
    return f"<menuitem{attrs}>{children}</menuitem>"


def meta(attrs=None, children=None):
    """ Defines metadata about an HTML document """
    attrs, children = _prep_args(attrs, children)
    return f"<meta{attrs}>{children}</meta>"


def meter(attrs=None, children=None):
    """ Defines a scalar measurement within a known range (a gauge) """
    attrs, children = _prep_args(attrs, children)
    return f"<meter{attrs}>{children}</meter>"


def nav(attrs=None, children=None):
    """ Defines navigation links """
    attrs, children = _prep_args(attrs, children)
    return f"<nav{attrs}>{children}</nav>"


def noscript(attrs=None, children=None):
    """ Defines an alternate content for users that do not support client-side scripts """
    attrs, children = _prep_args(attrs, children)
    return f"<noscript{attrs}>{children}</noscript>"


def object(attrs=None, children=None):
    """ Defines an embedded object """
    attrs, children = _prep_args(attrs, children)
    return f"<object{attrs}>{children}</object>"


def ol(attrs=None, children=None):
    """ Defines an ordered list """
    attrs, children = _prep_args(attrs, children)
    return f"<ol{attrs}>{children}</ol>"


def optgroup(attrs=None, children=None):
    """ Defines a group of related options in a drop-down list """
    attrs, children = _prep_args(attrs, children)
    return f"<optgroup{attrs}>{children}</optgroup>"


def option(attrs=None, children=None):
    """ Defines an option in a drop-down list """
    attrs, children = _prep_args(attrs, children)
    return f"<option{attrs}>{children}</option>"


def output(attrs=None, children=None):
    """ Defines the result of a calculation """
    attrs, children = _prep_args(attrs, children)
    return f"<output{attrs}>{children}</output>"


def p(attrs=None, children=None):
    """ Defines a paragraph """
    attrs, children = _prep_args(attrs, children)
    return f"<p{attrs}>{children}</p>"


def param(attrs=None, children=None):
    """ Defines a parameter for an object """
    attrs, children = _prep_args(attrs, children)
    return f"<param{attrs}>{children}</param>"


def pre(attrs=None, children=None):
    """ Defines preformatted text """
    attrs, children = _prep_args(attrs, children)
    return f"<pre{attrs}>{children}</pre>"


def progress(attrs=None, children=None):
    """ Represents the progress of a task """
    attrs, children = _prep_args(attrs, children)
    return f"<progress{attrs}>{children}</progress>"


def q(attrs=None, children=None):
    """ Defines a short quotation """
    attrs, children = _prep_args(attrs, children)
    return f"<q{attrs}>{children}</q>"


def rp(attrs=None, children=None):
    """ Defines what to show in browsers that do not support ruby annotations """
    attrs, children = _prep_args(attrs, children)
    return f"<rp{attrs}>{children}</rp>"


def rt(attrs=None, children=None):
    """ Defines an explanation/pronunciation of characters (for East Asian typography) """
    attrs, children = _prep_args(attrs, children)
    return f"<rt{attrs}>{children}</rt>"


def ruby(attrs=None, children=None):
    """ Defines a ruby annotation (for East Asian typography) """
    attrs, children = _prep_args(attrs, children)
    return f"<ruby{attrs}>{children}</ruby>"


def s(attrs=None, children=None):
    """ Defines text that is no longer correct """
    attrs, children = _prep_args(attrs, children)
    return f"<s{attrs}>{children}</s>"


def samp(attrs=None, children=None):
    """ Defines sample output from a computer program """
    attrs, children = _prep_args(attrs, children)
    return f"<samp{attrs}>{children}</samp>"


def script(attrs=None, children=None):
    """ Defines a client-side script """
    attrs, children = _prep_args(attrs, children)
    return f"<script{attrs}>{children}</script>"


def section(attrs=None, children=None):
    """ Defines a section in a document """
    attrs, children = _prep_args(attrs, children)
    return f"<section{attrs}>{children}</section>"


def select(attrs=None, children=None):
    """ Defines a drop-down list """
    attrs, children = _prep_args(attrs, children)
    return f"<select{attrs}>{children}</select>"


def small(attrs=None, children=None):
    """ Defines smaller text """
    attrs, children = _prep_args(attrs, children)
    return f"<small{attrs}>{children}</small>"


def source(attrs=None, children=None):
    """ Defines multiple media resources for media elements (<video> and <audio>) """
    attrs, children = _prep_args(attrs, children)
    return f"<source{attrs}>{children}</source>"


def span(attrs=None, children=None):
    """ Defines a section in a document """
    attrs, children = _prep_args(attrs, children)
    return f"<span{attrs}>{children}</span>"


def strong(attrs=None, children=None):
    """ Defines important text """
    attrs, children = _prep_args(attrs, children)
    return f"<strong{attrs}>{children}</strong>"


def style(attrs=None, children=None):
    """ Defines style information for a document """
    attrs, children = _prep_args(attrs, children)
    return f"<style{attrs}>{children}</style>"


def sub(attrs=None, children=None):
    """ Defines subscripted text """
    attrs, children = _prep_args(attrs, children)
    return f"<sub{attrs}>{children}</sub>"


def summary(attrs=None, children=None):
    """ Defines a visible heading for a <details> element """
    attrs, children = _prep_args(attrs, children)
    return f"<summary{attrs}>{children}</summary>"


def sup(attrs=None, children=None):
    """ Defines superscripted text """
    attrs, children = _prep_args(attrs, children)
    return f"<sup{attrs}>{children}</sup>"


def table(attrs=None, children=None):
    """ Defines a table """
    attrs, children = _prep_args(attrs, children)
    return f"<table{attrs}>{children}</table>"


def tbody(attrs=None, children=None):
    """ Groups the body content in a table """
    attrs, children = _prep_args(attrs, children)
    return f"<tbody{attrs}>{children}</tbody>"


def td(attrs=None, children=None):
    """ Defines a cell in a table """
    attrs, children = _prep_args(attrs, children)
    return f"<td{attrs}>{children}</td>"


def textarea(attrs=None, children=None):
    """ Defines a multiline input control (text area) """
    attrs, children = _prep_args(attrs, children)
    return f"<textarea{attrs}>{children}</textarea>"


def tfoot(attrs=None, children=None):
    """ Groups the footer content in a table """
    attrs, children = _prep_args(attrs, children)
    return f"<tfoot{attrs}>{children}</tfoot>"


def th(attrs=None, children=None):
    """ Defines a header cell in a table """
    attrs, children = _prep_args(attrs, children)
    return f"<th{attrs}>{children}</th>"


def thead(attrs=None, children=None):
    """ Groups the header content in a table """
    attrs, children = _prep_args(attrs, children)
    return f"<thead{attrs}>{children}</thead>"


def time(attrs=None, children=None):
    """ Defines a date/time """
    attrs, children = _prep_args(attrs, children)
    return f"<time{attrs}>{children}</time>"


def title(attrs=None, children=None):
    """ Defines a title for the document """
    attrs, children = _prep_args(attrs, children)
    return f"<title{attrs}>{children}</title>"


def tr(attrs=None, children=None):
    """ Defines a row in a table """
    attrs, children = _prep_args(attrs, children)
    return f"<tr{attrs}>{children}</tr>"


def track(attrs=None, children=None):
    """ Defines text tracks for media elements (<video> and <audio>) """
    attrs, children = _prep_args(attrs, children)
    return f"<track{attrs}>{children}</track>"


def u(attrs=None, children=None):
    """ Defines text that should be stylistically different from normal text """
    attrs, children = _prep_args(attrs, children)
    return f"<u{attrs}>{children}</u>"


def ul(attrs=None, children=None):
    """ Defines an unordered list """
    attrs, children = _prep_args(attrs, children)
    return f"<ul{attrs}>{children}</ul>"


def var(attrs=None, children=None):
    """ Defines a variable """
    attrs, children = _prep_args(attrs, children)
    return f"<var{attrs}>{children}</var>"


def video(attrs=None, children=None):
    """ Defines a video or movie """
    attrs, children = _prep_args(attrs, children)
    return f"<video{attrs}>{children}</video>"


def wbr(attrs=None, children=None):
    """ Defines a possible line-break """
    attrs, children = _prep_args(attrs, children)
    return f"<wbr{attrs}>{children}</wbr>"
