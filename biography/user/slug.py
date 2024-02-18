
import uuid
import base64

# def slug(length=8):
#
#     # generate base64 uniqe slug
#     return base64.b64encode(bytes.fromhex(uuid.uuid4().hex)).decode().replace('/', '_')[:length]

def slug(email):

    # generate base64 uniqe slug
    return email.split('@')[0]

