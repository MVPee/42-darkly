🚨 **EXPLOIT**

Create a script to find all the file in the /.hidden retrieved it in /robots.txt

---

✅ **PATCH**

Use htaccess or nginx to unauthrorized this path/folder

```nginx
    location /.hidden {
        deny all;
        return 403;
    }
```
