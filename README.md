# Real Estate Listings API - Group 4

## Group Members
- **Mathenge Gitahi** - 166078  
- **Samuel Mwesigwa** - 167999  
- **Gloria Munene** - 166074  
- **Larry Mburu** - 132453  
- **Michelle Gitonga** - 151113  
- **Naibei Kimtai** - 150344  

---

## Project Overview
This is a **Real Estate Listings API** built with Django and Django REST Framework (DRF).  
The API allows management of clients, property types, properties, property images, agents, and bookings.  
It is secured with token-based authentication and provides CRUD operations for all resources.


---

## Step-by-Step Implementation 

## Models and Relationships

### 1. **Client**
- Represents customers looking for properties.  
- Fields: `name`, `email`, `phone`.  
- A client can make multiple bookings.

### 2. **Agent**
- Represents property agents working under an agency.  
- Fields: `name`, `email`, `phone`, `agency`, `license_number`.  
- Agents can be linked to multiple properties.

### 3. **PropertyType**
- Defines the type of property.  
- Fields: `name` (e.g., *Apartment, Villa, Office*).  
- Each property must belong to one property type.

### 4. **Property**
- Represents the actual properties available.  
- Fields: `title`, `description`, `price`, `location`, `listed_date`.  
- Relationships: 
  - Linked to **PropertyType** (one-to-many).
  - Linked to **Agent** (one-to-many).
  - Linked to **PropertyImage** (one-to-many).
  - Linked to **Booking** (one-to-many).

### 5. **PropertyImage**
- Stores images of a property.  
- Fields: `property`, `image_url`.  
- Relationship: One property can have multiple images.

### 6. **Booking**
- Represents client bookings for a property.  
- Fields: `client`, `property`, `message`, `status`, `booking_date`.  
- Relationships: 
  - Linked to **Client** (many-to-one).
  - Linked to **Property** (many-to-one).
- Validation: A client cannot book the same property more than once.

---

## Views / ViewSets
- **ModelViewSets** are used for each model (`Client`, `Agent`, `PropertyType`, `Property`, `PropertyImage`, `Booking`).  
- They provide CRUD operations:  
  - `GET` → Retrieve list/detail  
  - `POST` → Create new entries  
  - `PUT/PATCH` → Update existing entries  
  - `DELETE` → Remove entries  
- Custom validation ensures unique booking per client-property pair.

---

## Serializers
- Each model has a corresponding **Serializer** that:
  - Defines exposed fields.  
  - Applies validation rules (e.g., booking uniqueness, required fields).  
  - Converts model instances to JSON and vice versa.

---

## URL Patterns
All endpoints are prefixed with `/api/`:
- `/api/clients/` → CRUD for clients  
- `/api/agents/` → CRUD for agents  
- `/api/property-types/` → CRUD for property types  
- `/api/properties/` → CRUD for properties  
- `/api/property-images/` → CRUD for property images  
- `/api/bookings/` → CRUD for bookings  
- `/api/auth/` → Authentication routes (login, token)

---

## Testing

We tested using **Postman** for all major endpoints.

### Clients
- **POST** `/api/clients/`
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890"
}

GET /api/clients/

PUT /api/clients/1/

DELETE /api/clients/1/

Agents

POST /api/agents/

{
  "name": "Jane Smith",
  "email": "jane@agency.com",
  "phone": "9876543210",
  "agency": "DreamHomes Ltd",
  "license_number": "AG12345"
}

Property Types

POST /api/property-types/

{ "name": "Apartment" }

Properties

POST /api/properties/

{
  "title": "Luxury Apartment",
  "description": "Spacious 3-bedroom apartment.",
  "price": "5000000",
  "location": "Nairobi",
  "property_type": 1,
  "agent": 1,
  "listed_date": "2025-08-20"
}

Property Images

POST /api/property-images/

{
  "property": 1,
  "image_url": "https://example.com/apartment1.jpg"
}

Bookings

POST /api/bookings/

{
  "client": 1,
  "property": 2,
  "message": "Interested in this property for next month.",
  "status": "Confirmed",
  "booking_date": "2025-08-25"
}

Evidence of Tests

All endpoints tested successfully in Postman.

Sample test results:

201 Created on valid POST requests.

200 OK on GET requests.

400 Bad Request on invalid data (e.g., missing required fields).

403 Forbidden when no authentication token is provided.

204 No Content on successful DELETE requests.

(Screenshots of Postman results should be attached here in the final submission.)

How to Run the Project

Clone the repository:

git clone <repo-url>
cd real-estate-api


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run migrations:

python manage.py makemigrations
python manage.py migrate


Create a superuser:

python manage.py createsuperuser


Start the development server:

python manage.py runserver


Test endpoints via Postman at:

http://127.0.0.1:8000/api/

Conclusion

This project implements a Real Estate Listings API with full CRUD support, authentication, and validation rules.
It provides a robust foundation for building a real estate management system with future extensions like search, filters, and user roles.