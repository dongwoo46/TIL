from django import template

register = template.Library()

@register.filter
def hashtag_link(word): # 해쉬태그를 받음
    content = word.content + ' '
    hashtags = word.hashtags.all()
    for hashtag in hashtags:
      content = content.replace(hashtag.content + ' ', f'<a href ="/movies/{hashtag.pk}/hashtag/">{hashtag.content}</a> ')
			# <a href ="/movies/{hashtag.pk}/hashtag/">{hashtag.content}</a>
    return content