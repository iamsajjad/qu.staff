
import uuid
import pathlib

def path(instance, filename):

    # `uniqe file name` `extract uploaded file extension`
    filename = f'{uuid.uuid4().hex}{pathlib.Path(filename).suffix.lower()}'

    return f'user/images/{filename}'

