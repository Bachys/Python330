from jinja2 import Template

html = """
{% macro set_input(type='', name='', placeholder='') %}
    <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
{% endmacro -%}

<p>{{ set_input('text', 'firstname', 'Имя')}}</p>
<p>{{ set_input('text', 'lastname', 'Фамилия')}}</p>
<p>{{ set_input('text', 'adress', 'Адрес')}}</p>
<p>{{ set_input('tel', 'phone', 'Телефон')}}</p>
<p>{{ set_input('email', 'email', 'Почта')}}</p>
"""


tm = Template(html)
msg = tm.render()
print(msg)