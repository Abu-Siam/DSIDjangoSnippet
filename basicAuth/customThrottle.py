from rest_framework.throttling import  UserRateThrottle

class MyUserRateThrottle(UserRateThrottle):
    scope = 'myuser'