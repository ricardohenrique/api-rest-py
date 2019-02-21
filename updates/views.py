import json

from django.core.serializers import serialize
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View

from pure_api_django.mixins import JsonResponseMixin
from .models import Update

# def detial_view(request):
# 	return render(request, templete, {}) #return JSON data -> JS Object Notion
# 	return HttpResponse(get_templete().render({}))


def json_http_example_view(request):
	data = {
		"count": 1000,
		"content": "Use HttpResponse"
	}
	json_data = json.dumps(data)
	return HttpResponse(json_data, content_type='application/json')

def json_response_example_view(request):
	data = {
		"count": 2000,
		"content": "Use JsonResponse"
	}
	return JsonResponse(data)


class JsonCBV(View):
	def get(self, request, *args, **kwargs):
		data = {
			"count": 2000,
			"content": "Use JsonResponse"
		}
		return JsonResponse(data)

class JsonCBV2(JsonResponseMixin, View):
	def get(self, request, *args, **kwargs):
		data = {
			"count": 2000,
			"content": "Use JsonResponse"
		}
		return self.render_to_json_response(data)

class SerializedDetialView(View):
	def get(self, request, *args, **kwargs):
		obj = Update.objects.get(id=1)
		data = serialize('json', [obj], fields=('user', 'content'))
		return HttpResponse(data, content_type='application/json')

class SerializedListView(View):
	def get(self, request, *args, **kwargs):
		obj = Update.objects.all()
		# data = serialize('json', obj, fields=('user', 'content'))
		data = serialize('json', obj)

		json_data = data
		return HttpResponse(json_data, content_type='application/json')