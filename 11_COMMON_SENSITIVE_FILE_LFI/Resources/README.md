🚨 **EXPLOIT**

The ?page= parameter is vulnerable to Local File Inclusion (LFI).
You can try to access critical system files via path traversal, such as:

`http://192.168.38.130/?page=/../../../../../../../../../../../etc/passwd`

---

✅ **PATCH**

Sanitize user input in the page parameter and prevent ../ path traversal.
Configure NGINX to deny access outside the web root.

```nginx
location ~* /(config|\.env|\.git|backup|backups|db_dump)\. {
    deny all;
}

# Block attempts to access /etc/passwd or other system files
location ~* /etc/ {
    deny all;
}
```
