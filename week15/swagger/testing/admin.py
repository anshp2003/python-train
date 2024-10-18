from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CustomUser)
admin.site.register(Address)
admin.site.register(PhoneNumber)


{
    "users":[
        {"id":"1",
        "name":"hardik",
        "addresses":[
            {"id":"1",
            "name":"ranip"}
        ],
        "phonenumbers":[
            {"id":"1",
            "name":"565464564"}
        ]}
    ]
}


{
    "id": 1,
    "name": "hardik",
    "addresses": [
        {
            "id": 1,
            "name": "ranip"
        }
    ],
    "phonenumbers": [
        {
            "id": 1,
            "name": "565464564"
        }
    ]
}
