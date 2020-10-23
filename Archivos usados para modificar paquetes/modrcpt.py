def modrcpt(packet):
        try:
                if packet['IP']['proto']==6:
                        if packet['SMTP']['command_line'][0:4]=='RCPT':
                                #print("hola")
                                nuevo="RCPT TO:<camb@haraka.test>\x0d\x0a"
                                orig_size=len(packet['SMTP']['command_line'])
                                diff=len(nuevo)-orig_size
                                packet['SMTP']['command_line']=nuevo
                                packet['IP']['len']+=diff
                return packet
        except:
                return None
