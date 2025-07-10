🚨 **EXPLOIT**

The password recovery form exposes the admin recovery email address directly in a hidden HTML field:

```html
<form action="#" method="POST">
  <input
    type="hidden"
    name="mail"
    value="webmaster@borntosec.com"
    maxlength="15"
  />
  <input type="submit" name="Submit" value="Submit" />
</form>
```

---

✅ **PATCH**

Store the recovery email as a server-side environment variable or configuration.
