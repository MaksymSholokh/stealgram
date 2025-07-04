


from .forms import PostForm


def instance_post(page_obj): 
    inst_forms = {} 

    for post in page_obj: 
        form = PostForm(instance=post)  
        inst_forms[post.id] = form 
    return inst_forms