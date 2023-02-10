from rest_framework.throttling import UserRateThrottle

class ChecckRateThrottle(UserRateThrottle):
    scope = 'check'