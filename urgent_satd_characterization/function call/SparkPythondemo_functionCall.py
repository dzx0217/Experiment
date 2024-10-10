import SparkApi_functionCall
#以下密钥信息从控制台获取

appid = "b24d9eaf"     #填写控制台中获取的 APPID 信息
api_secret = "NDk1ZTg0ZjY0ZTdmMTZlY2EzYWI1NDZm"   #填写控制台中获取的 APISecret 信息
api_key ="026cf9486631a31bf441ad99c68ebc23"    #填写控制台中获取的 APIKey 信息

#配置大模型版本
# domain = "generalv3.5"    # Max版本
domain = "4.0Ultra"    # v4.0版本


#云端环境的服务地址

# Spark_url = "ws://spark-api.xf-yun.com/v3.5/chat"  # v3.5环境的地址
Spark_url = "wss://spark-api.xf-yun.com/v4.0/chat"  # v4.0环境的地址

text =[]

# length = 0

def getText(role,content):
    text.clear()
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text
    


if __name__ == '__main__':

    # while(1):
        Input = input("\n" +"我:")
        question = checklen(getText("user",Input))
        # question = [{"role":"user","content":"十一假期太短了，我必须得请两天"}]
        print(question)
        SparkApi_functionCall.answer =""
        print("星火:",end = "")
        SparkApi_functionCall.main(appid,api_key,api_secret,Spark_url,domain,question)
        getText("assistant",SparkApi_functionCall.answer)
        # print("sid:" + SparkApi2.sid)

