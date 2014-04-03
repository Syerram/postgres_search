'''
Created on Apr 3, 2014

@author: syerram
'''
def get_object_or_None(modal, **kwargs):
    try:
        return modal.objects.get(**kwargs)
    except Exception as ex:
        return None


class JSONEnabledMixin(object):

    def render_to_response(self, context, **response_kwargs):
        response = super(JSONEnabledMixin, self).render_to_response(context, **response_kwargs)
        response.content_type = 'applicaiton/json'
        return response
