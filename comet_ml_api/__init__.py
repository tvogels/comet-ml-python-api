from comet_ml_api import helpers
import pandas as pd

class CometMlApi:
    def __init__(self, api_key, version = helpers.DEFAULT_VERSION):
        self.version = version
        self.api_key = api_key

    def get_version(self):
        return self.version

    def get_url(self):
        return helpers.URLS[self.version]

    def projects(self, workspace_id):
        params = {'workspace': workspace_id}
        return pd.DataFrame(helpers.get_request("projects", params, self.version, self.api_key)['projects'])

    def experiments(self, project_id):
        params = {'projectId': project_id}
        return pd.DataFrame(helpers.get_request("experiments", params, self.version, self.api_key)['experiments'])

    def experiment_html(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/html", params, self.version, self.api_key)['html']

    def experiment_code(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/code", params, self.version, self.api_key)['code']

    def experiment_stdout(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/stdout", params, self.version, self.api_key)['output']

    def experiment_installed_packages(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/installed-packages", params, self.version, self.api_key)['packages']

    def experiment_graph(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/graph", params, self.version, self.api_key)['graph']

    def experiment_images(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return pd.DataFrame(helpers.get_request("experiment/images", params, self.version, self.api_key)['images'])

    def experiment_params(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return pd.DataFrame(helpers.get_request("experiment/params", params, self.version, self.api_key)['results'])

    def experiment_metrics(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return pd.DataFrame(helpers.get_request("experiment/metrics", params, self.version, self.api_key)['results'])

    def experiment_log_other(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return helpers.get_request("experiment/log-other", params, self.version, self.api_key)['logOtherList']

    def experiment_metrics_raw(self, experiment_key):
        params = {'experimentKey': experiment_key}
        return pd.DataFrame(helpers.get_request("experiment/metrics-raw", params, self.version, self.api_key)['metrics'])
