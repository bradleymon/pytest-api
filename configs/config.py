import configparser
import random

config = configparser.ConfigParser()
config.read('configs/config.ini')

# TODO add command line arg for target environment
env_name = "DARWIN-QA"

# Get key for environment with fallback to default if not found
def get(key):
    if config[env_name][key] is not None:
        return config[env_name][key]
    return config['DEFAULT'][key]


def rand_x_digit_num(x, leading_zeroes=True):
    """Return an X digit number, leading_zeroes returns a string, otherwise int"""
    if not leading_zeroes:
        # wrap with str() for uniform results
        return random.randint(10**(x-1), 10**x-1)
    else:
        if x > 6000:
            return ''.join([str(random.randint(0, 9)) for i in xrange(x)])
        else:
            return '{0:0{x}d}'.format(random.randint(0, 10**x-1), x=x)

