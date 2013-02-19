Feedback
========

Creates an ajax "feedback" button on your site, which pops up a form for the
user to fill.

+ Add it to your installed apps::

    INSTALLED_APPS += ('feedback',)


+ Sync the database

+ Include 'feedback.urls' in your urlconf somewhere

+ Include in your templates:

    <!-- with your css -->
        <link rel="stylesheet" href="{{ STATIC_URL }}feedback/main.css">

    <!-- with your scripts, after jquery -->
        <script src="{{ STATIC_URL }}feedback/jquery.form.js"></script>
        <script src="{{ STATIC_URL }}feedback/main.js"></script> 

    <!-- somewhere after that -->
        {% include "feedback/form.html" %}
