class Handler:
    '''
    对Parser发起的方法调用进行处理的对象
    Parser将对每个文本块调用方法start()和end()，并将合适
    的文本块名称作为参数。方法sub()将用于正则表达式替换，
    使用诸如'emphasis'等名称调用时，这个方法将返回相应的
    替换函数
    '''
    def callback(self, prefix, name, *args):