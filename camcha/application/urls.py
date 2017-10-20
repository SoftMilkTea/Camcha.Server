from django.conf.urls import url
from application import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^detections/$',
        views.DetectionList.as_view(),
        name='detection-list'),
    url(r'^detections/(?P<pk>[0-9]+)/$',
        views.DetectionDetail.as_view(),
        name='detection-detail'),
    url(r'^$',views.api_root),

    url(r'^detection_map/$',views.detection_map),  # 지도
    ]

urlpatterns = format_suffix_patterns(urlpatterns)