from django.template import Template, Context


def render_template(section, context = {}):
    rendered_content = '<h1>No se puede renderizar</h1>'
    try:
        context['section'] = section
        template = Template(section.content)
        rendered_content = template.render(Context(context))
        context['section_rendered'] = rendered_content
    except Exception as ex:
        rendered_content += f'<br>{ex}'
    return rendered_content