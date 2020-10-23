def modcomando(packet):
        try:
                if packet['IP']['proto'] == 6:
                        if packet['SMTP']['command_line'][0:4]=='DATA':
                                packet['SMTP']['command_line']='QUIT\r\n'
                return packet
        except:
                return None