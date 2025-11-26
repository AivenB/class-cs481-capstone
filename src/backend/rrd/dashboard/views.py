from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse
from django.template import loader
from django.template.loader import render_to_string
from .models import Community, Assessment, Question, Topic, Characteristic, Survey, Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponseServerError, HttpResponseNotFound

# Create your views here.

# default view
# updated to landing page
def default_view(request):
    # return HttpResponse("Welcome to the Rural Resilience Dashboard!")
    return render(request, 'start.html')

# hello view
# def say_hello(request):
    # return HttpResponse("Hello, World!")
    # return render(request, 'hello.html')
    # template = loader.get_template('hello.html')
    # return HttpResponse(template.render({'name': 'World'}, request))

# index/home view
# def index(request):
    # return render(request, 'index.html')

# about view
def about(request):
    return render(request, 'about.html', {'active_page': 'about'})

# community profiles view
# def community_profiles(request):
    # return render(request, 'community_profiles.html')

# data input view
# def data_input(request):
#     return render(request, 'data_input.html')

# data visualization view
# def data_visualizations(request):
#     return render(request, 'data_visualizations.html')


# dashboard view
def dashboard(request):
    return render(request, 'dashboard.html', {'active_page': 'dashboard'})

# community dashboard view
def community(request):
    return render(request, 'community.html', {'active_page': 'community'})

# assessment dashboard view
def assessment(request):
    return render(request, 'assessment.html', {'active_page': 'assessment'})


def dashboard_stats(request):
    # Add logic to fetch updated stats
    context = {
        'total_communities': 12,
        'completed_assessments': 8,
        'score_range': '1 - 5'
    }
    return render(request, 'partials/dashboard_stats.html', context)

def dashboard_activity(request):
    # Add logic to fetch recent activity
    activities = [
        {'text': 'Boise County Assessment Updated', 'time': '2 hours ago'},
        {'text': 'New Community Added: Valley County', 'time': 'Yesterday'},
        {'text': 'Resilience Report Generated for Elmore County', 'time': '3 days ago'}
    ]
    return render(request, 'partials/activity_list.html', {'activities': activities})

def community_search(request):
    query = request.GET.get('q', '')
    # Add logic to filter communities based on search query
    return render(request, 'partials/community_cards.html', {'communities': filtered_communities})

def community_filter(request, filter_type):
    # Add logic to filter communities based on filter_type
    return render(request, 'partials/community_cards.html', {'communities': filtered_communities})

# Add this new view function
def start_view(request):
    return render(request, 'start.html')

# Update the default view to redirect to start
def default_view(request):
    return render(request, 'start.html')

# Add this new view function
def analytics(request):
    return render(request, 'analytics.html', {'active_page': 'analytics', 'active_tab': 'characteristics'})

def analytics_filter(request, filter_type):
    template = f'partials/analytics_{filter_type}.html'
    context = {'active_tab': filter_type}
    return render(request, template, context)

def profiles(request):
    return render(request, 'community.html', {'active_tab': 'all'})

def profiles_filter(request, filter_type):
    context = {'active_tab': filter_type}
    
    if filter_type == 'all':
        return render(request, 'partials/profiles_all.html', context)
    elif filter_type == 'assessed':
        return render(request, 'partials/profiles_assessed.html', context)
    elif filter_type == 'in_progress':
        return render(request, 'partials/profiles_in_progress.html', context)
    
# Handle assessment view
# def assessment_view(request):
#     # Get all communities from database
#     communities = Community.objects.all().order_by('name')
    
#     return render(request, 'assessment.html', {
#         'communities': communities,
#     })

# # This handles the HTMX request when a community is selected
# def load_assessment_form(request):
#     community_id = request.GET.get('community')
#     if community_id:
#         community = Community.objects.get(pk=community_id)
#         surveys = Survey.objects.all().order_by('name')
        
#         return render(request, 'partials/assessment_form.html', {
#             'community_id': community_id,
#             'community': community,
#             'surveys': surveys,
#         })
#     return render(request, 'partials/assessment_form.html', {})

# # Add this function to handle form submission
# def create_assessment(request):
#     if request.method == 'POST':
#         community_id = request.POST.get('community_id')
#         survey_id = request.POST.get('survey_id')
        
#         # Create new assessment
#         assessment = Assessment.objects.create(
#             community_id=community_id,
#             survey_id=survey_id
#         )
        
#         # Redirect to a page where the user can fill out the assessment
#         return redirect(reverse('fill_assessment', kwargs={'assessment_id': assessment.id}))
    
#     # Handle GET requests or form errors
#     return redirect('assessment_view')

# # Add stub for fill_assessment (to be implemented later)
# def fill_assessment(request, assessment_id):
#     assessment = Assessment.objects.get(pk=assessment_id)
#     return render(request, 'fill_assessment.html', {
#         'assessment': assessment
#     })


# def assessment_view(request):
#     """View for the assessment page"""
#     communities = Community.objects.all().order_by('name')
#     return render(request, 'assessment.html', {'communities': communities})

# def load_assessment_form(request):
#     """Load the assessment form for a selected community"""
#     community_id = request.GET.get('community')
#     if community_id:
#         community = Community.objects.get(pk=community_id)
#         surveys = Survey.objects.all().order_by('name')
#         return render(request, 'partials/assessment_form.html', {
#             'community': community,
#             'surveys': surveys
#         })
#     return render(request, 'partials/assessment_form.html', {})

# def load_survey_questions(request):
#     """Load questions for a selected survey"""
#     community_id = request.GET.get('community_id')
#     survey_id = request.GET.get('survey_id')
    
#     # Check if navigating between questions
#     direction = request.GET.get('direction')
#     current_index = int(request.GET.get('current_index', 0))
    
#     if direction == 'prev' and current_index > 0:
#         current_index -= 1
    
#     if community_id and survey_id:
#         community = Community.objects.get(pk=community_id)
#         survey = Survey.objects.get(pk=survey_id)
#         questions = list(survey.questions.all().order_by('id'))
        
#         if not questions:
#             return render(request, 'partials/survey_questions.html', {'survey': survey})
        
#         current_question = questions[current_index]
        
#         # Check if there's already a saved response for this question
#         assessment = None
#         saved_rating = None
#         saved_feedback = None
        
#         try:
#             assessment = Assessment.objects.get(community=community, survey=survey)
#             try:
#                 response = Response.objects.get(assessment=assessment, question=current_question)
#                 saved_rating = str(response.rating)
#                 saved_feedback = response.feedback
#             except Response.DoesNotExist:
#                 pass
#         except Assessment.DoesNotExist:
#             # Create a new assessment
#             assessment = Assessment.objects.create(community=community, survey=survey)
        
#         # Calculate progress percentage
#         progress_percent = (current_index + 1) / len(questions) * 100
        
#         return render(request, 'partials/survey_questions.html', {
#             'community_id': community_id,
#             'survey': survey,
#             'questions': questions,
#             'current_question': current_question,
#             'current_index': current_index,
#             'progress_percent': progress_percent,
#             'saved_rating': saved_rating,
#             'saved_feedback': saved_feedback
#         })
    
#     return render(request, 'partials/survey_questions.html', {})

# def submit_question_response(request):
#     """Handle submission of a question response"""
#     if request.method == 'POST':
#         community_id = request.POST.get('community_id')
#         survey_id = request.POST.get('survey_id')
#         question_index = int(request.POST.get('question_index', 0))
#         total_questions = int(request.POST.get('total_questions', 0))
#         rating = request.POST.get('rating')
#         feedback = request.POST.get('feedback')
        
#         if community_id and survey_id:
#             community = Community.objects.get(pk=community_id)
#             survey = Survey.objects.get(pk=survey_id)
#             questions = list(survey.questions.all().order_by('id'))
#             current_question = questions[question_index]
            
#             # Get or create assessment
#             assessment, created = Assessment.objects.get_or_create(
#                 community=community,
#                 survey=survey
#             )
            
#             # Save response
#             response, created = Response.objects.update_or_create(
#                 assessment=assessment,
#                 question=current_question,
#                 defaults={
#                     'rating': rating,
#                     'feedback': feedback
#                 }
#             )
            
#             # Check if this was the last question
#             if question_index >= total_questions - 1:
#                 # Calculate average rating
#                 responses = Response.objects.filter(assessment=assessment)
#                 total_responses = responses.count()
#                 avg_rating = responses.aggregate(models.Avg('rating'))['rating__avg']
                
#                 return render(request, 'partials/assessment_complete.html', {
#                     'community': community,
#                     'survey': survey,
#                     'total_responses': total_responses,
#                     'avg_rating': avg_rating
#                 })
            
#             # Move to the next question
#             next_index = question_index + 1
#             next_question = questions[next_index]
            
#             # Check if there's already a saved response for the next question
#             saved_rating = None
#             saved_feedback = None
#             try:
#                 next_response = Response.objects.get(assessment=assessment, question=next_question)
#                 saved_rating = str(next_response.rating)
#                 saved_feedback = next_response.feedback
#             except Response.DoesNotExist:
#                 pass
            
#             # Calculate new progress percentage
#             progress_percent = (next_index + 1) / len(questions) * 100
            
#             return render(request, 'partials/survey_questions.html', {
#                 'community_id': community_id,
#                 'survey': survey,
#                 'questions': questions,
#                 'current_question': next_question,
#                 'current_index': next_index,
#                 'progress_percent': progress_percent,
#                 'saved_rating': saved_rating,
#                 'saved_feedback': saved_feedback
#             })
    
#     # Fallback to assessment view
#     return redirect('assessment_view')

# def assessment_start(request):
    # communities = Community.objects.all()
    # return render(request, "assessment.html", {"communities": communities})
    # return render(request, "assessment.html")

# def load_assessment_form(request):
#     try:
#         community_id = request.GET.get("community")
#         if not community_id:
#             return HttpResponse("No community selected", status=400)

#         community = get_object_or_404(Community, pk=community_id)
        
#         survey = Survey.objects.first()
#         if not survey:
#             return HttpResponse("No surveys found. Please add one.", status=500)

#         assessment, created = Assessment.objects.get_or_create(
#             community=community, survey=survey
#         )
#         questions = survey.questions.all().order_by("id")

#         return render(request, "partials/assessment_form.html", {
#             "assessment": assessment,
#             "questions": questions,
#             "current_index": 0
#         })
#     except Exception as e:
#         import traceback
#         return HttpResponseServerError(f"<pre>{traceback.format_exc()}</pre>")


# @csrf_exempt  # Required for HTMX POSTs unless you use {% csrf_token %}
# def submit_response(request):
#     assessment_id = request.POST["assessment_id"]
#     question_id = request.POST["question_id"]
#     rating = request.POST.get("rating")
#     feedback = request.POST.get("feedback", "")
#     nav = request.POST.get("nav", "next")
#     current_index = int(request.POST.get("current_index", 0))

#     assessment = get_object_or_404(Assessment, pk=assessment_id)
#     question = get_object_or_404(Question, pk=question_id)

#     Response.objects.update_or_create(
#         assessment=assessment,
#         question=question,
#         defaults={"rating": rating, "feedback": feedback},
#     )

#     questions = list(assessment.survey.questions.all().order_by("id"))

#     if nav == "next" and current_index < len(questions) - 1:
#         current_index += 1
#     elif nav == "prev" and current_index > 0:
#         current_index -= 1

#     return render(request, "partials/assessment_form.html", {
#         "assessment": assessment,
#         "questions": questions,
#         "current_index": current_index
#     })


def assessment(request):
    # Only include communities with assessments
    communities = Community.objects.filter(assessment__isnull=False).distinct()
    
    return render(request, 'assessment.html', {
        'communities': communities,
    })

# show start assessment button when community is selected
def show_start_assessment_button(request):
    community_id = request.GET.get("community")
    if not community_id:
        return HttpResponse("")  # No community selected, don't show anything

    community = Community.objects.filter(id=community_id).first()
    if not community:
        return HttpResponse("")

    return render(request, "partials/start_assessment_button.html", {"community": community})

from django.shortcuts import render, get_object_or_404
from .models import Community, Survey, Assessment, Question


def start_assessment(request):
    community_id = request.GET.get("community")
    community = get_object_or_404(Community, id=community_id)

    # Get the assessment that ties this community to a survey
    assessment = Assessment.objects.filter(community=community).first()
    if not assessment:
        return HttpResponseNotFound("No assessment assigned to this community.")

    survey = assessment.survey
    questions = list(survey.questions.all().order_by("id"))
    question = questions[0] if questions else None

    # rating labels
    RATING_LABELS = [
        (1, "Very Low"),
        (2, "Low"),
        (3, "Moderate"),
        (4, "High"),
        (5, "Very High"),
    ]

    return render(request, "survey/take_assessment.html", {
        "community": community,
        "assessment": assessment,
        "questions": questions,
        "question": question,
        "current_index": 0,
        "responses": {},
        "rating_labels": RATING_LABELS,
    })


@csrf_exempt
def next_question(request):
    community_id = request.POST.get("community_id")
    community = get_object_or_404(Community, id=community_id)

    survey = Survey.objects.filter(assessment__community=community).first()
    questions = list(survey.questions.all().order_by("id"))

    current_index = int(request.POST.get("current_index", 0))
    question_id = request.POST.get("question_id")
    rating = request.POST.get("rating")

    responses = {}
    for key in request.POST:
        if key.startswith("q_"):
            responses[key[2:]] = request.POST[key]

    # Add current answer
    if question_id and rating:
        responses[question_id] = rating

    
    # Debug print 
    print("Current Index:", current_index)
    print("Next Index:", current_index + 1)
    print("Responses:", responses)
    print("Total Questions:", len(questions))

    # proceed to the next question
    next_index = current_index + 1

    if next_index >= len(questions):
        return render(request, "assessment/review.html", {
            "community": community,
            "responses": responses,
            "questions": questions,
        })

    next_question = questions[next_index]

    # rating labels
    RATING_LABELS = [
        (1, "Very Low"),
        (2, "Low"),
        (3, "Moderate"),
        (4, "High"),
        (5, "Very High"),
    ]

    return render(request, "survey/question_form.html", {
        "question": next_question,
        "current_index": next_index,
        "questions": questions,
        "responses": responses,
        "community": community,
        "rating_labels": RATING_LABELS,
    })



# This function handles the HTMX request to submit the assessment
def submit_assessment(request):
    community_id = request.POST.get("community_id")
    community = get_object_or_404(Community, id=community_id)
    survey = Survey.objects.first()

    assessment = Assessment.objects.create(community=community, survey=survey)

    for key, value in request.POST.items():
        if key.startswith("q_"):
            qid = key[2:]
            question = get_object_or_404(Question, id=qid)
            Response.objects.create(
                assessment=assessment,
                question=question,
                rating=int(value)
            )

    return render(request, "survey/thank_you.html")

# partial views test
def test_partial(request):
    return render(request, "partials/assessment_form.html", {
        "assessment": None,
        "questions": [],
        "current_index": 0
    })
