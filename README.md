## How to Install

1. Git Clone

```
git clone http://aidhere-gmbh-donhty@git.codesubmit.io/aidhere-gmbh/book-api-for-wookies-xffusz
```

2. Setting

```
cd book-api-for-wookies-xffusz
python3 -m venv env
(For Mac) source env/bin/activate
(For Windows) env/Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Testing

1. There are two apps (users and books) and overall 7 test cases.

2. To run users tets cases

```
python3 manage.py test apps.users
```

3. To run books test cases

```
python3 manage.py test apps.books
```

4. I have also created a test account in postman cloud to hit apis.

```
https://www.postman.com/
```

5. Login to postman using below credentials.

```
email: testdeekhari00716@gmail.com
password: Test@00716
```

6. Go to ```collections``` -> ```Aidhere Test```

7. ```Auth``` folder contains the authentication api and ```Book``` folder has all book api.


### Objective

Your assignment is to implement a bookstore REST API using Python and any framework. While we will allow the use of any framework you prefer (incl. none at all) we would be grateful if you could complete the assignment in FastAPI or Django if you prefer.

### Brief

Lohgarra, a Wookie from Kashyyyk, has a great idea. She wants to build a marketplace that allows her and her friends to
self-publish their adventures and sell them online to other Wookies. The profits would then be collected and donated to purchase medical supplies for an impoverished Ewok settlement.

### Tasks

-   Implement assignment using:
    -   Language: **Python**
    -   Framework: **any framework** (preferred: FastAPI or Django)
-   Implement a REST API returning JSON or XML based on the `Content-Type` header
-   Implement a custom user model with a "author pseudonym" field
-   Implement a book model. Each book should have a title, description, author (your custom user model), cover image and price
    -   Choose the data type for each field that makes the most sense
-   Provide an endpoint to authenticate with the API using username, password and return a JWT 
-   Implement REST endpoints for the `/books` resource #####done
    -   No authentication required #####done
    -   Allows only GET (List/Detail) operations #######done
    -   Make the List resource searchable with query parameters ####done
-   Provide REST resources for the authenticated user
    -   Implement the typical CRUD operations for this resource #####done
    -   Implement an endpoint to unpublish a book (DELETE) #### done
-   Implement tests as you see fit
    -   These could be unit test as well as API tests
    -   We would also count schema based validation as testing

### Evaluation Criteria

-   **Python** best practices
-   If you are using a framework make sure best practices are followed for models, configuration and tests
-   Sanity and usefulness of tests
-   Protect users' data
    -   Make sure that users may only unpublish and change their own books
-   Bonus: Make sure the user _Darth Vader_ is unable to publish his work on Wookie Books ###done

### CodeSubmit

Please organize, design, test and document your code as if it were
going into production - then push your changes to the master branch. After you have pushed your code, you may submit the assignment on the assignment page.

All the best and happy coding,

The aidhere GmbH Team