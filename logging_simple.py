import logging

def inputFunc():
    s=input('test: ')
    try:
        i=int(s)
    except:
        print('Error occured')
        print (1/0)
    finally:
        print('Finally clause')
    print("This is what happens after finally")
def openFile():
    name=input('Enter filename: ')
    try:
        f= open(name)
    except FileNotFoundError:
        print("not found")
    
#inputFunc()
    
#openFile()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s- %(name)s - %(relativeCreated)6d %(threadName)s %(message)s')

logging.info('Starting the module')
logging.debug('Error 4003')

