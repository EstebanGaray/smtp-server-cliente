def modcod(packet):
        try:
                if packet['SMTP']['response'][0:13]=='250 recipient':
                        a=packet['SMTP']['response'][3:]
                        packet['SMTP']['response']="550"+a
                        return packet
                else:
                        return packet
        except:
                return None