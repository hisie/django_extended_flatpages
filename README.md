Django Extended Flatpages

============================

Installing:

pip install django_extended_flatpages

In settings:


INSTALLED_APPS = (
	...
    'django.contrib.flatpages',
	...
    'ckeditor',
    'extended_flatpages',
    ...
)


MIDDLEWARE_CLASSES = (
	...
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
	...
)

Configure CKeditor

https://github.com/shaunsephton/django-ckeditor#installation

settings.py

# ckeditor config
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT + '/editor'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
                    [ 'Source','-','Save','-', 'Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo', '-', 'Find','Replace','-','SelectAll'], 
                    [ 'Bold','Italic','Underline','Strike','Subscript','Superscript','-','RemoveFormat' ] ,'/',
                    [ 'NumberedList','BulletedList','-','Outdent','Indent','-','Blockquote','CreateDiv','-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock','-','BidiLtr','BidiRtl' ], 
                    [ 'Link','Unlink' ],
                    [ 'Image','Table','HorizontalRule','SpecialChar' ],
                    [ 'Format'],
                    [ 'TextColor','BGColor', '-', 'Styles','Format','FontSize' ],
                    [ 'Maximize', 'ShowBlocks','-','About' ],
                ],
        'format_tags': 'p;h1;h2;h3;h4;h5;h6;pre;address;div',
    },
}

urls.py

(r'^ckeditor/', include('ckeditor.urls')),

And finally create a 

/templates/flatpages/default.html template to get working this.
    
