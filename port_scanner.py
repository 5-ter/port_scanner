import socket
import sys


ports = []
arg_len = len(sys.argv)
default_list = [20,21,22,23,25,53,80,443,3306,3389]

#see if ip is set
if arg_len > 1:
    ip = sys.argv[1]
else:
    print("ip not set")
    sys.exit()

#check if ip is valid
try:
    socket.inet_aton(ip)
    pass
except :
    print("invalid ip")
    sys.exit()


#set ports list
if arg_len > 2:
    if sys.argv[2] == "--full":
        #set full range
        ports = range(1,65535 + 1)
       
    elif sys.argv[2] == "--range" and arg_len == 5 :

        try:
            n1 = int(sys.argv[3])
            n2 = int(sys.argv[4])
            start = min(n1, n2)
            end   = max(n1, n2)

            if start < 1 or end > 65535:
                print("range must be between 1-65535, using default")
                ports = default_list
            else:
                ports = range(start, end +1)

        except ValueError:
            print("invalid range, using default")
            ports = default_list
else:
    ports = default_list



for port in ports:

    new_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.settimeout(5)

    try:
        new_socket.connect((ip, port))
        print(f"port {port} is open")
        
    except ConnectionRefusedError:
        print(f"Port {port} is closed")
    except socket.timeout:
        print(f"Port {port} failed to connect")
    except OSError as e:
        print(f"port {port} error: {e}")

    finally:
        new_socket.close()
       







    


