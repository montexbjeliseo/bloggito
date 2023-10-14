from typing import Any
from django.db import transaction
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.template import Template, Context
from .models import SectionContent
from .forms import SectionContentForm, ImageFormSet


class BlogIndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        home_section = SectionContent.objects.filter(
            parent='home')

        if len(home_section) > 0:
            home_section = home_section.first()
            context['home_section'] = home_section
            template = Template(home_section.content)
            rendered_content = template.render(Context(context))
            context['home_section_rendered'] = rendered_content
        
        return context


class SectionContentListView(ListView):
    model = SectionContent
    template_name = 'sections/list.html'
    context_object_name = 'sections'


class SectionContentCreateView(CreateView):
    model = SectionContent
    form_class = SectionContentForm
    template_name = 'sections/create.html'
    success_url = reverse_lazy('list_sections')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ImageFormSet(
                self.request.POST, self.request.FILES)
        else:
            context['formset'] = ImageFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)


class SectionContentUpdateView(UpdateView):
    model = SectionContent
    template_name = 'sections/update.html'
    form_class = SectionContentForm
    success_url = reverse_lazy('list_sections')


class SectionContentDeleteView(DeleteView):
    model = SectionContent
    template_name = "sections/delete.html"
    context_object_name = 'section'
    success_url = reverse_lazy('list_sections')