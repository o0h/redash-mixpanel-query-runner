import json
from redash.query_runner import *
from collections import Iterable


try:
    import mixpanel
    enabled = True

except ImportError:
    enabled = False

class MixpanelJql(BaseQueryRunner):
    @classmethod
    def annotate_query(cls):
        return False

    @classmethod
    def type(cls):
        return "mixpanel_jql"

    @classmethod
    def name(cls):
        return "Mixpanel JQL"

    def __init__(self, configuration):
        super(MixpanelJql, self).__init__(configuration)


    @classmethod
    def configuration_schema(cls):
        return {
            'type': 'object',
            'properties': {
                'api_secret': {
                    'type': 'string',
                    'title': 'Api Secret'
                }
            },
            "required": ["api_secret"],
            "secret": ["api_secret"]
        }

    @classmethod
    def enabled(cls):
        return enabled

    def test_connection(self):
        import mixpanel

        sample_query = "main = () => People().reduce(mixpanel.reducer.null())"
        api_secret = self.configuration.get('api_secret')
        api = mixpanel.Mixpanel(api_secret)
        data = api.request(["jql"], {"script": sample_query}, "POST")
        if data != [None]:
            raise Exception("Can't fetch from JQL")

    def run_query(self, query, user):
        import mixpanel

        api_secret = self.configuration.get('api_secret')
        api = mixpanel.Mixpanel(api_secret)
        data = api.request(["jql"], {"script": query}, "POST")

        result = {}
        if (not isinstance(data[0], Iterable)) or type(data[0]) in [str, unicode]:
            result["columns"] = [{"name": "value", "friendly_name": "value"}]
            result["rows"] = [{"value": v} for v in data]
        elif isinstance(data[0], dict):
            result["columns"] = [{"name": k, "friendly_name": k} for k in data[0]]
            result["rows"] = data
        else:
            result["columns"] = [{"name": k, "friendly_name": k} for k in range(len(data[0]))]
            result["rows"] = data

        print result["columns"]

        return json.dumps(result), None

register(MixpanelJql)
