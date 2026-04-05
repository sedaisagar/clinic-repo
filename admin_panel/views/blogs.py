from django.views import generic

from admin_panel.permissions import AdminLoginRequiredMixin
from mainapp.models import BlogCategories, BlogTags, Blogs
from django.urls import reverse_lazy
from django.contrib import messages

# Categories
class BlogCategoriesListView(AdminLoginRequiredMixin,generic.ListView):
    template_name = "admin-panel/common/list.html"
    queryset = BlogCategories.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["name"]
        data["title"] = "Blog Categories"
        data["actions"] = ["create", "edit", "delete"]
        return data


class BlogCategoriesCreateView(AdminLoginRequiredMixin,generic.CreateView):
    template_name = "admin-panel/common/forms.html"
    queryset = BlogCategories.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-cat-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Add New Category"
        return data

    def get_success_url(self):
        messages.success(self.request, "Category Created Successfully!")
        return super().get_success_url()

class BlogCategoriesUpdateView(AdminLoginRequiredMixin,generic.UpdateView):
    template_name = "admin-panel/common/forms.html"
    queryset = BlogCategories.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-cat-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Update Category"
        return data

    def get_success_url(self):
        messages.success(self.request, "Category Updated Successfully!")
        return super().get_success_url()

class BlogCategoriesDeleteView(AdminLoginRequiredMixin,generic.DeleteView):
    template_name = "admin-panel/common/forms.html"
    queryset = BlogCategories.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-cat-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete This Category ?"
        return data


    def get_success_url(self):
        messages.success(self.request, "Category Deleted Successfully!")
        return super().get_success_url()



# Tags
from tinymce.widgets import TinyMCE

class BlogTagsListView(AdminLoginRequiredMixin,generic.ListView):
    template_name = "admin-panel/common/list.html"
    queryset = BlogTags.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["name"]
        data["title"] = "Blog Tags"
        data["actions"] = ["create", "edit", "delete"]
        return data


class BlogTagsCreateView(AdminLoginRequiredMixin,generic.CreateView):
    template_name = "admin-panel/common/forms.html"
    queryset = BlogTags.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-tag-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Add New Tag"
        return data

    def get_success_url(self):
        messages.success(self.request, "Tag Created Successfully!")
        return super().get_success_url()
    
    

class BlogTagsUpdateView(AdminLoginRequiredMixin,generic.UpdateView):
    template_name = "admin-panel/common/forms.html"
    queryset = BlogTags.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-tag-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Update Tag"
        return data

    def get_success_url(self):
        messages.success(self.request, "Tag Updated Successfully!")
        return super().get_success_url()
    
    

class BlogTagsDeleteView(AdminLoginRequiredMixin,generic.DeleteView):
    template_name = "admin-panel/common/forms.html"
    queryset = BlogTags.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-tag-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete This Tag ?"
        return data


    def get_success_url(self):
        messages.success(self.request, "Tag Deleted Successfully!")
        return super().get_success_url()


# Blogs



class BlogsListView(AdminLoginRequiredMixin,generic.ListView):
    template_name = "admin-panel/common/list.html"
    queryset = Blogs.objects.all()

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["fields"] = ["title"]
        data["title"] = "Blogs"
        data["actions"] = ["create", "edit", "delete"]
        return data


class BlogsCreateView(AdminLoginRequiredMixin,generic.CreateView):
    template_name = "admin-panel/common/forms.html"
    queryset = Blogs.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Add New Blog"
        return data

    def get_success_url(self):
        messages.success(self.request, "Blog Created Successfully!")
        return super().get_success_url()
    
    def get_form(self):
        form =  super().get_form()
        form.fields['description'].widget = TinyMCE(attrs={'cols': 80, 'rows': 30})
        return form

class BlogsUpdateView(AdminLoginRequiredMixin,generic.UpdateView):
    template_name = "admin-panel/common/forms.html"
    queryset = Blogs.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Update Blog"
        return data

    def get_success_url(self):
        messages.success(self.request, "Blog Updated Successfully!")
        return super().get_success_url()
    
    def get_form(self):
        form =  super().get_form()
        form.fields['description'].widget = TinyMCE(attrs={'cols': 80, 'rows': 30})
        return form

class BlogsDeleteView(AdminLoginRequiredMixin,generic.DeleteView):
    template_name = "admin-panel/common/forms.html"
    queryset = Blogs.objects.all()
    fields = "__all__"
    success_url = reverse_lazy("admin-blog-page")

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["title"] = "Delete This Blog ?"
        return data


    def get_success_url(self):
        messages.success(self.request, "Blog Deleted Successfully!")
        return super().get_success_url()
