class ReadAndWriteLog():
    def __init__(self):                 
        self.df = []
        self.datas = []
    def addLog(self,data):
        try:
            open('./log/log.txt',mode='a',encoding='utf-8').write(data+'\n')
        except:
            open('./log/log.txt',mode='w',encoding='utf-8').write(data+'\n')
    def getLog(self):
        self.datas = []
        self.df = open('./log/log.txt',mode='r',encoding='utf-8').readlines()
        for i in self.df:
            self.datas.append(i[:-1])
        return self.datas
    def clearLog(self):
        open('./log/log.txt',mode='w',encoding='utf-8').write('')
a = ReadAndWriteLog()
a.addLog("log.txt")
a.addLog("100")
a.addLog("200")
a.addLog("300")
print(a.getLog())
a.clearLog()
