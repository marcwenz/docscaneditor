class DocumentManager:
    def __init__(self):
        self.images = []

    def get_document(self, ix):
        # returns document at ix
        raise NotImplementedError

    def new_document(self, ims=[]):
        # adds empty document to stack, optionally doc content
        raise NotImplementedError

    def append_to_last(self, im):
        # adds image to last document in stack
        raise NotImplementedError

    def split_document(self, doc_ix, im_ix):
        # splits document of index doc_ix at index im_ix
        raise NotImplementedError

    def merge_documents(self, docs):
        # merges list of documents, docs is list of indexes
        raise NotImplementedError

    def merge_to_prev(self, ix):
        # merges document ix to previous index
        raise NotImplementedError
        # beware check for out of range
        self.merge_documents(self, [ix, ix - 1])

    def merge_to_next(self, ix):
        # merges document ix to next index
        raise NotImplementedError
        # beware check for out of range
        self.merge_documents(self, [ix, ix + 1])


class Document:
    def __init__(self, ims=[]):
        self.images = ims

    def append(self, im):
        self.images.append(im)

    def extend(self, ims):
        self.images.extend(ims)

    def insert(self, ix, im):
        self.images.insert(ix, im)

    def remove(self, ix):
        self.images.remove(ix)

    def pop(self):
        self.images.pop()

    def __getitem__(self, i):
        if isinstance(i, int):
            return self.images[i]
        elif isinstance(i, list) or isinstance(i, tuple):
            return [self.images[x] for x in i]


class ScannedImage:
    def __init__(self, path, qr=None):
        self.path = path
        self.qrcode = qr

    def get_full_image(self):
        # returns PIL Image object of image
        raise NotImplementedError

    def get_thumbnail(self, size):
        # generates thumbnail of size (w, h)
        raise NotImplementedError

    def qr(self):
        return self.qrcode
