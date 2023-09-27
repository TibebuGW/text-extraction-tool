import json

from google.cloud import secretmanager


def get_secret_value_dict(
    project_id="452718658108", secret_id="rate-eat", version_id="latest"
):
    client = secretmanager.SecretManagerServiceClient()

    secret_name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    response = client.access_secret_version(request={"name": secret_name})
    secret_value = json.loads(response.payload.data.decode("UTF-8"))

    return secret_value
