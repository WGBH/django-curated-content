===============
Curated Content
===============

Curated Content uses django-model-gatekeeper to provide "Set it and forget it!" behavior for content blocks.


Quick start
-----------

1. Add "gatekeeper" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'gatekeeper',
        'curated_content',
    ]

2. Run python manage.py migrate 

How to use it
-------------

This creates two new models:

* Curated Content Block
* Curated Content Instance

Each block is defines content that you want to re-use in templates, but want to REPLACE at different times.

For example if your project has an event or promotion, you'll want the content surrounding that event/promotion to appear
at a particular date/time but change or disappear at a later/date or time.   This software accommodates this need.

To start off:

1. Create a block
2. Add instances whose "content_block" is your block.
3. Use the Gatekeeper "publish_status" and "live_as_of" date to "set it and forget it".

Then:

4. In a template add {% load curated_content %} at the top;
5. Use {% curated_content "my-content-block-slug" as new_variable %} add new_variable to the context.
6. {{ new_variable }} where you want the curated content instance to appear.

Note that is NO instances of the content_block are live via the gatekeeper, then nothing will appear (the system will return an empty string).


See the project README for more-detailed instructions of use.
