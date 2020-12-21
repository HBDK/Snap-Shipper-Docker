import boto3
import logging
from botocore.exceptions import ClientError


class S3Client:
    def __init__(self, settings):
        self._settings = settings["S3Client"]
        self.Name = settings["Name"]
        self.client = self._init_client()
        self.UpRemotes()

    def UpRemotes(self):
        self.Remotes = self._list_bucket_files()

    def Upload(self, remote_path="", local_path=""):
        try:
            self.client.meta.client.upload_file(
                local_path, self._settings["bucket"], remote_path)
        except ClientError as err:
            logging.error(
                "Error while uploading file to {}: {}".format(self.Name, err))

    def _init_client(self):
        return boto3.resource("s3",
                              endpoint_url=self._settings["endpoint_url"],
                              aws_access_key_id=self._settings["aws_access_key"],
                              aws_secret_access_key=self._settings["aws_secret_access_key"])

    def _list_bucket_files(self):
        bucket = self.client.Bucket(self._settings["bucket"])
        return [x.key for x in bucket.objects.all()]
