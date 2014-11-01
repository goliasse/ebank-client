from django.conf.urls import patterns, url, include


urlpatterns = patterns(
    'apps.main.views.main',
    url(r'^$', 'index'),
    url(r'^template/(?P<template_name>.+)$', 'template'),
)

urlpatterns += patterns(
    'apps.main.views.api',
    url(r'^api/change-password$', 'change_password'),
    url(r'^api/info$', 'get_info'),
    url(r'^api/currency$', 'get_currency'),
    url(r'^api/notifications$', 'get_notifications'),
    url(r'^api/erip/tree$', 'erip_tree'),
    url(r'^api/pay$', 'pay'),
)

urlpatterns += patterns(
    'apps.main.views.bank_api',
    url(r'^bank-api/notify$', 'notify'),
)

urlpatterns += patterns(
    'apps.main.views.auth',
    url(r'^auth/login$', '_login'),
    url(r'^auth/logout$', '_logout'),
)
