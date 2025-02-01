from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

# chứng chỉ SSL
CERTFILE = "cert.pem"
KEYFILE = "key.pem"

# foldel chứa tệp tin FTP
FTP_DIRECTORY = "/drive"

# check folder (hãy đảm bảo folder có chạy)
if not os.path.exists(FTP_DIRECTORY):
    os.makedirs(FTP_DIRECTORY)
    
# user và perm (vui lòng đọc sách hdsd)
authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", FTP_DIRECTORY, perm="elradfmw")  
authorizer.add_anonymous(FTP_DIRECTORY, perm="elr")  

# cấu hình handler với TLS
handler = FTPHandler
handler.authorizer = authorizer

handler.tls_control_required = True
handler.tls_data_required = True
handler.certfile = "cert.pem" 
handler.keyfile = "key.pem" 

# chạy máy chủ FTP với TLS trên cổng 2121
server = FTPServer(("192.168.1.11", 21215), handler)

print(f"🔐 FTP Server với TLS đang chạy trên ...")
server.serve_forever()
