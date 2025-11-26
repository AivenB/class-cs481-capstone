from django.urls import path
from . import views


# dashboard urls
DASHBOARD_URL = 'dashboard/'
COMMUNITY_URL = DASHBOARD_URL + 'community/'
ASSESSMENT_URL = DASHBOARD_URL + 'assessment/'
ANALYTICS_URL = DASHBOARD_URL + 'analytics/'
ABOUT_URL = DASHBOARD_URL + 'about/'

# url patterns for HTMX endpoints
urlpatterns = [
    # Main page routes
    path('', views.default_view, name='default'),
    path('start/', views.start_view, name='start'),
    path(DASHBOARD_URL, views.dashboard, name='dashboard'),
    path(ABOUT_URL, views.about, name='about'),
    
    # HTMX endpoints for dashboard updates
    path(DASHBOARD_URL + 'stats/', views.dashboard_stats, name='dashboard_stats'),
    path(DASHBOARD_URL + 'activity/', views.dashboard_activity, name='dashboard_activity'),
    
    # HTMX endpoints for community features
    path(COMMUNITY_URL, views.community, name='community'),
    path(COMMUNITY_URL + 'search/', views.community_search, name='community_search'),
    path(COMMUNITY_URL + 'filter/<str:filter_type>', views.community_filter, name='community_filter'),
    
    # Assessment routes
    path(ASSESSMENT_URL, views.assessment, name='assessment'),
    path(ASSESSMENT_URL + 'start-button/', views.show_start_assessment_button, name='show_start_assessment_button'),
    path(ASSESSMENT_URL + 'start/', views.start_assessment, name="assessment_start"),
    path(ASSESSMENT_URL + "next/", views.next_question, name="next_question"),
    path(ASSESSMENT_URL + "submit/", views.submit_assessment, name="submit_assessment"),

    # Analytics
    path(ANALYTICS_URL, views.analytics, name='analytics'),
    path(ANALYTICS_URL + 'filter/<str:filter_type>', views.analytics_filter, name='analytics_filter'),
    path('dashboard/profiles/filter/<str:filter_type>/', views.profiles_filter, name='profiles_filter'),

    # test partial view
    path('test_partial/', views.test_partial, name='test_partial'),
]
