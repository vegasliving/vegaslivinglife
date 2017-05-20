from rets.client import RetsClient

client = RetsClient(
    login_url='http://rets.las.mlsmatrix.com/rets/login.ashx',
    username='tinoco',
    password='lv360',
    # Ensure that you are using the right auth_type for this particular MLS
    # auth_type='basic',
    # Alternatively authenticate using user agent password
    # user_agent='rets-python/0.3',
    # user_agent_password=''
)

resource = client.get_resource('Property')
print(resource.key_field)


