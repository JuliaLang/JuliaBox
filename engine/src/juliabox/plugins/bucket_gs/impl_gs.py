__author__ = 'Nishanth'

import os
import urllib
import io
from juliabox.cloud import JBPluginCloud
from juliabox.jbox_util import JBoxCfg
from oauth2client.service_account import _ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseUpload
from mimetypes import MimeTypes

class JBoxGS(JBPluginCloud):
    provides = [JBPluginCloud.JBP_BUCKETSTORE, JBPluginCloud.JBP_BUCKETSTORE_GS]
    CONN = None
    BUCKETS = dict()

    @staticmethod
    def connect():
        if JBoxGS.CONN is None:
            google_oauth = JBoxCfg.get("google_oauth")
            creds = _ServiceAccountCredentials(
                service_account_id=google_oauth["client_id"],
                service_account_email=google_oauth["client_email"],
                private_key_id=google_oauth["key"],
                private_key_pkcs8_text=google_oauth["secret"],
                scopes=[])
            JBoxGS.CONN = build("storage", "v1", credentials=creds)
        return JBoxGS.CONN

    @staticmethod
    def connect_bucket(bucket):
        if bucket not in JBoxGS.BUCKETS:
            JBoxGS.BUCKETS[bucket] = JBoxGS.connect().buckets().get(bucket=bucket).execute()
        return JBoxGS.BUCKETS[bucket]

    @staticmethod
    def _get_mime_type(local_file):
        mime = MimeTypes()
        url = urllib.pathname2url(local_file)
        mime_type = mime.guess_type(url)
        return mime_type[0]

    @staticmethod
    def push(bucket, local_file, metadata=None):
        objconn = JBoxGS.connect().objects()
        fh = open(local_file, "rb")
        media = MediaIoBaseUpload(fh, JBoxGS._get_mime_type(local_file))
        if metadata:
            retval = objconn.insert(bucket=bucket, media_body=media,
                                    name=os.path.basename(local_file),
                                    body={"metadata": metadata}).execute()
        else:
            retval = objconn.insert(bucket=bucket, media_body=media,
                                    name=os.path.basename(local_file)).execute()
        fh.close()
        return retval

    @staticmethod
    def pull(bucket, local_file, metadata_only=False):
        objname = os.path.basename(local_file)
        if metadata_only:
            k = None
            try:
                k = JBoxGS.connect().objects().get(bucket=bucket,
                                                   object=objname).execute()
            except:
                pass
            return k
        else:
            req = JBoxGS.connect().objects().get_media(bucket=bucket,
                                                       object=objname)

            fh = open(local_file, "wb")
            downloader = MediaIoBaseDownload(fh, req, chunksize=1024*1024)
            done = False
            while not done:
                try:
                    _, done = downloader.next_chunk()
                except:
                    break
            fh.close()
            if not done:
                os.remove(local_file)

    @staticmethod
    def delete(bucket, local_file):
        key_name = os.path.basename(local_file)
        k = JBoxGS.connect().objects().delete(bucket=bucket, object=key_name).execute()
        return k

    @staticmethod
    def copy(from_file, to_file, from_bucket, to_bucket=None):
        if to_bucket is None:
            to_bucket = from_bucket

        from_key_name = os.path.basename(from_file)
        to_key_name = os.path.basename(to_file)

        k = JBoxGS.connect().objects().copy(sourceBucket=from_bucket,
                                            sourceObject=from_key_name,
                                            destinationBucket=to_bucket,
                                            destinationObject=to_key_name,
                                            body={}).execute()
        return k

    @staticmethod
    def move(from_file, to_file, from_bucket, to_bucket=None):
        k_new = JBoxGS.copy(from_file, to_file, from_bucket, to_bucket)
        if k_new is None:
            return None
        JBoxGS.delete(from_bucket, from_file)
        return k_new
