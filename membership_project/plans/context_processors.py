from django.conf import settings
import environ
env = environ.Env()
environ.Env.read_env()

def data_key(_):
  return {'DATA_KEY': env('STRIPE_PUBLIC_API_KEY')}

SECRET_KEY = env('STRIPE_PRIVATE_API_KEY')
