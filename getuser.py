#OKTAユーザ情報を取得する
def getUserInfo(pusername,token_secret,user_client_id):
    #00u4ifwtcqYRfHeRY5d7
    #00Zm-258gdM_13mc-MGrCqCvvfqaNJWKOinQdk-r5T
    pusername="wangliang"
    user_client_id="00u4ifwtcqYRfHeRY5d7"
    token_secret="00Zm-258gdM_13mc-MGrCqCvvfqaNJWKOinQdk-r5T"
    user_info_json={}
    
    #·ヘーダを定義する
    if token_secret:
        myheaders = {'Authorization':"SSWS "+token_secret,'Accept':'application/json','Content-Type': 'application/json'}
    
    #userinfo_response対象を取得する
    if user_client_id:
        userinfo_response= requests.get(f'https://dev-97030065.okta.com/api/v1/users/'+user_client_id,headers=myheaders).json()

    #Usernameを取得する
    if pusername:
        user_info_json["Username"]=pusername
        
    #firstNameを取得する
    if userinfo_response["profile"]["firstName"]:
        user_info_json["firstName"]=userinfo_response["profile"]["firstName"]

    #lastNameを取得する
    if userinfo_response["profile"]["lastName"]:
        user_info_json["lastName"]=userinfo_response["profile"]["lastName"]
    
    #Middle nameを取得する
    if userinfo_response["profile"]["middleName"]:
        user_info_json["middleName"]=userinfo_response["profile"]["middleName"]
    
    #honorificPrefixを取得する
    if userinfo_response["profile"]["honorificPrefix"]:
        user_info_json["honorificPrefix"]=userinfo_response["profile"]["honorificPrefix"]
    
    #honorificSuffixを取得する
    if userinfo_response["profile"]["honorificSuffix"]:
        user_info_json["honorificSuffix"]=userinfo_response["profile"]["honorificSuffix"]
    
    #PRIMARY Mail
    if userinfo_response["credentials"]["emails"]:
        for k in userinfo_response["credentials"]["emails"]:
            if k["type"]=="PRIMARY":
                if k["value"]:
                    user_info_json["email"]=k["value"]

    #titleを取得する
    if userinfo_response["profile"]["title"]:
        user_info_json["title"]=userinfo_response["profile"]["title"]
    
    #displayNameを取得する
    if userinfo_response["profile"]["displayName"]:
        user_info_json["displayName"]=userinfo_response["profile"]["displayName"]
    
    #nickNameを取得する
    if userinfo_response["profile"]["nickName"]:
        user_info_json["nickName"]=userinfo_response["profile"]["nickName"]
    
    #profileUrlを取得する
    if userinfo_response["profile"]["profileUrl"]:
        user_info_json["profileUrl"]=userinfo_response["profile"]["profileUrl"]
    
    total_json=json.dumps(user_info_json)
    print("------user_info_json------------:"+total_json)
