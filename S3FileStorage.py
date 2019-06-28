import boto3


class S3FileStorage:
    def __init__(self, bucket_name: str, aws_access_key_id: str, aws_secret_access_key: str):
        self.bucket_name = bucket_name
        self.storage_client = boto3.client('s3',
                                           aws_access_key_id=aws_access_key_id,
                                           aws_secret_access_key=aws_secret_access_key)
        """ :type : pyboto3.s3 """

    def upload_file(self, local_file_path: str, file_name: str):
        """
        Uploads an local file to the S3 storage.
        :param local_file_path: The path of the local file.
        :param file_name: The name of the file on the S3 storage
        :return: None
        """
        self.storage_client.upload_file(local_file_path, self.bucket_name, file_name)

    def upload_file_obj(self, file_object, file_name):
        """
        Upload a file-like object to S3.
        The file-like object must be in binary mode.
        This is a managed transfer which will perform a multipart upload in
        multiple threads if necessary.
        :

        :example: from S3FileStorage import S3FileStorage
        fs = S3FileStorage()

        with open('filename', 'rb') as file_object:
            fs.upload_file_obj(file_object, file_name)


        :param file_object: An file-like object.
        :param file_name: The file name on the S3 storage.
        :return:
        """
        self.storage_client.upload_fileobj(Fileobj=file_object, Bucket=self.bucket_name, Key=file_name)

    def download_file(self, storage_file_name: str, local_path: str):
        """
        Downloads a file from S3 to the local storage.
        :param storage_file_name: The filename on S3.
        :param local_path: The local storage path.
        :return: None
        """
        self.storage_client.download_file(self.bucket_name, storage_file_name, local_path)

    def download_file_obj(self, storage_file_name:str, file_object):
        """
        Download an object from S3 to a file-like object.
        The file-like object must be in binary mode.
        This is a managed transfer which will perform a multipart download in
        multiple threads if necessary.
        :


        :example: from S3FileStorage import S3FileStorage
        fs = S3FileStorage()

        with open('filename', 'wb') as file_object:
            fs.download_file_obj(storage_file_name, file_object)


        :param storage_file_name: The filename on S3.
        :param file_object: An file-like object
        :return: None
        """
        self.storage_client.download_fileobj(Bucket=self.bucket_name, Key=storage_file_name, Fileobj=file_object)

    def delete_file(self, storage_file_name:str):
        """
        Deletes a file on S3.
        :param storage_file_name: The filename on the S3 storage.
        :return: None
        """
        self.storage_client.delete_object(Bucket=self.bucket_name, Key=storage_file_name)


if __name__ == "__main__":
    pass
