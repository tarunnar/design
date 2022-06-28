import abc


class IDownloader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def download(self, filename):
        pass


class Downloader(object):
    def download(self, filename):
        return str(filename)


class GoogleDrive(object):
    def auth(self):
        authToken = "auth"  # logic to authenticate
        return authToken

    def download(self, authToken, filename):
        return filename


class GoogleAdapter(IDownloader):
    def download(self, filename):
        googleDrive = GoogleDrive()
        authToken = googleDrive.auth()
        return googleDrive.download(authToken, filename)


### resource: https://www.youtube.com/watch?v=VNL1NsS5Prs&list=PLJN9ydlFnJsi6-lev2fQ2f1X7YD-VPQVW&index=6