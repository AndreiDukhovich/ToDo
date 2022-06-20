from .models import Action, Topic


def topic_list(request):
    topics = [i[0] for i in Topic.objects.values_list()]
    topic_dict = {}
    for topic in topics:
        topic_dict[f'{topic}'] = Action.objects.filter(person=request.user.username).filter(topic=f'{topic}').order_by('-date').order_by('-time').order_by('-important').order_by('complete')          
    data = {'topics': topics, 'topicDict' : topic_dict}
    return data