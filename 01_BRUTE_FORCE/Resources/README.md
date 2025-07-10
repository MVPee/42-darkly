🚨 **EXPLOIT**

The application allows login requests via GET parameters like:
`http://192.168.38.130/index.php?page=signin&username=flag&password=shadow&Login=Login#`

Because there's no rate limiting, timeout, or account lockout, an attacker can write a simple Python script to brute-force the password by repeatedly sending requests with different values.

---

✅ **PATCH**

1. Enforce Rate Limiting / Delay
2. Implement Account Lockout
3. Use Strong Passwords
4. Log and Monitor Login Attempts
