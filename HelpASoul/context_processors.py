from social_cases.models import SocialCase


def get_all_social_cases(request):
    social_cases = SocialCase.objects.all()
    return {'social_cases': social_cases}

