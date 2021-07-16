import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token

    def upload(self, file_from,file_to):
        db=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        db.files_upload(f.read(), file_to)

def main():
    access_token="JhbcWnh-C6cAAAAAAAAAAT70P7DuQoK_-rbd5DKTvTAdqMql-uFFmm-cppm-mIxy"
    TransferData(access_token)

    file_from=input("Enter the file path to transfer: ")
    file_to=input("Enter the full file path to transfer: ")

    TransferData.upload(file_from,file_to)
    print("File has been moved.")

    

