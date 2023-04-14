from .models import Action, Topic


def topic_list(request):
    topics = [i[0] for i in Topic.objects.values_list()]
    topic_dict = {}
    actions = list(Action.objects.select_related('topic')
                    .filter(person=request.user.id).order_by('-date')
                    .order_by('-time').order_by('-important').values())
    for topic in topics:
        topic_dict[f'{topic}'] = list(filter(lambda x: x['topic_id'] == f'{topic}', actions))
    data = {'topics': topics, 'topicDict' : topic_dict}
    return data