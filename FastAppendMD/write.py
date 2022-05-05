#Test
from time import gmtime, strftime
data = open('test.txt','a')

data.write('\n' + strftime("%Y%m%d%H%M%S", gmtime()) + ' ' + text)

data.close()