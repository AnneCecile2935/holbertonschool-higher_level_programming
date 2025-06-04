```mermaid

flowchart TD

classDiagram

    %% Classe User
    class User {
        +UUID4 id
        +String first_name
        +String last_name
        +String email
        +String password
        +bool is_admin
        +Date created_at
        +Date updated_at

        +register()
        +updateProfile()
        +delete()
        +login()
    }

    %% Classe Place
    class Place {
        +UUID4 id
        +String title
        +String description
        +float price
        +float latitude
        +float longitude
        +Date created_at
        +Date updated_at

        +create()
        +update()
        +delete()
        +list()
        +getDetails()
    }

    %% Classe Review
    class Review {
        +UUID4 id
        +UUID4 user_id
        +UUID4 place_id
        +int rating
        +String comment
        +Date created_at
        +Date updated_at

        +create()
        +update()
        +delete()
        +listByPlace()
        +editReview()
    }

    %% Classe Amenity
    class Amenity {
        +UUID4 id
        +String name
        +String description
        +Date created_at
        +Date updated_at

        +create()
        +update()
        +delete()
        +list()
    }

    %% Relations (déclarées après les classes)
    User "1" -- "*" Review : writes
    User "1" -- "*" Place : owns
    Place "1" -- "*" Review : receives
    Place "1" o-- "*" Amenity : has

```

---
