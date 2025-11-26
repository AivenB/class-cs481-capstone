from django.contrib import admin

# Register your models here.
from .models import Testing, Topic, Characteristic, Question, Survey, Community, Response, Assessment

# admin.site.register(Testing)

# admin.site.register(Question)
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'text', 'topic', 'characteristic', 'created_at', 'updated_at')
#     list_filter = ('topic', 'characteristic')
#     search_fields = ('text',)
#     autocomplete_fields = ('topic', 'characteristic')
#     readonly_fields = ('created_at', 'updated_at')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'topic', 'created_at', 'updated_at')
    list_filter = ('topic', 'characteristics')
    search_fields = ('text',)
    autocomplete_fields = ('topic',)
    filter_horizontal = ('characteristics',)  # For easy selection of multiple tags
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    filter_horizontal = ('questions',)  # Use dual-pane widget to select questions


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'community', 'survey', 'started_at')
    search_fields = ('community__name', 'survey__name')
    autocomplete_fields = ('community', 'survey')
    readonly_fields = ('started_at',)



@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'assessment_community', 'assessment_survey', 'question', 'rating', 'submitted_at')
    list_filter = ('assessment__survey', 'assessment__community', 'question__topic')
    search_fields = ('feedback',)
    autocomplete_fields = ('assessment', 'question')
    readonly_fields = ('submitted_at',)

    def assessment_community(self, obj):
        return obj.assessment.community
    assessment_community.short_description = 'Community'

    def assessment_survey(self, obj):
        return obj.assessment.survey
    assessment_survey.short_description = 'Survey'
