import django_filters
from django_filters import DateFilter, CharFilter, ModelChoiceFilter, ChoiceFilter

from .models import *

class CommentFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Comment
		fields = '__all__'
		exclude = ['guest', 'date_created']

class PostFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    title = CharFilter(field_name='title', lookup_expr='icontains')
    content = CharFilter(field_name='content', lookup_expr='icontains')
    category = ChoiceFilter(field_name='category', choices=Post.CATEGORY)
    tag = ModelChoiceFilter(queryset=Tag.objects.all(), field_name='tags')
    # tags = ModelMultipleChoiceFilter(queryset=Tag.objects.all(), field_name='tags', to_field_name='id', conjoined=False)  # Use 'tags' and allow multiple selections

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['account', 'date_created', 'image']