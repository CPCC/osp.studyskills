import os

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.template import Template
from django.utils import simplejson as json
from django.core.exceptions import PermissionDenied
from django.views.generic.simple import direct_to_template

from studyskills import models
from studyskills import forms

@login_required
def study_skills_show_assessment(request):
    """
        Displays the Study Skills Assessment.
    """
    if not request.user.groups.filter(name__in=['Students', 'Employees']):
        raise PermissionDenied

    if request.method == 'POST':
       form = forms.StudySkillsForm(request.POST)
       # Save the student's responses to the questions - answers will
       # be stored as a json formatted string.
       if form.is_valid():
           answers = []
           for item in form.cleaned_data:
               if item in form.fields:
                   # Retrieve the scoring category and sub-category from
                   # field attributes for this field and save them with
                   # the answer as they'll be needed for scoring purposes.
                   field_attrs = form.fields[item].widget.attrs
                   if 'score_category' in field_attrs:
                       score_category = field_attrs["score_category"]
                   else:
                       score_category = ""
                   if 'score_subcategory' in field_attrs:
                       score_subcategory = field_attrs["score_subcategory"]
                   else:
                       score_subcategory = ""
                   answers.append({'question': form.fields[item].label,
                                   'answer': form.cleaned_data[item],
                                   'question_id': item,
                                   'score_category': score_category,
                                   'score_subcategory': score_subcategory})
           answers = json.dumps(answers)
           result = models.StudySkillsResult(
               student = request.user,
               answers = answers
           )
           result.save()
           # Display the results of the assessment based on the student's
           # responses (or a message indicating successful submission, etc.).
           return redirect('assessment:study-skills-get-result',
                   result_id=result.pk)
    else:
       form = forms.StudySkillsForm()
    return direct_to_template(request,
                              'studyskills/study-skills.html',
                              {'form': form})

@login_required
def study_skills_student_results(request, student_id):
    """
        Retrieves the assessment result records for the specified student.
    """
    if not request.user.groups.filter(name__in=['Students', 'Employees']):
        raise PermissionDenied

    # Make sure the logged-in user should have access to these results
    if (not request.user.groups.filter(name='Employees') and
        int(student_id) != request.user.id):
        raise PermissionDenied

    results = models.StudySkillsResult.objects.filter(student=student_id)
    # return direct_to_template(request,
    #                           'studyskills/study-skills-student-results.html',
    #                           {'results': results,})

    json_data = []
    for result in results:
        json_data.append({'id': result.pk,
                          'date_taken': '%s' % result.date_taken})
    json_data = json.dumps(json_data)
    return HttpResponse(json_data)


@login_required
def study_skills_get_result(request, result_id):
    """
        Retrieves the specified assessment result record, scores it,
        and displays the outcome.
    """
    if not request.user.groups.filter(name__in=['Students', 'Employees']):
        raise PermissionDenied

    result = get_object_or_404(models.StudySkillsResult, id=result_id)

    # Make sure the logged-in user should have access to these results
    if (not request.user.groups.filter(name='Employees') and
        result.student != request.user):
        raise PermissionDenied

    answers = json.loads(result.answers)

    # Create dictionaries for storing totals that will be used to
    # calculate scores and subscores
    scores = {'D': {'total': 0, 'count_total': 0},
              'S': {'total': 0, 'count_total': 0},
              'A': {'total': 0, 'count_total': 0},
              'P': {'total': 0, 'count_total': 0}
             } 
    subscores = {'DS': {'total': 0, 'count_total': 0},
                 'DR': {'total': 0, 'count_total': 0},
                 'DE': {'total': 0, 'count_total': 0},
                 'DI': {'total': 0, 'count_total': 0},
                 'SO': {'total': 0, 'count_total': 0},
                 'ST': {'total': 0, 'count_total': 0},
                 'SD': {'total': 0, 'count_total': 0},
                 'SA': {'total': 0, 'count_total': 0},
                 'SM': {'total': 0, 'count_total': 0},
                 'AL': {'total': 0, 'count_total': 0},
                 'AU': {'total': 0, 'count_total': 0},
                 'AS': {'total': 0, 'count_total': 0},
                 'AF': {'total': 0, 'count_total': 0},
                 'PS': {'total': 0, 'count_total': 0},
                 'PT': {'total': 0, 'count_total': 0}
                }

    # Process each of the student's answers
    for answer in answers:
        if 'score_category' in answer and 'score_subcategory' in answer:
            if answer['score_category'] != '' and answer['score_subcategory'] != '':
                subscores[answer['score_category']+answer['score_subcategory']]['total']+=float(answer['answer'])
                subscores[answer['score_category']+answer['score_subcategory']]['count_total']+=15
            
                scores[answer['score_category']]['total']+=float(answer['answer'])
                scores[answer['score_category']]['count_total']+=15    

    # Compile the information and calculate the actual scores
    compiled_scores = [{'category':'Deep approach', 'score': scores['D']['total'] / scores['D']['count_total'] * 100,
                                  'sub_cats': [{'sub_cat': 'Seeking meaning', 'sub_cat_score': subscores['DS']['total'] / subscores['DS']['count_total'] * 100},
                                               {'sub_cat': 'Relating ideas', 'sub_cat_score': subscores['DR']['total'] / subscores['DR']['count_total'] * 100},
                                               {'sub_cat': 'Use of evidence', 'sub_cat_score': subscores['DE']['total'] / subscores['DE']['count_total'] * 100},
                                               {'sub_cat': 'Interest in ideas', 'sub_cat_score': subscores['DI']['total'] / subscores['DI']['count_total'] * 100}
                                              ]
                           },
                           {'category':'Strategic approach', 'score': scores['S']['total'] / scores['S']['count_total'] * 100,
                                  'sub_cats': [{'sub_cat': 'Organized studying', 'sub_cat_score': subscores['SO']['total'] / subscores['SO']['count_total'] * 100},
                                               {'sub_cat': 'Time management', 'sub_cat_score': subscores['ST']['total'] / subscores['ST']['count_total'] * 100},
                                               {'sub_cat': 'Alertness to assessment demands', 'sub_cat_score': subscores['SD']['total'] / subscores['SD']['count_total'] * 100},
                                               {'sub_cat': 'Achieving', 'sub_cat_score': subscores['SA']['total'] / subscores['SA']['count_total'] * 100},
                                               {'sub_cat': 'Monitoring effectiveness', 'sub_cat_score': subscores['SM']['total'] / subscores['SM']['count_total'] * 100}
                                              ]
                           },
                           {'category':'Surface apathetic approach', 'score': scores['A']['total'] / scores['A']['count_total'] * 100,
                                  'sub_cats': [{'sub_cat': 'Lack of purpose', 'sub_cat_score': subscores['AL']['total'] / subscores['AL']['count_total'] * 100},
                                               {'sub_cat': 'Unrelated memorizing', 'sub_cat_score': subscores['AU']['total'] / subscores['AU']['count_total'] * 100},
                                               {'sub_cat': 'Syllabus-boundness', 'sub_cat_score': subscores['AS']['total'] / subscores['AS']['count_total'] * 100},
                                               {'sub_cat': 'Fear of failure', 'sub_cat_score': subscores['AF']['total'] / subscores['AF']['count_total'] * 100}
                                              ]
                           },
                           {'category':'Preferences for different types of course and teaching', 'score': scores['P']['total'] / scores['P']['count_total'] * 100,
                                  'sub_cats': [{'sub_cat': 'Supporting understanding', 'sub_cat_score': subscores['PS']['total'] / subscores['PS']['count_total'] * 100},
                                               {'sub_cat': 'Transmitting information', 'sub_cat_score': subscores['PT']['total'] / subscores['PT']['count_total'] * 100}
                                              ]
                           }
                      ]

    # Display the results
    return direct_to_template(request, 'studyskills/study-skills-result.html', {'scores': compiled_scores})
