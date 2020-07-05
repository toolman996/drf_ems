from rest_framework.response import Response


class ApiResponse(Response):
    def __init__(self, data_status=200,data_message='提示信息',result=None,http_status=None,headers=None,
                 exception=False,**kwargs):
        data={
            'status':data_status,
            'message':data_message,
        }
        #判断result
        if result:
            data['result']=result
        #接受参数
        data.update(kwargs)
        super().__init__(data=data,status=http_status,headers=headers,exception=exception)
