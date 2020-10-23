def modid(packet):
        try:
                if packet['SMTP']['response'][:3]=='220':
                        a=packet['SMTP']['response'][5:]
                        packet['SMTP']['response']='220-a'+a
                return packet
        except:
                return None