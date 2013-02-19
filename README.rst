Feedback
========

Creates an ajax "feedback" button on your site, which pops up a form for the
user to fill.

+ Add it to your installed apps::

    INSTALLED_APPS += ('feedback',)

+ Configure settings

    + FEEDBACK_EMAIL_LIST
        If not set, no emails will be sent (feedback is stored in the
        database either way)
        Needs to be a list of email addresses ready for django's send_mail()
        function. A sane value may be derived from ADMINS or MANAGERS, eg:
        FEEDBACK_EMAIL_LIST = ['{} <{}>'.format(name, address) for name, address in MANAGERS]
        or, more simply [address for name, address in MANAGERS]

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
