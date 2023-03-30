{% extends "base.html" %}
{% load crispy_forms_filters %}

{% block content %}

  {% if form.errors %}
    <p>Your username and password didn't match. Please try again.</p>
  {% endif %}

  <h1>Login</h1>

  {% if next %}
    <p>Please login to see this page.</p>
  {% endif %}

  <form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    {{ form|crispy }}

    <input type="submit" value="Login" class="btn btn-primary" />
    <input type="hidden" name="next" value="{{ next }}" />
  </form>

{% endblock %}