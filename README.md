# Curated Content

This is a simple Django app that adds functionality to `django-model-gatekeeper`.

It creates two models:

1.  `CuratedContentBlock`
2.  `CuratedContentInstance`

Basically you create 1 or more instances that are assigned to blocks.   You reference blocks in templates, and the "correct" instance will appear depending on it's Gatekeeper  `publish_status` and `live_as_of` date.

## Quick start

1. `pip install django-curated-content`
2. You must have "gatekeeper" and "curated_content" in your INSTALLED_APPS.

    ```
    INSTALLED_APPS = [
        ...
        'gatekeeper',
        'curated_content',
    ]
    ```
    
3.  `python manage.py migrate`  to create the models.

# Gatekeeping Content

The main use for gatekeeping is where you have a model with many instances, but you only want some to be "live" on the site.

Please refer to the `django-model-gatekeeper` documentation on how gatekeeping works.

## Curated Content Blocks

These define a block of content that you'll want to appear within one or more templates, but that you want to update automatically on the site per a pre-arranged schedule.

For example if your site has a promotion, you might want content that announces it prior to the start ("New Feature Coming Soon!"), that changes when the promotion starts ("Check out our New Feature"), and again one or more times during the promotion ("Get 20% off!  Promotion Ending Soon"), and disappears after the promotion.

By creating a content block, you can make content instance for each of these circumstances, set a `live_as_of` date, and the content will cycle through as directed.

## Curated Content Instances

For each content block, no more than one instance will ever be live at any time.  (It is entirely possible, and sometimes desired/necessary to have NO instances live.)

You can see which instance is "live" on the Curated Content Instances admin listing page.

## Using Curated Content in a Template

Rendering Curated Content is done through a template tag, `curated_content`.

1. First add {% load curated_content %} at the top of the template.

2. Set the context to include the curated content: here the content block is `my-content-blog-slug`: 
    `{% curated_content 'my-content-blog-slug' as promo_banner %}`
    
3. Use the updated context where desired:  `{{ promo_banner }}`.




# Testing

TBD.

# Troubleshooting

TBD.

# Features still to be integrated

1. Admin Preview

2. Markdown, HTML, etc.


