{% extends 'base.html' %}
{% load comment_extras %}

{% block main %}
    {% show_comment_form post form %}
{% endblock main %}
