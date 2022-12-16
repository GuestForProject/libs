import configparser

config = configparser.ConfigParser()
config.sections()
config.read('assets/example.ini')
config.sections()

print(config['bitbucket.org']['User'])
print(config['DEFAULT']['Compression'])
topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])
print(topsecret['Port'])
for key in config['bitbucket.org']:
    print(key)

config['bitbucket.org']['ForwardX11']
