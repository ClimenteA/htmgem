import os
import re
import json
import keyword


prep_template = """#This module generates html function tags (needs to run only once)
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
    
       
"""


with open("html5_tags.json", "r") as f:
    html5_tags = json.load(f)

reserved_keywords = keyword.kwlist + dir(__builtins__)


tag_funcs = []
tag_funcs.append(prep_template)


for t in html5_tags:
    tag_name = re.match(r'<([a-z1-6]*)>', t['tag']).group(1)
    if tag_name in reserved_keywords: tag_name = tag_name + "_"
    
    start_tag = t['tag'][:-1]
    end_tag   = t['tag'].replace('<', '</')
    doc_tag = t['desc']
    
    tag = f"""
def {tag_name}(attrs=None, children=None):
    \""" {doc_tag} \"""
    attrs, children = _prep_args(attrs, children)
    return f"{start_tag}{{attrs}}>{{children}}{end_tag}"
"""
    tag_funcs.append(tag)
    

with open("tags.py", "w") as f:
    f.write("\n".join(tag_funcs))


