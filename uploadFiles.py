import dropbox
import os

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFile(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,"rb")
        dbx.files_upload(f.read(),dropbox_path)

        for root, dirs, files in os.walk(file_from):
            local_path = root
            dirs = dirs
            files = files
        dropbox_path = os.path.join(file_to,relative_path)
        relative_path = os.path.relpath(local_path,file_to)

def main():
    access_token = "sl.BJB7YeLZAK_FSfvCPDlQMUud1KkzvREpxi7LDp3kRoU7ZFr87MUsz1svzVzrtYaZLeELo0u10UL3vKVdPL73C6YrcVZN3Xf99Un0DpjN33Yaskr4FLWxY6r6WjQ83AwHl2OKqMh2Dgs"
    td = TransferData(access_token)
    file_from = input("Enter File Path to be backed up: ")
    file_to= input("Enter dropbox path: ")
    td.uploadFile(file_from,file_to)
    print("File has been moved")

main()