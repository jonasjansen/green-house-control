import json
from logger import logger

import firebase_admin
from firebase_admin import credentials, initialize_app, storage
from firebase_admin import firestore
from config_provider import config


class Firebase:

    def __init__(self):
        # Init firebase connection.
        cred = credentials.Certificate(config.get_firebase_credentials_file())
        initialize_app(cred, {'storageBucket': config.get_config('FIREBASE/STORAGE_BUCKET')})
        self.db = firestore.client()

    def add_document(self, collection, data):
        self.db.collection(collection).add(data)

    def update_document(self, collection, document, data):
        doc_ref = self.db.collection(collection).document(document)
        doc_ref.update(data)

    def get_document(self, collection, document):
        result = {}
        doc_ref = self.db.collection(collection).document(document)

        try:
            doc = doc_ref.get()
            if doc.exists:
                result = doc.to_dict()
            else:
                print('Document', document, "in collection", collection, "does not exist.")
        except Exception as e:
            print("Error getting document:", e)
        return result

    def upload_file(self, blob_name, file_name):
        try:
            logger.info("Upload:" + file_name)
            bucket = storage.bucket()
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(file_name)
            #blob.make_public()

        except Exception as e:
            logger.error("Error uploading " + file_name + "to storage:" + str(e))


firebase = Firebase()
