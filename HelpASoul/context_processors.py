from blog.models import Blog
from social_cases.models import SocialCase


def get_all_social_cases(request):
    social_cases = SocialCase.objects.all()
    social_cases_with_percentages = []
    for social_case in social_cases:
        percent = social_case.percent_raised()
        amount_raised = social_case.total_donations()
        social_cases_with_percentages.append({'social_case': social_case, 'percent': percent,
                                              'amount_raised': amount_raised})

    return {'social_cases': social_cases, 'social_cases_with_percentages': social_cases_with_percentages}


def get_all_blog_posts(request):
    blogs = Blog.objects.all()
    return {'blogs': blogs}



