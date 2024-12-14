### `views.py` Documentation

This document provides a detailed explanation of the functionality of each view in the `views.py` file, including how the data is displayed in the API and how `auth.token` is implemented for authentication.

---

#### **1. RegisterAPIView**
**Purpose:**
Allows new users to register by providing their credentials (e.g., username and password).

**Class:**
- Inherits from `CreateAPIView`.

**Key Features:**
- **Queryset:** Retrieves all users from the `User` model.
- **Serializer:** Uses `UserSerializer` to validate and save user data.

**Authentication:**
- No authentication required for registration.

**How It Works:**
- Accepts a `POST` request with `username` and `password` in the request body.
- Creates a new user in the database.

---

#### **2. LoginAPIView**
**Purpose:**
Authenticates a user and provides an authentication token upon successful login.

**Class:**
- Inherits from `APIView`.

**Key Features:**
- Accepts `POST` requests only.
- Authenticates the user using `username` and `password`.

**Authentication:**
- Token-based authentication is implemented using `Token` from `rest_framework.authtoken.models`.

**How It Works:**
1. Extracts `username` and `password` from the request data.
2. Authenticates the user using Django's `authenticate` function.
3. If the user is valid:
   - Retrieves or creates a token for the user.
   - Logs the user in using `login()`.
   - Returns the token in the response.
4. If invalid, returns an error response with status code `401`.

---

#### **3. ProductCreateAPIView**
**Purpose:**
Allows authenticated users to create new products. Restricted to staff users only.

**Class:**
- Inherits from `CreateAPIView`.

**Key Features:**
- **Queryset:** Retrieves all `Product` objects.
- **Serializer:** Uses `ProductSerializer` to validate and save product data.
- **Permission:** Only accessible to authenticated staff users (`IsAuthenticated`).

**How It Works:**
1. Accepts a `POST` request with product data in the body.
2. Validates the data using the serializer.
3. Saves the product to the database if the user has the necessary permissions.
4. Returns the created product details.

---

#### **4. InventoryListAPIView**
**Purpose:**
Displays a list of all available products in the inventory for authenticated users.

**Class:**
- Inherits from `ListAPIView`.

**Key Features:**
- **Queryset:** Retrieves all `Product` objects.
- **Serializer:** Uses `ProductSerializer` to format the data.
- **Permission:** Restricted to authenticated users (`IsAuthenticated`).

**How It Works:**
1. Accepts a `GET` request.
2. Fetches all products from the database.
3. Returns the data in a serialized format.

---

#### **5. ProductDetailAPIView**
**Purpose:**
Displays the details of a specific product based on its ID.

**Class:**
- Inherits from `RetrieveAPIView`.

**Key Features:**
- **Queryset:** Retrieves all `Product` objects.
- **Serializer:** Uses `ProductSerializer` to format the data.
- **Permission:** Restricted to authenticated users (`IsAuthenticated`).

**How It Works:**
1. Accepts a `GET` request with a product ID.
2. Retrieves the product with the given ID.
3. Returns the product's details in a serialized format.

---

#### **6. LogOutAPIView**
**Purpose:**
Logs out an authenticated user by invalidating their authentication token.

**Class:**
- Inherits from `APIView`.

**Key Features:**
- **Authentication:** Uses `TokenAuthentication`.
- **Permission:** Restricted to authenticated users (`IsAuthenticated`).

**How It Works:**
1. Accepts a `POST` request.
2. Retrieves the token associated with the authenticated user.
3. Deletes the token from the database to invalidate it.
4. Returns a success message upon logout.
5. If the token does not exist, returns an error response.

---

### **Authentication with `auth.token`**

**How Token Authentication is Used:**
- The `TokenAuthentication` class is used in the `LogOutAPIView` to secure the endpoint.
- When a user logs in, they are issued a unique token.
- The token must be included in the `Authorization` header for all subsequent requests:
  ```
  Authorization: Token your_token_here
  ```

**Steps to Use Token Authentication:**
1. Login via the `LoginAPIView` to obtain a token.
2. Include the token in the `Authorization` header for any protected endpoint.
3. Use the `LogOutAPIView` to invalidate the token when the user logs out.

---

### **Error Handling**
- **401 Unauthorized:** Returned when:
  - The token is not provided in the `Authorization` header.
  - The token is invalid or expired.
- **Permission Denied:** Occurs if the user does not have the required permissions for certain endpoints (e.g., creating products).
- **Validation Errors:** If invalid data is submitted, the serializer returns detailed error messages.


