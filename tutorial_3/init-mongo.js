var db = connect("mongodb://localhost/mydb");

db.createRole(
    {
        role: "somerole",
        privileges: [
            {
              actions: [ "find", "update", "insert" ],
              resource: { db: "mydb", collection: "" }
            }
          ],
        roles: [  ]
    }
)

db.createUser(
    {
        user: "admin",
        pwd: "adminpass",
        roles: [ { role: "somerole", db: "mydb" } ]
    }
)

db.createUser(
    {
        user: "system",
        pwd: "systempass",
        roles: [ { role: "somerole", db: "mydb" } ]
    }
)