
from google.cloud import storage
from datetime import datetime

class c_data_gbucket:

    def __init__(self):
        self.folder_name='/home/dfbrownnz/example-youtube/'
        self.file_name='employee_records.json'

    def test(self  ):
        print(f" this is c_data_json {self.folder_name}{self.file_name}" )
        self.write_read_my()

    def write_read_my(self):
        bucket_name='example-bucket-1-dfb'
        dtnow = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        blob_name='somefile_dtnow_.txt'
        self.write_read(bucket_name , blob_name)

    def write_read(self, bucket_name, blob_name):
        """Write and read a blob from GCS using file-like IO"""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"

        # The ID of your new GCS object
        # blob_name = "storage-object-name"

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        # Mode can be specified as wb/rb for bytes mode.
        # See: https://docs.python.org/3/library/io.html
        with blob.open("w") as f:
            f.write("Hello world")

        with blob.open("r") as f:
            print(f.read())


if __name__ == '__main__':
    file_name='employee_records.json'
    ma = c_data_gbucket()
    ma.test()
    # ma.gstoreage()
