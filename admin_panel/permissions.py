from django.contrib.auth.mixins import LoginRequiredMixin


class AdminLoginRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if not (request.user.role == "ADMIN"):
            return self.handle_no_permission()
            
        return super().dispatch(request, *args, **kwargs)