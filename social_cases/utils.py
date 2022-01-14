from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_social_cases(request, social_cases_with_percentages, results):

    page = request.GET.get('page')
    paginator = Paginator(social_cases_with_percentages, results)

    try:
        social_cases_with_percentages = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        social_cases_with_percentages = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        social_cases_with_percentages = paginator.page(page)

    left_index = (int(page) - 4)
    if left_index < 1:
        left_index = 1
    right_index = (int(page) + 5)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return custom_range, social_cases_with_percentages
