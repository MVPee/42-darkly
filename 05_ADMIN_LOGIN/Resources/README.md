🚨 **EXPLOIT**

Download the htpasswd and decrypt the password in MD5 from /whatever retrieved it in /robots.txt
https://md5decrypt.net/en/

---

✅ **PATCH**

1. Don't store .htpasswd in a publicly accessible directory.

```
<Files ".htpasswd">
  Require all denied
</Files>
```
