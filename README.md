# TechSystem: Applying the CAP Model with MongoDB and PostgreSQL

## Team Members
- Cristian Eduardo Botina (A00395008)  
- Juan Manuel Marín (A00382037)  
- Óscar Andrés Gómez (A00394142)  

## Overview
TechSystem is a web-based platform designed to manage the rental of technology equipment. The system leverages both PostgreSQL and MongoDB to balance the needs for consistency, availability, and partition tolerance as outlined in the CAP theorem. This document explains the rationale behind the technology stack, how the CAP model is applied, and the architectural choices made for the solution.



## CAP Model in TechSystem

### PostgreSQL: Consistency and Availability
PostgreSQL, a relational database management system, was chosen to manage structured and strongly consistent data. The key reasons for deploying PostgreSQL include:

- **Consistency**: PostgreSQL ensures ACID compliance, which is critical for managing transactional data such as contracts, delivery certificates, and customers.
- **Availability**: Deployed on Render, PostgreSQL ensures high uptime and reliable access to data.

PostgreSQL was used to maintain the structured model provided in the initial system requirements. An additional table was added:

- **SpecificAttributes**: This table defines the specific attributes available for each category of equipment (e.g., laptops, printers). This structure allows dynamic handling of different attribute sets while maintaining relational integrity.

The enhanced PostgreSQL schema provides:
1. **Category Definitions**: Strongly defined categories with unique identifiers.
2. **Extensible Attributes**: The flexibility to handle attribute variability without compromising schema integrity.



### MongoDB: Partition Tolerance and Schema Flexibility
MongoDB, a NoSQL database, was introduced to handle dynamic and semi-structured data, specifically:

- **Products**: Products have flexible attributes that vary by category, making MongoDB ideal due to its schema-less nature.
- **Rental Requests**: These documents include nested arrays and references to products, simplifying the representation and retrieval of complex relationships.

#### MongoDB Collections
1. **Products**:
   - **Category ID**: References the PostgreSQL category.
   - **Attributes**: Stored as key-value pairs, allowing dynamic definitions for each product.
   - **Example Document**:
     ```json
     {
       "_id": "unique_product_id",
       "category_id": "laptops",
       "common_attributes": {
         "brand": "HP",
         "model": "ProBook 745",
         "price": 750.00,
         "stock": 15
       },
       "specific_attributes": {
         "processor": "AMD Ryzen 5",
         "ram": "16 GB",
         "storage": "512 GB SSD"
       }
     }
     ```

2. **Rental Requests**:
   - **Customer NIT**: Identifies the customer.
   - **Request Date**: Tracks when the request was made.
   - **Status**: Tracks the state of the request (e.g., pending, approved).
   - **Products Array**: Contains product IDs and quantities.
   - **Example Document**:
     ```json
     {
       "_id": "unique_request_id",
       "customer_nit": "900123456",
       "request_date": "2024-11-22",
       "status": "pending",
       "products": [
         { "product_id": "unique_product_id", "quantity": 2 },
         { "product_id": "another_product_id", "quantity": 1 }
       ]
     }
     ```

### Why MongoDB?
MongoDB was selected due to its quality attributes:
- **Availability**: Deployed on Mongo Atlas, ensures high uptime and reliable access to data, storing products with varying attributes dynamically.
- **Partition Tolerance**: MongoDB’s distributed architecture is robust against network partitioning.



## Framework Selection: Why Django?
Django was chosen as the framework for TechSystem due to its:
- **Rapid Development**: Built-in tools for authentication, ORM, and administrative interfaces.
- **ORM Support**: Seamless integration with PostgreSQL through its default ORM and compatibility with MongoDB using `mongoengine`.
- **Scalability**: Django’s modular design supports future growth of the application.



## Deployment Details
- **PostgreSQL**:
  - Hosted on Render, ensuring high availability and scalability.
  - Stores relational data, including categories, customers, contracts, and delivery certificates.

- **MongoDB**:
  - Hosted locally or on MongoDB Atlas for flexibility.
  - Manages collections for products and rental requests.



## Functional Requirements
1. **Customer Login**:
   - Customers must be able to log in using their credentials.
2. **View Active Rentals**:
   - Customers should view all currently rented equipment with details such as contract ID, start and end dates, and monthly rental cost.
3. **Submit Rental Requests**:
   - Customers should browse available products, filter by category, and submit rental requests.
4. **Dynamic Attribute Display**:
   - The system should dynamically display product attributes based on the category (e.g., processor for laptops, printing technology for printers).
5. **Manage Contracts and Delivery Certificates**:
   - Administrators must manage contracts and associated delivery certificates, including linking them to equipment.



## Non-Functional Requirements
1. **Scalability**:
   - MongoDB’s schema-less nature ensures the system can handle new product categories without altering the structure.
2. **Data Consistency**:
   - PostgreSQL ensures ACID compliance for critical transactional data like contracts and delivery certificates.
3. **Availability**:
   - PostgreSQL hosted on Render provides reliable uptime and fast query responses.
4. **Partition Tolerance**:
   - MongoDB’s distributed model ensures data availability even in case of network issues.
5. **Performance**:
   - The system must handle concurrent users browsing products and submitting requests with minimal latency.
6. **Security**:
   - Customer data and login credentials must be securely stored and managed using industry best practices.
7. **Usability**:
   - The web interface must be intuitive and responsive across devices.



## Conclusion
By combining PostgreSQL and MongoDB, TechSystem leverages the strengths of both relational and NoSQL databases. This hybrid approach balances the CAP theorem’s constraints effectively, providing a robust, flexible, and scalable solution for managing technology rentals. Django further simplifies development and deployment, ensuring the system is maintainable and extensible.

