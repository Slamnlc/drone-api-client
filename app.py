from drone_api_client.drone_api_client import DroneApi

if __name__ == '__main__':
    dr = DroneApi()
    x = dr.user.get_user_info()
    z = dr.users.get_user_info(x.login)
    1==1