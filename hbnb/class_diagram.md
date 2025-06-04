```mermaid

flowchart TD

classDiagram

class User {
  id
  first_name
  last_name
  email
  password
  is_admin
  created_at
  updated_at

  register()
  updateProfile()
  delete()
  login()
}

class Place {
  id
  title
  description
  price
  latitude
  longitude
  created_at
  updated_at

  create()
  update()
  delete()
  list()
  getDetails()
}

class Review {
  id
  user_id
  place_id
  rating
  comment
  created_at
  updated_at

  create()
  update()
  delete()
  listByPlace()
  editReview()
}

class Amenity {
  id
  name
  description
  created_at
  updated_at

  create()
  update()
  delete()
  list()
}

%% Relations
User --> Review : writes
User --> Place : owns
Place --> Review : receives
Place o-- Amenity : has

```

---
