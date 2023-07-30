import json 
    
# session databesas
class Session_databesas:

    def __init__(self):
        self.PAT =   r'data/Sessions.json'

    def ADD_SESSION(self ,api_hash: str ,api_id: str ,phone: str ,seesion_string: str 
        ,first_name: str ,accont_id: str ,username : str ,):
        # open session databesas file 
        with open(self.PAT ,'r') as JSObjRead:
            JSObj = json.load(JSObjRead)
        # session id
        session_id = len(JSObj['sessions'])+1
        # add data
        JSObj['sessions'].update({f'session_{str(session_id)}':{"id":session_id,"api_hash":api_hash ,"api_id":api_id,"phone":phone,'session':seesion_string,'first_name':first_name,'username':username,'accont_id':accont_id,'is_block':False,'floodwait_block':False,'timet_block':0}})

        # update Json File
        with open(self.PAT ,'w') as JSObjWireat:
            json.dump(JSObj , JSObjWireat,indent=3)

    def READ_SESSIONS(self ,):
        with open(self.PAT ,'r') as JSObjRead:
            JSObj = json.load(JSObjRead)
        return JSObj

    # Updata Sessions Data
    def UPDATA(self, UP_DATA):
        with open(self.PAT ,'w') as JSFile:
            json.dump(UP_DATA,JSFile, indent=3)
    # get sessions count 
    def GET_SESSION_COUNT(self ,):
            # open session databesas file 
        with open(self.PAT ,'r') as JSObjRead:
            JSObj = json.load(JSObjRead)
        # session id
        session_count = len(JSObj['sessions'])

        return session_count

    def DELET_SESSION(self, session_id: str ,):
        sessions = self.READ_SESSIONS()
        sessions['sessions'].pop(session_id)
        with open(self.PAT ,'w') as JSObjWireat:
            json.dump(sessions , JSObjWireat,indent=3)
    
    def CHACHK_SESSION(self ,API_HASH : str ,API_ID : int ,PHONE : str ,):
        RETUERE = True
        sessions = self.READ_SESSIONS()
        for i in sessions['sessions']:
            if PHONE in sessions['sessions'][i]['phone'] or API_ID == sessions['sessions'][i]['api_id'] or API_HASH ==  sessions['sessions'][i]['api_hash']:
                RETUERE = False
            else : 
                RETUERE = True
        return RETUERE
