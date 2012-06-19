from django import forms
from django.utils import simplejson as json


class StudySkillsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StudySkillsForm, self).__init__(*args, **kwargs)
        
        questions = [
        'I manage to find conditions for studying which allow me to get on with my work easily.',
        "When working on an assessment, I'm keeping in mind how best to inpress the Instructor.",
        'Often I find myself wondering whether the work I am doing here is really worthwhile.',
        'I usually set out to understand for myself the meaning of what we have to learn.',
        'I organize my study time carefully to make the best use of it.',
        'I find i have to concentrate on just memorizing a good deal of what we have to learn.',
        'I go over the work I have done carefullyto check the reasoning and that it makes sense.',
        'Often I feel I am drowning in the sheer amount of material we are having to cope with.',
        "I look at the evidence carefully and try to reach my own conclusion about what I’m studying.",
        "It’s important for me to feel that I’m doing as well as I really can on the courses here.",
        "I try to relate ideas I come across to those in other topics or other courses whenever possible.",
        "I tend to read very little beyond what is actually required to pass.",
        "Regularly I find myself thinking about ideas from lectures when I’m doing other things.",
        "I think I’m quite systematic and organised when it comes to revising for exams.",
        "I look carefully at tutors’ comments on course work to see how to get higher marks next time.",
        "There’s not much of the work here that I find interesting or relevant.",
        "When I read an article or book, I try to find out for myself exactly what the author means.",
        "I’m pretty good at getting down to work whenever I need to.",
        "Much of what I’m studying makes little sense: it’s like unrelated bits and pieces.",
        "I think about what I want to get out of this course to keep my studying well focused.",
        "When I’m working on a new topic, I try to see in my own mind how all the ideas fit together.",
        "I often worry about whether I’ll ever be able to cope with the work properly.",
        "Often I find myself questioning things I hear in lectures or read in books.",
        "I feel that I’m getting on well, and this helps me put more effort into the work.",
        "I concentrate on learning just those bits of information I have to know to pass.",
        "I find that studying academic topics can be quite exciting at times.",
        "I’m good at following up some of the reading suggested by lecturers or tutors.",
        "I keep in mind who is going to mark an assignment and what they’re likely to be looking for.",
        "When I look back, I sometimes wonder why I ever decided to come here.",
        "When I am reading, I stop from time to time to reflect on what I am trying to learn from it.",
        "I work steadily through the term or semester, rather than leave it all until the last minute.",
        "I’m not really sure what’s important in lectures so I try to get down all I can.",
        "Ideas in course books or articles often set me off on long chains of thought of my own.",
        "Before starting work on an assignment or exam question, I think first how best to tackle it.",
        "I often seem to panic if I get behind with my work.",
        "When I read, I examine the details carefully to see how they fit in with what’s being said.",
        "I put a lot of effort into studying because I’m determined to do well.",
        "I gear my studying closely to just what seems to be required for assignments and exams.",
        "Some of the ideas I come across on the course I find really gripping.",
        "I usually plan out my week’s work in advance, either on paper or in my head.",
        "I keep an eye open for what lecturers seem to think is important and concentrate on that.",
        "I’m not really interested in this course, but I have to take it for other reasons.",
        "Before tackling a problem or assignment, I first try to work out what lies behind it.",
        "I generally make good use of my time during the day.",
        "I often have trouble in making sense of the things I have to remember.",
        "I like to play around with ideas of my own even if they don’t get me very far.",
        "When I finish a piece of work, I check it through to see if it really meets the requirements.",
        "Often I lie awake worrying about work I think I won’t be able to do.",
        "It’s important for me to be able to follow the argument, or to see the reason behind things.",
        "I don’t find it at all difficult to motivate myself.",
        "I like to be told precisely what to do in essays or other assignments.",
        "I sometimes get ‘hooked’ on academic topics and feel I would like to keep on studying them."
        ]
        preferences =[
        "lecturers who tell us exactly what to put down in our notes.",
        "lecturers who encourage us to think for ourselves and show us how they themselves think.",
        "exams which allow me to show that I’ve thought about the course material for myself.",
        "exams or tests which need only the material provided in our lecture notes.",
        "courses in which it’s made very clear just which books we have to read.",
        "courses where we’re encouraged to read around the subject a lot for ourselves.",
        "books which challenge you and provide explanations which go beyond the lectures.",
        "books which give you definite facts and information which can easily be learned.",
        "How well do you think you have been doing in your assessed work overall, so far?"
        ]
        assess = [
        "How well do you think you have been doing in your assessed work overall, so far?"
        ]

        i = 1
        for question in questions:
            label = question
            choices = [(1, 'Strongly Disagree'),(2,'Disagree'),(3,'Neither Agree Nor Disagree'),(4,'Agree'),(5,'Strongly Agree')]
            field = forms.ChoiceField(label=label, choices=choices,
                    widget=forms.RadioSelect, required=True)
            self.fields['%d' % i] = field
            i += 1
        for question in preferences:
            label = question
            choices = [(1, 'Hate'),(2,'Dislike'),(3,'No Preference'),(4,'Like'),(5,'Love')]
            field = forms.ChoiceField(label=label, choices=choices,
                    widget=forms.RadioSelect, required=True)
            self.fields['%d' % i] = field
            i += 1
        for question in assess:
            label = question
            choices = [(1, 'Badly'),(2,'Not So Well'),(3,'Average'),(4,'Well'),(5,'Excellent')]
            field = forms.ChoiceField(label=label, choices=choices,
                    widget=forms.RadioSelect, required=True)
            self.fields['%d' % i] = field
            i += 1
