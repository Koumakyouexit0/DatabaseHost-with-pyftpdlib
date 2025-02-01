from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

# foldel chứa tệp tin FTP
FTP_DIRECTORY = "/drive"

# check folder (hãy đảm bảo folder có chạy)
if not os.path.exists(FTP_DIRECTORY):
    os.makedirs(FTP_DIRECTORY)
    
# user và perm (vui lòng đọc sách hdsd)
authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", FTP_DIRECTORY, perm="elradfmw")  
authorizer.add_anonymous(FTP_DIRECTORY, perm="elr")  

# cấu hình handler
handler = FTPHandler
handler.authorizer = authorizer

# chạy máy chủ FTP với TLS trên cổng 2121
server = FTPServer(("127.0.0.1", 21215), handler)

print(f"🔐 FTP Server với TLS đang chạy trên ...")
server.serve_forever()
