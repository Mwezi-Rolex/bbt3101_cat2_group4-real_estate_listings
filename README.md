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
This project is a **Django REST Framework API** for managing real estate property listings.  
It allows for the creation, retrieval, update, and deletion of data related to properties, agents, clients, images, and bookings.

---

## Step-by-Step Implementation (So Far)

### 1. Models
We have defined **five models** to represent the main entities in a real estate listing system:

1. **Agent** – Stores agent details such as name, email, phone, agency, and license number.  
2. **Property** – Represents real estate listings with title, description, price, location, type, size, and the agent assigned to it.  
3. **PropertyImage** – Stores images for each property, linked via a foreign key.  
4. **Client** – Represents potential customers who may inquire or book properties.  
5. **Booking** – Records inquiries/bookings made by clients for specific properties, including messages, date sent, and booking status.

**Relationships:**
- One **Agent** can have many **Properties** (`One-to-Many`).  
- One **Property** can have many **PropertyImages** (`One-to-Many`).  
- One **Client** can make many **Bookings** (`One-to-Many`).  
- Each **Booking** is linked to one **Property** and one **Client**.

---

### 2. Serializers
Serializers were created for each model to transform model data into JSON and vice versa.  
- **AgentSerializer** – Serializes agent data.  
- **PropertySerializer** – Includes nested `PropertyImageSerializer` to return property images along with property data.  
- **PropertyImageSerializer** – Serializes property image details.  
- **ClientSerializer** – Serializes client details.  
- **BookingSerializer** – Serializes booking details.

**Validation Rules Implemented So Far:**  
Currently, default DRF `ModelSerializer` validation is used (required fields, correct field types, unique constraints from models).

---

### 3. Views/Viewsets
We implemented **ModelViewSets** for each model to provide CRUD operations automatically:  
- `AgentViewSet` – Manage agents.  
- `PropertyViewSet` – Manage property listings.  
- `PropertyImageViewSet` – Manage property images.  
- `ClientViewSet` – Manage client records.  
- `BookingViewSet` – Manage bookings.  

Each viewset supports:
- `GET` (list and retrieve)
- `POST` (create)
- `PUT/PATCH` (update)
- `DELETE` (remove)

---

### 4. URLs
We used Django REST Framework’s `DefaultRouter` to generate RESTful endpoints automatically:
- `/api/agents/` – Manage agents  
- `/api/properties/` – Manage properties  
- `/api/property-images/` – Manage property images  
- `/api/clients/` – Manage clients  
- `/api/bookings/` – Manage bookings  

In the main project `urls.py`, all app routes are included under the `/api/` prefix.

---

## Current Status
✅ Models created with relationships  
✅ Serializers implemented  
✅ CRUD Viewsets implemented  
✅ URL routing configured  
⬜ Testing (Postman/Django tests) – **pending**  
⬜ Documentation of test results – **pending**  

---

## Next Steps
1. Implement custom validation rules (e.g., positive price, valid booking dates).
2. Add permission controls for agents and clients.
3. Test API endpoints using Postman and document results.
4. Finalize README with test evidence.

---
