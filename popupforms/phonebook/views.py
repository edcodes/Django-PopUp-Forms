from django.shortcuts import render
from .models import PhoneBook

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import ListView, DetailView, CreateView , UpdateView, DeleteView
from bootstrap_modal_forms.generic import BSModalReadView, BSModalCreateView, BSModalUpdateView, BSModalDeleteView

from .forms import PhoneBookModelForm
from django.urls import reverse_lazy



class PhoneBookList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "stones.view_phonebook"
    model = PhoneBook    
    context_object_name = 'PhoneBooks'
    ordering = ['name']
    paginate_by = 20
    template_name = 'phonebook/phonebook_list.html'


class PhoneBookReadPopup(LoginRequiredMixin,PermissionRequiredMixin,BSModalReadView):
    permission_required = "stones.view_phonebook"
    model = PhoneBook
    template_name = 'phonebook/phonebook_detail_popup.html'



class PhoneBookCreatePopup(LoginRequiredMixin,PermissionRequiredMixin,BSModalCreateView):
    permission_required = "stones.add_phonebook"
    template_name = 'phonebook/phonebook_form_popup.html'
    form_class = PhoneBookModelForm
    success_message = 'Success: Shape was Created.'
    
    
    def form_valid(self, form):
        form.instance.creator = self.request.user        
        return super().form_valid(form) 

    def get_success_url(self):
        return reverse_lazy('phonebook-list')



class PhoneBookUpdatePopup(LoginRequiredMixin,PermissionRequiredMixin,BSModalUpdateView):
    permission_required = "stones.change_phonebook"
    model = PhoneBook
    template_name = 'phonebook/phonebook_form_popup.html'
    form_class = PhoneBookModelForm
    success_message = 'Success: Shape was Updated.'
    
    def get_success_url(self):
        return reverse_lazy('phonebook-list')
    
    
class PhoneBookDeletePopup(LoginRequiredMixin,PermissionRequiredMixin,BSModalDeleteView):
    permission_required = "stones.delete_phonebook"
    template_name = 'phonebook/phonebook_delete_popup.html'
    model = PhoneBook
    success_message = 'Success: Shape was Deleted.'    

    def get_success_url(self):
        return reverse_lazy('phonebook-list')