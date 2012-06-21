from django import forms
from django.utils import simplejson as json


class StudySkillsForm(forms.Form):
    """
        This form provides the questions to be asked on the assessment. Each field is
        also going to have two additional attributes, category and subcategory, that
        will pertain to how the responses to the questions need to be grouped for scoring
        purposes. Each inner list will be of the format [question, category, subcategory].
        To see what the letter codes mean, look in the study_skills_get_result view at
        the compiled scores dictionary.
    """
    def __init__(self, *args, **kwargs):
        super(StudySkillsForm, self).__init__(*args, **kwargs)
        
        questions = [
        ["I manage to find conditions for studying which allow me to get on with my work easily.", "S", "O"],
        ["When working on an assessment, I am keeping in mind how best to inpress the Instructor.", "S", "D"],
        ["Often I find myself wondering whether the work I am doing here is really worthwhile.", "A", "L"],
        ["I usually set out to understand for myself the meaning of what we have to learn.", "D", "S"],
        ["I organize my study time carefully to make the best use of it.", "S", "T"],
        ["I find i have to concentrate on just memorizing a good deal of what we have to learn.", "A", "U"],
        ["I go over the work I have done carefullyto check the reasoning and that it makes sense.", "S", "M"],
        ["Often I feel I am drowning in the sheer amount of material we are having to cope with.", "A", "F"],
        ["I look at the evidence carefully and try to reach my own conclusion about what I am studying.", "D", "E"],
        ["It is important for me to feel that I am doing as well as I really can on the courses here.", "S", "A"],
        ["I try to relate ideas I come across to those in other topics or other courses whenever possible.", "D", "R"],
        ["I tend to read very little beyond what is actually required to pass.", "A", "S"],
        ["Regularly I find myself thinking about ideas from lectures when I am doing other things.", "D", "I"],
        ["I think I am quite systematic and organised when it comes to revising for exams.", "S", "O"],
        ["I look carefully at tutors comments on course work to see how to get higher marks next time.", "S", "D"],
        ["There is not much of the work here that I find interesting or relevant.", "A", "L"],
        ["When I read an article or book, I try to find out for myself exactly what the author means.", "D", "S"],
        ["I am pretty good at getting down to work whenever I need to.", "S", "T"],
        ["Much of what I am studying makes little sense: it is like unrelated bits and pieces.", "A", "U"],
        ["I think about what I want to get out of this course to keep my studying well focused.", "S", "M"],
        ["When I am working on a new topic, I try to see in my own mind how all the ideas fit together.", "D", "R"],
        ["I often worry about whether I will ever be able to cope with the work properly.", "A", "F"],
        ["Often I find myself questioning things I hear in lectures or read in books.", "D", "E"],
        ["I feel that I am getting on well, and this helps me put more effort into the work.", "S", "A"],
        ["I concentrate on learning just those bits of information I have to know to pass.", "A", "S"],
        ["I find that studying academic topics can be quite exciting at times.", "D", "I"],
        ["I am good at following up some of the reading suggested by lecturers or tutors.", "S", "O"],
        ["I keep in mind who is going to mark an assignment and what they are likely to be looking for.", "S", "D"],
        ["When I look back, I sometimes wonder why I ever decided to come here.", "A", "L"],
        ["When I am reading, I stop from time to time to reflect on what I am trying to learn from it.", "D", "S"],
        ["I work steadily through the term or semester, rather than leave it all until the last minute.", "S", "T"],
        ["I am not really sure what is important in lectures so I try to get down all I can.", "A", "U"],
        ["Ideas in course books or articles often set me off on long chains of thought of my own.", "D", "R"],
        ["Before starting work on an assignment or exam question, I think first how best to tackle it.", "S", "M"],
        ["I often seem to panic if I get behind with my work.", "A", "F"],
        ["When I read, I examine the details carefully to see how they fit in with what is being said.", "D", "E"],
        ["I put a lot of effort into studying because I am determined to do well.", "S", "A"],
        ["I gear my studying closely to just what seems to be required for assignments and exams.", "A", "S"],
        ["Some of the ideas I come across on the course I find really gripping.", "D", "I"],
        ["I usually plan out my weeks work in advance, either on paper or in my head.", "S", "O"],
        ["I keep an eye open for what lecturers seem to think is important and concentrate on that.", "S", "D"],
        ["I am not really interested in this course, but I have to take it for other reasons.", "A", "L"],
        ["Before tackling a problem or assignment, I first try to work out what lies behind it.", "D", "S"],
        ["I generally make good use of my time during the day.", "S", "T"],
        ["I often have trouble in making sense of the things I have to remember.", "A", "U"],
        ["I like to play around with ideas of my own even if they do not get me very far.", "D", "R"],
        ["When I finish a piece of work, I check it through to see if it really meets the requirements.", "S", "M"],
        ["Often I lie awake worrying about work I think I will not be able to do.", "A", "F"],
        ["It is important for me to be able to follow the argument, or to see the reason behind things.", "D", "E"],
        ["I do not find it at all difficult to motivate myself.", "S", "A"],
        ["I like to be told precisely what to do in essays or other assignments.", "A", "S"],
        ["I sometimes get hooked on academic topics and feel I would like to keep on studying them.", "D", "I"]
        ]
        preferences =[
        ["lecturers who tell us exactly what to put down in our notes.", "P", "T"],
        ["lecturers who encourage us to think for ourselves and show us how they themselves think.", "P", "S"],
        ["exams which allow me to show that I have thought about the course material for myself.", "P", "S"],
        ["exams or tests which need only the material provided in our lecture notes.", "P", "T"],
        ["courses in which it is made very clear just which books we have to read.", "P", "T"],
        ["courses where we are encouraged to read around the subject a lot for ourselves.", "P", "S"],
        ["books which challenge you and provide explanations which go beyond the lectures.", "P", "S"],
        ["books which give you definite facts and information which can easily be learned.", "P", "T"]
        ]
        assess = [
        ["How well do you think you have been doing in your assessed work overall, so far?"]
        ]
        i = 1
        for question in questions:
            label = question[0]
            choices = [(1, 'Strongly Disagree'),(2,'Disagree'),(3,'Neither Agree Nor Disagree'),(4,'Agree'),(5,'Strongly Agree')]
            field = forms.ChoiceField(label=label, choices=choices,
                    widget=forms.RadioSelect(attrs={'score_category':question[1],'score_subcategory':question[2]}), required=True)
            self.fields['%d' % i] = field
            i += 1
        for question in preferences:
            label = question[0]
            choices = [(1, 'Hate'),(2,'Dislike'),(3,'No Preference'),(4,'Like'),(5,'Love')]
            field = forms.ChoiceField(label=label, choices=choices,
                    widget=forms.RadioSelect(attrs={'score_category':question[1],'score_subcategory':question[2]}), required=True)
            self.fields['%d' % i] = field
            i += 1
        for question in assess:
            label = question[0]
            choices = [(1, 'Badly'),(2,'Not So Well'),(3,'Average'),(4,'Well'),(5,'Excellent')]
            field = forms.ChoiceField(label=label, choices=choices,
                    widget=forms.RadioSelect, required=True)
            self.fields['%d' % i] = field
            i += 1
