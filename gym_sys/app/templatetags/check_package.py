from django import template
from app.models import Subscription,SubcripPlan  
from django.contrib.auth.models import User

register=template.Library()

@register.simple_tag
def check_user_package(user_id,plan_id):
	user=User.objects.get(id=user_id)
	plan=SubcripPlan.objects.get(id=plan_id)
	check_package=Subscription.objects.filter(user=user,plan=plan).count()
	if check_package > 0:
		return True
	else:
		return False