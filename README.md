# Block Brothers
REST API Application

Back-end restfull application for managing co-living complex area with a common sports-center. Regular users have access only to sports-center and
corresponding application. Home owners are owners of a property inside the complex, they can send reports about broken things in the area of the complex. 
Admin roles are home owner managers and admin. The application uses stripe payment service for payment and subscriptions to monthly taxation and sports-center membership.
The project can be extended with additional functionality, like adding a car, it can be integrated with WISE/S3 for uploading photos about maintenance events and etc. 
It has a real life application and customisation for co-living areas and condominiums. It can ease the payments and gathering complex expenses.



## Run the app

   http://localhost:5000/

## Run the tests

    

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
      -H "Authorization: Bearer <admin token>"
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
     -H "Authorization: Bearer <admin token>"
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
     -H "Authorization: Bearer <admin token>"
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

    curl -X POST http://127.0.0.1:5000/home_owner/login \     
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
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjgsImV4cCI6MTY1MDAyNjI3MSwicm9sZSI6IkhvbWVPd25lck1vZGVsIn0.aQ4j66p6_OSS52MzUCsTqevNLiFPG5vaUnp5pBMRCtE",
    "role": "homeowner"
}

## Login Home Owner Manager

### Request

`POST /home_owner/login`

    curl -X POST http://127.0.0.1:5000/home_owner_manager/login \     
     -H "Content-Type: application/json" \
     -d {
          "email":"krasi@balakov.com",
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
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEsImV4cCI6MTY1MDAyNjU1NSwicm9sZSI6IkhvbWVPd25lck1hbmFnZXJNb2RlbCJ9.diU0zf2Zj-2N3-KOOWrqFEfBI7PV7qRFsKCWW_LhbmA",
    "role": "homeowner_manager"
   }

## Add Card
Add card after a user is logged in. The card is saved with its stripe unique number inside the application database, where the card detailes are saved securely in Stripe Account of the Home Owner Manager. Who is in charge of the facility and all the payments and subscriptions.

### Request

`POST /login/add_card`    

 curl -X POST http://127.0.0.1:5000/login/add_card \     
  -H "Authorization: Bearer <user token>"\
  -H "Content-Type: application/json" \
  
  {
    "number" : "4242 4242 4242 4242",
    "card_holder": "NIKOLAY CHALKANOV",
    "exp_month": 4,
    "exp_year": 2022,
    "cvc": "314"
   }
   
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 12:50:34 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 53

    "Successfully added card number **** **** **** 4242"

## Create maintance event
   Only home owners can send a report for a maintenace problem of the facility he lives in. 
   
   
### Request
   
`POST /home_owners/maint_event`  

 curl -X POST http://127.0.0.1:5000/home_owners/maint_event \     
  -H "Authorization: Bearer <home owner token>"\
  -H "Content-Type: application/json" \
  
  {
   "title": "Second floor stairs dirty",
   "content" : "There is oil spilige on the stairs",
   "photo_url": "https://www.something.sn"
   }
   
### Response

    HTTP/1.1 201 Created
    Date: Wed, 05 Jan 2022 12:54:32 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Content-Length: 223

   {
    "created_on": "2022-01-05T14:54:32.047726",
    "title": "Second floor stairs dirty",
    "status": "Pending",
    "content": "There is oil spilige on the stairs",
    "updated_on": null,
    "id": 2,
    "photo_url": "https://www.something.sn"
}

## Close maintenance event
   A maintenace event which is fixed is regarded as closed. The home owner manager has reviewed it and can close it. Changes the status to closed.

### Request
   
`PUT /home_owner_manager/maint_event/<int:id_>/close`  

 curl -X POST http://127.0.0.1:5000//home_owner_manager/maint_event/<int:id_>/close \     
  -H "Authorization: Bearer <home owner manager token>"\
  -H "Content-Type: application/json" \  
     
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 12:54:32 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 21

   {
      "status": "closed"
   }

## Update maintenance event
   
A maintenace event which is submited already can be updated.

### Request
   
`POST /home_owners/maint_event/<int:id>`  

 curl -X POST http://127.0.0.1:5000/home_owners/maint_event/<int:id> \     
  -H "Authorization: Bearer <home owner token>"\
  -H "Content-Type: application/json" \
  -d {
   "title": "Second floor stairs dirty",
   "content" : "There is oil spilige on the stairs. Check right next to the elevator.",
   "photo_url": "https://www.something.sn"
   }
     
### Response

    HTTP/1.1 200 OK
    Date: Wed, 05 Jan 2022 12:54:32 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 21
   
{
    "photo_url": "https://www.something.sn",
    "content": "There is oil spilige on the stairs. Check right next to the elevator.",
    "status": "Closed",
    "updated_on": "2022-01-05T15:09:10.812224",
    "title": "Second floor stairs dirty",
    "created_on": "2022-01-05T14:54:32.047726",
    "id": 2
}
  
## Delete maintenance event
   
The admin can delete the maint event after a period of time.

### Request
   
`DELETE /home_owners/maint_event/<int:id>`  

 curl -X DELETE http://127.0.0.1:5000/home_owners/maint_event/<int:id_> \     
  -H "Authorization: Bearer <home owner token>"\
  -H "Content-Type: application/json" \
  
     
### Response

    HTTP/1.1 204 NO CONTENT
    Date: Wed, 05 Jan 2022 12:54:32 GMT
    Status: 204 NO CONTENT
    Connection: close
    Content-Type: application/json
    


