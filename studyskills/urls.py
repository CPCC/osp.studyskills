from django.conf.urls.defaults import *

from studyskills import views

urlpatterns = patterns('',
    (r'^show/$', views.study_skills_show_assessment, {}, 'study-skills-show-assessment'),
    (r'^get/results/(?P<student_id>\d+)/$', views.study_skills_student_results, {}, 'study-skills-student-results'),
    (r'^get/result-initial/(?P<result_id>\d+)/$', views.study_skills_get_result, {'is_initial':True}, 'study-skills-get-result-initial'),
    (r'^get/result/(?P<result_id>\d+)/$', views.study_skills_get_result, {'is_initial':False}, 'study-skills-get-result'),
)
