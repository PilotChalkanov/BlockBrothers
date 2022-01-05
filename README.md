# Block Brothers
REST API Application
Back-end restfull application for managing co-living complex with a common sports-center. The regular users have access only to sports-center and
corresponding application. Home owners are owners of property inside the complex, they can send reports about broken things in the area of the complex. 
Admin roles are home owner managers and admin. It uses stripe payment service for payment and subscriptions to monthly taxation and sports-center membership.



## Run the app

   http://localhost:5000/

## Run the tests

    ./run-tests.sh

# REST API

The REST API app is described below.

## Register Users

### Request

`POST /register/`

    curl -X POST http://127.0.0.1:5000/register/ \     
     -H "Content-Type: application/json" \
     -d '{
    "email":"marti_dimitrov@gmail.com",
    "password":"123456",
    "first_name": "Martin",
    "last_name": "Dimitrov",
    "phone":"1234567891011"     
     }'

### Response

    HTTP/1.1 201 CREATED
    Date: Wed, 05 Jan 2022 09:37:55 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Content-Length: 190

    []

## Login User

### Request

`POST /login/`

    curl -X POST http://127.0.0.1:5000/login/ \     
     -H "Content-Type: application/json" \
     -d '{
    "email":"marti_dimitrov@gmail.com",
    "password":"123456"         
     }'
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 09:57:03 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json    
    Content-Length: 155

    {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEsImV4cCI6MTY1MDAxNTQ3NSwicm9sZSI6IlVzZXJNb2RlbCJ9.PPDa32vasrEE_qEoA5kQ9kjpuBZxw427kOaf2527VrI",
    "stripe_id": "cus_KuKbghTIWtZji9"
    }

## Create Admin

### Request

`POST /create_admin/`

    curl -X POST http://127.0.0.1:5000/admin/create_admin \
      -H "Authorization: Bearer <JWT token>"
     -H "Content-Type: application/json" \
     -d {
    "email":"adam@adam.com",
    "password":"123456",
    "first_name": "Adam",
    "last_name": "Adamov",
    "phone":"1234567891011"    
    }
### Response

    HTTP/1.1 201 CREATED
    Date: Wed, 05 Jan 2022 10:19:55 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 4

    201
    
## Login Admin

### Request

`POST /admin/login`

    curl -X POST http://127.0.0.1:5000/admin/login \     
     -H "Content-Type: application/json" \
     -d {
    "email":"adam@adam.com",
    "password":"123456",       
    }
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 10:29:26 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 167

    {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEsImV4cCI6MTY1MDAxODU2Niwicm9sZSI6IkFkbWluaXN0cmF0b3JNb2RlbCJ9.SCD4j5ya4FKk6VSpSACxKH2HGkYZ2ttEr-AEiMvmpa0"
    }
    
## Create Home Owner

### Request

`POST /admin/create_home_owner`

    curl -X POST http://127.0.0.1:5000/admin/create_home_owner \     
     -H "Authorization: Bearer <JWT token>"
     -H "Content-Type: application/json" \
     -d {
        "email":"aleko@kaleko.com",
        "password":"123456",
        "first_name": "Aleko",
        "last_name": "Kaleko",
        "phone":"1234567891011"    
        }
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 10:54:52 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 197

   {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjgsImV4cCI6MTY1MDAyMDA5Miwicm9sZSI6IkhvbWVPd25lck1vZGVsIn0.EspLTC4d8kCU6KU0iPc3exrd5-eCFd8GoLKDEBwtEq4",
    "stripe_id": "cus_KuLqkT0PJPpXQW"
    }
    
    
## Create Home Owner Manager

### Request

`POST /admin/create_home_owner_manager`

    curl -X POST http://127.0.0.1:5000/admin/create_home_owner_manager \ 
     -H "Authorization: Bearer <JWT token>"
     -H "Content-Type: application/json" \
     -d {
        "email":"krasi@balakov.com",
        "password":"123456",
        "first_name": "Krasi",
        "last_name": "Balakov",
        "phone":"1234567891011"    
        }
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 10:54:52 GMT
    Status: 201 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 197
   

## Login Home Owner

### Request

`POST /home_owner/login`

    curl -X POST http://127.0.0.1:5000//home_owner/login \     
     -H "Content-Type: application/json" \
     -d {
      "email":"aleko@kaleko.com",
      "password":"123456"       
      }
      
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 10:54:52 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 197

   {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjgsImV4cCI6MTY1MDAyMDA5Miwicm9sZSI6IkhvbWVPd25lck1vZGVsIn0.EspLTC4d8kCU6KU0iPc3exrd5-eCFd8GoLKDEBwtEq4",
    "stripe_id": "cus_KuLqkT0PJPpXQW"
    }

## Change a Thing's state

### Request

`PUT /thing/:id/status/changed`

    curl -i -H 'Accept: application/json' -X PUT http://localhost:7000/thing/1/status/changed

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:31 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 40

    {"id":1,"name":"Foo","status":"changed"}

## Get changed Thing

### Request

`GET /thing/id`

    curl -i -H 'Accept: application/json' http://localhost:7000/thing/1

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:31 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 40

    {"id":1,"name":"Foo","status":"changed"}

## Change a Thing

### Request

`PUT /thing/:id`

    curl -i -H 'Accept: application/json' -X PUT -d 'name=Foo&status=changed2' http://localhost:7000/thing/1

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:31 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 41

    {"id":1,"name":"Foo","status":"changed2"}

## Attempt to change a Thing using partial params

### Request

`PUT /thing/:id`

    curl -i -H 'Accept: application/json' -X PUT -d 'status=changed3' http://localhost:7000/thing/1

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:32 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 41

    {"id":1,"name":"Foo","status":"changed3"}

## Attempt to change a Thing using invalid params

### Request

`PUT /thing/:id`

    curl -i -H 'Accept: application/json' -X PUT -d 'id=99&status=changed4' http://localhost:7000/thing/1

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:32 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 41

    {"id":1,"name":"Foo","status":"changed4"}

## Change a Thing using the _method hack

### Request

`POST /thing/:id?_method=POST`

    curl -i -H 'Accept: application/json' -X POST -d 'name=Baz&_method=PUT' http://localhost:7000/thing/1

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:32 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 41

    {"id":1,"name":"Baz","status":"changed4"}

## Change a Thing using the _method hack in the url

### Request

`POST /thing/:id?_method=POST`

    curl -i -H 'Accept: application/json' -X POST -d 'name=Qux' http://localhost:7000/thing/1?_method=PUT

### Response

    HTTP/1.1 404 Not Found
    Date: Thu, 24 Feb 2011 12:36:32 GMT
    Status: 404 Not Found
    Connection: close
    Content-Type: text/html;charset=utf-8
    Content-Length: 35

    {"status":404,"reason":"Not found"}

## Delete a Thing

### Request

`DELETE /thing/id`

    curl -i -H 'Accept: application/json' -X DELETE http://localhost:7000/thing/1/

### Response

    HTTP/1.1 204 No Content
    Date: Thu, 24 Feb 2011 12:36:32 GMT
    Status: 204 No Content
    Connection: close


## Try to delete same Thing again

### Request

`DELETE /thing/id`

    curl -i -H 'Accept: application/json' -X DELETE http://localhost:7000/thing/1/

### Response

    HTTP/1.1 404 Not Found
    Date: Thu, 24 Feb 2011 12:36:32 GMT
    Status: 404 Not Found
    Connection: close
    Content-Type: application/json
    Content-Length: 35

    {"status":404,"reason":"Not found"}

## Get deleted Thing

### Request

`GET /thing/1`

    curl -i -H 'Accept: application/json' http://localhost:7000/thing/1

### Response

    HTTP/1.1 404 Not Found
    Date: Thu, 24 Feb 2011 12:36:33 GMT
    Status: 404 Not Found
    Connection: close
    Content-Type: application/json
    Content-Length: 35

    {"status":404,"reason":"Not found"}

## Delete a Thing using the _method hack

### Request

`DELETE /thing/id`

    curl -i -H 'Accept: application/json' -X POST -d'_method=DELETE' http://localhost:7000/thing/2/

### Response

    HTTP/1.1 204 No Content
    Date: Thu, 24 Feb 2011 12:36:33 GMT
    Status: 204 No Content
    Connection: close

