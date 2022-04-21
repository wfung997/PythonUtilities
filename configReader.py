from configparser import ConfigParser, ExtendedInterpolation


class Config():
    def read_config(config_file) :
        config = ConfigParser(
            interpolation=ExtendedInterpolation())
        config.read(filenames=config_file)
        return config
    

# def test():
#     config_file='system.conf'
#     config=Config.read_config(config_file)
#     print(f'{config.sections()=}')
#     print(f"{config['DEFAULT']['uri']=}")
#     return config

# test()