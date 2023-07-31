{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon">
<!--  <link href="css/bootstrap.min.css" rel="stylesheet">-->
  <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'css/fontello.css' %}">
  <title>{% block title %}Index{% endblock %}</title>
</head>

<body>
{% block content %}
{% endblock %}

{% block script %}
<script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
{% endblock %}
</body>

</html>